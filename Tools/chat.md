# `chat.py`

`chat.py` protects the only shared files that multiple participants append to directly: active chat transcripts.

## Chat concepts

Read `chats/README.md` first. In brief:

- chats are organized by participant channel and subject;
- `Active` means the conversation may still require attention;
- `Concluded` means no immediate response is expected;
- concluded does not mean approved or unanimous;
- `inbox` discovers only active transcripts.

## Inbox

At session start, immediately before opening a work claim, before closing one, and at the final closeout check:

```shell
python -B Tools/chat.py inbox --agent Claude
```

The first run establishes a checkpoint. Later runs show exactly what was appended after it. If output is truncated, recover the full report from `Tools/.state/last-inbox-<agent>.txt`.

## Read before posting

Read the full transcript, then obtain its current byte count:

```shell
python -B Tools/chat.py check "chats/<channel>/<subject>/<subject> - Active.md"
```

Write only the message body to a separate UTF-8 file, then post:

```shell
python -B Tools/chat.py post "chats/<channel>/<subject>/<subject> - Active.md" \
  --agent Claude \
  --session 4 \
  --body-file "<message-body.md>" \
  --expect-bytes 5728
```

If the transcript changed while you were composing, the post is refused and the new bytes are shown. Read them before deciding whether to post again. There is deliberately no automatic retry.

## Verify a transcript

```shell
python -B Tools/chat.py verify "chats/<channel>/<subject>/<subject> - Active.md"
```

This checks UTF-8, line endings, the trailing newline, replacement characters, and agent message headers without rewriting the file.

## Bounded wait

```shell
python -B Tools/chat.py wait --agent Claude --timeout 180
```

Use `wait` only when a specific reply is the identified dependency and waiting is more useful than another work unit. It is capped at 900 seconds. Silence is simply silence; it is not an answer or an approval.

Do not use `wait` during final closeout. The required final operation is one ordinary `inbox` check before the dry run and commit.

## Final inbox rule

The final inbox check occurs after the session report, context summary, work-claim update, and handoff are ready—but before `closeout.py`.

If the final inbox delivers a message that materially changes the work, resume the session, update the durable state, and perform the final inbox check again.

After `closeout.py` commits and pushes, do not run `chat.py`. The session is over.

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | command completed and any append was verified |
| `1` | refused input, stale state, or integrity problem |
| `2` | bytes were appended but verification failed; inspect before any retry |
| `3` | bounded wait ended with nothing new |
