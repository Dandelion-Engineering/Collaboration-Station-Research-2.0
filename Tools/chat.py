#!/usr/bin/env python3
"""Safe append and in-session inbox for Collaboration Station transcripts.

Usage:
    python -B Tools/chat.py check "<transcript.md>"
    python -B Tools/chat.py post "<transcript.md>" --agent Claude --session 4 \
        --body-file "<body.md>" --expect-bytes 5728
    python -B Tools/chat.py verify "<transcript.md>"
    python -B Tools/chat.py inbox --agent Claude
    python -B Tools/chat.py wait --agent Claude --timeout 180
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time

CRLF = b"\r\n"
LF = b"\n"
OK = 0
PROBLEM = 1
POSTED_UNVERIFIED = 2
NOTHING_ARRIVED = 3

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except (AttributeError, OSError):
    pass


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def sha12(data):
    return sha256_hex(data)[:12]


def detect_eol(data):
    crlf = data.count(CRLF)
    bare_lf = data.count(LF) - crlf
    bare_cr = data.count(b"\r") - crlf
    if crlf == 0 and bare_lf == 0:
        return CRLF, crlf, bare_lf, bare_cr
    return (CRLF if crlf >= bare_lf else LF), crlf, bare_lf, bare_cr


def tz_abbrev():
    name = time.strftime("%Z")
    if not name:
        return ""
    if " " in name:
        return "".join(word[0] for word in name.split() if word).upper()
    return name


def timestamp():
    return time.strftime("%Y-%m-%d %H:%M ") + tz_abbrev()


def normalize(text, eol):
    unix = text.replace("\r\n", "\n").replace("\r", "\n")
    return unix.replace("\n", eol.decode("ascii"))


def show(data):
    return data.decode("utf-8", errors="replace").replace("\r\n", "\n")


def die(msg):
    sys.stdout.write("REFUSED: " + msg + "\n")
    sys.exit(PROBLEM)


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    d = here
    while True:
        if os.path.isfile(os.path.join(d, "AgentPrompt.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            die("no AgentPrompt.md in any directory above %s, so the project root cannot be determined" % here)
        d = parent


def tools_rel(root):
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        relpath = os.path.relpath(here, root)
        if not relpath.startswith(os.pardir):
            return relpath
    except ValueError:
        pass
    return "Tools"


def state_path(agent, root=None):
    root = root or repo_root()
    return os.path.join(root, tools_rel(root), ".state", "inbox-%s.json" % agent.lower())


def last_report_path(agent, root=None):
    root = root or repo_root()
    return os.path.join(root, tools_rel(root), ".state", "last-inbox-%s.txt" % agent.lower())


def rel(path, root):
    return os.path.relpath(os.path.abspath(path), root).replace(os.sep, "/")


def find_transcripts(agent, root=None):
    root = root or repo_root()
    chats_dir = os.path.join(root, "chats")
    found = []
    if not os.path.isdir(chats_dir):
        return found
    wanted = agent.strip().lower()
    for channel in sorted(os.listdir(chats_dir)):
        channel_dir = os.path.join(chats_dir, channel)
        if not os.path.isdir(channel_dir):
            continue
        parts = [p.strip().lower() for p in channel.split("-")]
        if wanted not in parts:
            continue
        for dirpath, _dirnames, filenames in os.walk(channel_dir):
            for name in sorted(filenames):
                if name.endswith("Active.md"):
                    found.append(os.path.join(dirpath, name))
    return sorted(found)


def load_state(agent, root=None):
    path = state_path(agent, root)
    if not os.path.exists(path):
        return {"agent": agent, "files": {}}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (ValueError, OSError):
        return {"agent": agent, "files": {}}
    data.setdefault("files", {})
    data.setdefault("agent", agent)
    return data


def save_last_report(agent, text, root=None):
    path = last_report_path(agent, root)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8", errors="replace", newline="\n") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except OSError:
        pass
    return path


def save_state(agent, state, root=None):
    path = state_path(agent, root)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
    os.replace(tmp, path)


def scan_inbox(agent, root=None):
    root = root or repo_root()
    state = load_state(agent, root)
    results = []
    for path in find_transcripts(agent, root):
        key = rel(path, root)
        data = read_bytes(path)
        prior = state["files"].get(key)
        item = {"path": path, "key": key, "bytes": len(data), "data": data}
        if prior is None:
            item["status"] = "unseen"
        elif len(data) < prior["bytes"]:
            item["status"] = "rewritten"
            item["detail"] = "shrank from %d to %d bytes" % (prior["bytes"], len(data))
        elif sha256_hex(data[: prior["bytes"]]) != prior["sha256"]:
            item["status"] = "rewritten"
            item["detail"] = "the first %d bytes are no longer what you read" % prior["bytes"]
        elif len(data) == prior["bytes"]:
            item["status"] = "unchanged"
        else:
            item["status"] = "new"
            item["added"] = data[prior["bytes"] :]
        results.append(item)
    return state, results


def advance(state, item):
    state["files"][item["key"]] = {
        "bytes": item["bytes"],
        "sha256": sha256_hex(item["data"]),
        "marked": timestamp(),
    }


def cmd_check(args):
    if not os.path.exists(args.file):
        sys.stdout.write("File does not exist: %s\n" % args.file)
        return PROBLEM
    data = read_bytes(args.file)
    eol, crlf, bare_lf, bare_cr = detect_eol(data)
    sys.stdout.write("file        : %s\n" % args.file)
    sys.stdout.write("bytes       : %d      <-- pass this to --expect-bytes\n" % len(data))
    sys.stdout.write("sha256(12)  : %s\n" % sha12(data))
    sys.stdout.write(
        "line endings: %s (crlf=%d bare_lf=%d bare_cr=%d)\n"
        % ("CRLF" if eol == CRLF else "LF", crlf, bare_lf, bare_cr)
    )
    sys.stdout.write("ends w/ nl  : %s\n" % ("yes" if data.endswith(LF) else "NO - will be repaired on post"))
    sys.stdout.write("\n--- last 400 bytes ---\n")
    sys.stdout.write(show(data[-400:]))
    sys.stdout.write("\n--- end ---\n")
    return OK


def cmd_post(args):
    if not os.path.exists(args.file):
        die(
            "transcript does not exist: %s\n"
            "         Create the chat folder and file first; this tool only appends." % args.file
        )
    before = read_bytes(args.file)
    if len(before) != args.expect_bytes:
        delta = len(before) - args.expect_bytes
        sys.stdout.write("REFUSED: the transcript changed since you read it.\n")
        sys.stdout.write("  you read : %d bytes\n" % args.expect_bytes)
        sys.stdout.write("  now      : %d bytes (%+d)\n" % (len(before), delta))
        if delta > 0:
            sys.stdout.write("\n--- arrived while you were composing ---\n")
            sys.stdout.write(show(before[args.expect_bytes :]))
            sys.stdout.write("--- end ---\n")
            sys.stdout.write(
                "\nRead the above, revise if it changes your message, then post again\n"
                "with --expect-bytes %d\n" % len(before)
            )
        else:
            sys.stdout.write(
                "\nThe file SHRANK. Someone overwrote or truncated it. Do not post.\n"
                "Recover it from git before writing anything.\n"
            )
        return PROBLEM

    body = read_bytes(args.body_file).decode("utf-8").strip()
    if not body:
        die("body file is empty: %s" % args.body_file)

    eol, _, bare_lf_b, bare_cr_b = detect_eol(before)
    stamp = timestamp()
    header = "**%s (Session %s, %s):**" % (args.agent, args.session, stamp)
    lead = "" if (before.endswith(LF) or len(before) == 0) else "\n"
    block = normalize("%s\n---\n\n%s\n\n%s\n" % (lead, header, body), eol)
    block_bytes = block.encode("utf-8")

    if args.dry_run:
        sys.stdout.write("DRY RUN - nothing written.\n")
        sys.stdout.write("target      : %s\n" % args.file)
        sys.stdout.write("line endings: %s\n" % ("CRLF" if eol == CRLF else "LF"))
        sys.stdout.write("appending   : %d bytes\n" % len(block_bytes))
        sys.stdout.write("header      : %s\n" % header)
        return OK

    with open(args.file, "ab") as fh:
        fh.write(block_bytes)
        fh.flush()
        os.fsync(fh.fileno())

    after = read_bytes(args.file)
    problems = []
    notes = []
    if not after.startswith(before):
        problems.append("prior content is no longer a byte-exact prefix (DATA LOSS)")
    else:
        appended = after[len(before) :]
        if appended != block_bytes:
            problems.append(
                "the bytes after the old end of file are not the bytes we wrote "
                "(%d appended, %d intended) - another writer appended concurrently"
                % (len(appended), len(block_bytes))
            )
        else:
            occurrences = appended.decode("utf-8").count(header)
            if occurrences != 1:
                problems.append("header appears %d times in the appended block, expected 1" % occurrences)

    _, _, bare_lf_a, bare_cr_a = detect_eol(after)
    new_bare_lf = bare_lf_a - bare_lf_b
    new_bare_cr = bare_cr_a - bare_cr_b
    if eol == CRLF and (new_bare_lf or new_bare_cr):
        problems.append(
            "this append introduced %d bare LF and %d bare CR into a CRLF transcript"
            % (new_bare_lf, new_bare_cr)
        )
    if eol == LF and new_bare_cr:
        problems.append("this append introduced %d bare CR into an LF transcript" % new_bare_cr)
    if eol == CRLF and (bare_lf_b or bare_cr_b):
        notes.append("the transcript already had %d bare LF / %d bare CR before this post" % (bare_lf_b, bare_cr_b))
    if eol == LF and bare_cr_b:
        notes.append("the transcript already had %d bare CR before this post" % bare_cr_b)
    try:
        if "�" in before.decode("utf-8"):
            notes.append("the transcript already contained a replacement character")
    except UnicodeDecodeError as exc:
        notes.append("the transcript was not valid UTF-8 before this post: %s" % exc)

    if problems:
        sys.stdout.write("POSTED, BUT VERIFICATION FAILED:\n")
        for problem in problems:
            sys.stdout.write("  - %s\n" % problem)
        sys.stdout.write(
            "\nYour message was appended, but the file is not in the state this tool intended.\n"
            "Inspect it before posting again. Do not simply retry: the message may already be present.\n"
        )
        return POSTED_UNVERIFIED

    root = getattr(args, "root", None) or repo_root()
    state = load_state(args.agent, root)
    key = rel(args.file, root)
    prior = state["files"].get(key)
    unread_bytes = 0
    if prior is not None:
        read_through = prior["bytes"] == len(before) and sha256_hex(before) == prior["sha256"]
        if read_through:
            state["files"][key] = {"bytes": len(after), "sha256": sha256_hex(after), "marked": stamp}
            save_state(args.agent, state, root)
        else:
            unread_bytes = len(before) - prior["bytes"]

    sys.stdout.write("POSTED and verified.\n")
    sys.stdout.write("  file    : %s\n" % args.file)
    sys.stdout.write("  header  : %s\n" % header)
    sys.stdout.write("  bytes   : %d -> %d (+%d)\n" % (len(before), len(after), len(block_bytes)))
    sys.stdout.write("  endings : %s preserved\n" % ("CRLF" if eol == CRLF else "LF"))
    for note in notes:
        sys.stdout.write("  note    : %s\n" % note)
    if unread_bytes > 0:
        sys.stdout.write(
            "\n  UNREAD  : %d bytes arrived before your post that `inbox` has never\n"
            "            shown you. Your checkpoint was LEFT at %d so they are not\n"
            "            lost. Run `inbox` now -- it will display them.\n"
            % (unread_bytes, prior["bytes"])
        )
    return OK


def cmd_verify(args):
    if not os.path.exists(args.file):
        sys.stdout.write("File does not exist: %s\n" % args.file)
        return PROBLEM
    data = read_bytes(args.file)
    eol, crlf, bare_lf, bare_cr = detect_eol(data)
    problems = []
    if eol == CRLF and (bare_lf or bare_cr):
        problems.append("mixed line endings in a CRLF file: %d bare LF, %d bare CR" % (bare_lf, bare_cr))
    if eol == LF and bare_cr:
        problems.append("stray CR in an LF file: %d" % bare_cr)
    if data and not data.endswith(LF):
        problems.append("no trailing newline - the next append would weld onto the last line")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        sys.stdout.write("INVALID: not valid UTF-8: %s\n" % exc)
        return PROBLEM
    if "�" in text:
        problems.append("contains a replacement character (encoding damage)")
    headers = re.findall(r"^\*\*(.+?)\s*\(Session\s+(\S+?),\s*(.+?)\):\*\*", text, re.MULTILINE)
    plain = re.findall(r"^\*\*([A-Za-z]+):\*\*", text, re.MULTILINE)
    sys.stdout.write("file          : %s\n" % args.file)
    sys.stdout.write("bytes         : %d\n" % len(data))
    sys.stdout.write("line endings  : %s\n" % ("CRLF" if eol == CRLF else "LF"))
    sys.stdout.write("agent messages: %d\n" % len(headers))
    sys.stdout.write("plain headers : %d %s\n" % (len(plain), sorted(set(plain)) if plain else ""))
    for who, session, when in headers:
        sys.stdout.write("  - %-8s session %-4s %s\n" % (who, session, when))
    if problems:
        sys.stdout.write("\nPROBLEMS:\n")
        for problem in problems:
            sys.stdout.write("  - %s\n" % problem)
        return PROBLEM
    sys.stdout.write("\nOK - no problems found.\n")
    return OK


def report_inbox(agent, state, results, root=None, mark_only=False, quiet_when_empty=False):
    changed = [r for r in results if r["status"] in ("new", "unseen")]
    broken = [r for r in results if r["status"] == "rewritten"]
    captured = []

    class _Out(object):
        @staticmethod
        def write(text):
            captured.append(text)
            sys.stdout.write(text)

    out = _Out
    if not results:
        sys.stdout.write("No transcripts found for %s.\n" % agent)
        return OK
    if quiet_when_empty and not changed and not broken:
        return NOTHING_ARRIVED
    if mark_only:
        for item in results:
            if item["status"] != "rewritten":
                advance(state, item)
        save_state(agent, state, root)
        sys.stdout.write(
            "Marked %d transcript(s) as read for %s at %s.\n"
            % (len([r for r in results if r["status"] != "rewritten"]), agent, timestamp())
        )
        for item in broken:
            sys.stdout.write("  NOT marked (rewritten): %s - %s\n" % (item["key"], item["detail"]))
        return PROBLEM if broken else OK

    out.write("Inbox checkpoint for %s - %s\n" % (agent, timestamp()))
    out.write(
        "%d transcript(s): %d new, %d unseen, %d unchanged, %d rewritten\n\n"
        % (
            len(results),
            len([r for r in results if r["status"] == "new"]),
            len([r for r in results if r["status"] == "unseen"]),
            len([r for r in results if r["status"] == "unchanged"]),
            len(broken),
        )
    )
    for item in results:
        if item["status"] == "unchanged":
            out.write("  unchanged : %s (%d bytes)\n" % (item["key"], item["bytes"]))
    for item in broken:
        out.write("\n!! REWRITTEN : %s\n" % item["key"])
        out.write("   %s\n" % item["detail"])
        out.write(
            "   A transcript is append-only. Do not post here; read the file and git diff it.\n"
            "   The checkpoint was not advanced.\n"
        )
    for item in results:
        if item["status"] == "unseen":
            out.write("\n>> NO CHECKPOINT YET : %s (%d bytes)\n" % (item["key"], item["bytes"]))
            out.write("   Read this file directly. Recording it now as your baseline.\n")
            advance(state, item)
    for item in results:
        if item["status"] == "new":
            out.write("\n>> NEW IN %s (+%d bytes)\n" % (item["key"], len(item["added"])))
            out.write("--- arrived since your last checkpoint ---\n")
            out.write(show(item["added"]))
            if not item["added"].endswith(LF):
                out.write("\n")
            out.write("--- end ---\n")
            advance(state, item)
    save_state(agent, state, root)
    if not changed and not broken:
        out.write("\nNothing new. Carry on.\n")
    elif changed:
        out.write("\nRead the above before your next reply or work unit.\n")
    if changed:
        saved = save_last_report(agent, "".join(captured), root)
        out.write("\nFull copy of this report: %s\n" % rel(saved, root or repo_root()))
    out.write(
        "=== END OF INBOX (%d new, %d unseen, %d rewritten) ===\n"
        % (
            len([r for r in results if r["status"] == "new"]),
            len([r for r in results if r["status"] == "unseen"]),
            len(broken),
        )
    )
    return PROBLEM if broken else OK


def cmd_inbox(args):
    root = args.root or repo_root()
    state, results = scan_inbox(args.agent, root)
    return report_inbox(args.agent, state, results, root=root, mark_only=args.mark)


def cmd_wait(args):
    root = args.root or repo_root()
    timeout = max(1, min(args.timeout, 900))
    interval = max(1, min(args.interval, 60))
    deadline = time.time() + timeout
    sys.stdout.write(
        "Waiting up to %ds for new content in %s's transcripts (checking every %ds).\n"
        % (timeout, args.agent, interval)
    )
    sys.stdout.flush()
    while True:
        state, results = scan_inbox(args.agent, root)
        code = report_inbox(args.agent, state, results, root=root, quiet_when_empty=True)
        if code != NOTHING_ARRIVED:
            return code
        if time.time() >= deadline:
            sys.stdout.write(
                "Nothing arrived within %ds. Continue or close out according to the actual dependency; silence is not an answer.\n"
                % timeout
            )
            return NOTHING_ARRIVED
        time.sleep(min(interval, max(1, deadline - time.time())))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Safe append and in-session inbox for project chat transcripts.")
    subs = parser.add_subparsers(dest="command")
    p_check = subs.add_parser("check", help="size, hash, line endings, and tail")
    p_check.add_argument("file")
    p_check.set_defaults(func=cmd_check)
    p_post = subs.add_parser("post", help="append one message, safely")
    p_post.add_argument("file")
    p_post.add_argument("--agent", required=True)
    p_post.add_argument("--session", required=True)
    p_post.add_argument("--body-file", required=True)
    p_post.add_argument("--expect-bytes", type=int, required=True)
    p_post.add_argument("--dry-run", action="store_true")
    p_post.add_argument("--root", default=None, help=argparse.SUPPRESS)
    p_post.set_defaults(func=cmd_post)
    p_verify = subs.add_parser("verify", help="integrity check an existing transcript")
    p_verify.add_argument("file")
    p_verify.set_defaults(func=cmd_verify)
    p_inbox = subs.add_parser("inbox", help="show what arrived since your last checkpoint")
    p_inbox.add_argument("--agent", required=True)
    p_inbox.add_argument("--mark", action="store_true")
    p_inbox.add_argument("--root", default=None, help=argparse.SUPPRESS)
    p_inbox.set_defaults(func=cmd_inbox)
    p_wait = subs.add_parser("wait", help="poll for new content, bounded, then return")
    p_wait.add_argument("--agent", required=True)
    p_wait.add_argument("--timeout", type=int, default=120)
    p_wait.add_argument("--interval", type=int, default=5)
    p_wait.add_argument("--root", default=None, help=argparse.SUPPRESS)
    p_wait.set_defaults(func=cmd_wait)
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return PROBLEM
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
