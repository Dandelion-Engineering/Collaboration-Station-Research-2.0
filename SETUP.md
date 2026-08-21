# Set Up and Launch a Research Project

## The only required research input

Open `Project Details/Project Details.md` and replace:

```text
{{PASTE_THE_SEED_IDEA_HERE}}
```

with the researcher's seed idea. That is the only research field the human must
complete before launch. Do not fill out `Research/Research Contract.md` or the
other `Research/` templates for the researcher; the agents build those from the
seed and current evidence.

The seed can include constraints, methods, links, local dataset paths, preferred
outputs, or a fully specified plan, but none are required. Preserve the seed as
written after launch so the original intent remains inspectable.

## Prepare the folder

1. Copy the complete template to a new project folder.
2. Put the seed idea in the one location above.
3. Ensure Python 3 and Git are available.
4. Initialize the folder as a Git repository. Connect the private or public
   remote appropriate for the project when one is wanted; do not publish merely
   as part of setup.
5. Make the initial commit before agent work begins.
6. Give each agent filesystem access to the same project root.

Optional setup:

- Rename the default `agents/Claude` and `agents/Codex` workspaces and matching
  chat channels if different agents will participate.
- Add project-specific ignore rules for private data, generated outputs, model
  weights, and environments before those files are created.
- Configure repository visibility, data storage, credentials, and publication
  only through the appropriate human-controlled systems.

## Launch command

Inside a session, the project instruction is:

> Follow the instructions in `AgentPrompt.md`.

For a manual launch, give that instruction from the project root. For recurring
automations, wrap it in the per-agent lock gate below so an interrupted or still
running session fails closed.

### Codex launcher wrapper

```text
First, check for .codex-session.lock in the project root. If .codex-session.lock exists, do no project work. Simply end this task by saying another Codex session is still active. If .codex-session.lock does not exist, create .codex-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md. When the AgentPrompt.md workflow is complete, delete .codex-session.lock.
```

### Claude launcher wrapper

```text
First, check for .claude-session.lock in the project root. If .claude-session.lock exists, do no project work. Simply end this task by saying another Claude session is still active. If .claude-session.lock does not exist, create .claude-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md. When the AgentPrompt.md workflow is complete, delete .claude-session.lock.
```

Use a distinct lock filename for any additional agent. A session removes only
its own lock and only after its complete closeout. Never remove a lock just
because it looks old; first verify that its agent no longer has a live session.

Launcher locks prevent two sessions of the same agent from overlapping. They do
not replace `Work/` claims, which coordinate writes between different agents.

## What the first agents do

The first useful sessions should:

1. read the seed without demanding a more formal restatement;
2. inspect any resources it names, and search for suitable public datasets,
   software, models, tools, and other online materials when inputs are missing;
3. use established methods when they fit; when they do not, make a bounded
   cross-field, adaptation, or novel-method attempt with an explicit validation
   burden and stopping rule;
4. choose the closest useful investigation that preserves the seed's purpose
   and fits the available compute, time, money, materials, access, safety, and
   legal boundaries;
5. record helpful researcher questions with live defaults instead of waiting;
6. build the Research Contract and record material uncertainty;
7. begin exploratory work that can proceed safely while the contract is drafted;
8. activate the contract before accessing evidence designated confirmatory or
   held out.

If a seed is already detailed, agents should use that detail rather than
restarting the design from zero. If it is only a sentence, they should supply
the missing technical structure themselves.

## Validate the scaffold

The bundled tools are standard-library programs. From the project root run:

```shell
python -B Tools/test_chat.py
python -B Tools/test_work.py
python -B Tools/test_closeout.py
```

When a Git remote is configured, verify before the first real closeout that it
accepts a normal push from the environment in which agent sessions run. Without
a remote, `Tools/closeout.py` commits locally, reports that no push occurred,
and ends the session successfully.

## Publication and citation

Local research does not require publication metadata to be decided at launch.
Before releasing a project publicly:

- replace the framework metadata in `CITATION.cff` with the project's title,
  authorship, version, date, and repository URL;
- update `LICENSING.md` for project-owned code and prose;
- document every dataset, model, and third-party asset under its own license;
- confirm that no private data, credentials, ignored local artifacts, or
  internal-only records are being published;
- obtain explicit human authorization for the release.
