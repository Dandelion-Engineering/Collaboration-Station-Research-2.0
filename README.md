# Collaboration Station Research 2.0

> ## Testing status
>
> This is an early, actively tested successor to the original
> [Collaboration Station Research](https://github.com/Dandelion-Engineering/Collaboration-Station-Research)
> framework. Newer AI models broke a central assumption of that design. Its
> mandatory cross-review, repeated verification, and same-state approval loops
> were meant to compensate for agents that did not reliably check their own
> work. Current models already verify and self-correct much more aggressively;
> layering the old instructions on top caused careful agents to spend more time
> reviewing plans and specifications than executing research.
>
> Version 2.0 removes fixed reviewer roles, recurring review cycles, and AI
> approval gates. It trusts agents to move the work forward, correct errors as
> execution exposes them, and verify in proportion to the consequences. It
> retains the protections that bear scientific claims: explicit evidence
> boundaries, strong controls, source provenance, visible consequential changes,
> and reproducible checks matched to the claim.
>
> **The framework is still in testing.** Preliminary use is promising for its
> intended operational change—less recursive review and more forward motion—but
> it has not yet accumulated enough completed projects to establish reliability
> across research domains, datasets, or future agent versions. Expect the
> framework to evolve as those tests expose what works and what does not.

A filesystem-native template for long-running exploratory research by a
researcher and capable AI agents.

The researcher starts with one input: a seed idea in
[`Project Details/Project Details.md`](Project%20Details/Project%20Details.md).
It can be a single question, an unfinished thought, a detailed proposal, or a
plan that already names methods and datasets. The agents turn that seed into a
source-grounded Research Contract, conduct the investigation across sessions,
and leave an honest, inspectable result. When inputs are not supplied, agents
look for suitable public datasets, software, models, tools, and other online
resources within the project's access and resource constraints.

The template is built on
[Collaboration Station 2.0](https://github.com/Dandelion-Engineering/Collaboration-Station-2.0).
Its universal scaffold handles session continuity, subject-focused chats,
concurrent write claims, and path-scoped Git closeout. This repository adds
only the research layer.

## Start a project

1. Copy this template into the new project's folder.
2. Replace the one seed placeholder in
   [`Project Details/Project Details.md`](Project%20Details/Project%20Details.md).
3. Follow [`SETUP.md`](SETUP.md) to initialize Git and launch the agents.

No research questionnaire is required. The remaining template fields in
`Research/` are completed by the agents from the seed and the evidence they
find.

## How the research works

The project follows a simple arc:

1. **Frame and ground.** Agents interpret the seed, inspect the field, and find
   the strongest relevant methods, baselines, controls, evidence, and usable
   resources. Established science is preferred when it fits; genuine gaps get
   a bounded cross-field or novel-method attempt with a higher validation burden.
2. **Contract.** Before designated confirmatory evidence is examined, the agents
   make the question, claim, evidence roles, evaluation, and success/failure
   boundaries explicit in `Research/Research Contract.md`.
3. **Execute and interpret.** The team builds, measures, analyzes, tests rival
   explanations, and corrects consequential problems as actual use reveals
   them.
4. **Conclude and communicate.** The result is reported at its true strength,
   including a clean negative, inconclusive, non-transfer, or evidence-blocked
   or authority-blocked outcome, with a proportionate way to inspect or
   reproduce it.

If the ideal study is infeasible, the project steps down to the closest useful
rung that still serves the seed—such as a feasibility study, data audit,
benchmark, simulation, method prototype, experimental design, or proof of a
current limit. It does not stop at the claim that no research can be done.

These stages may overlap when evidence roles remain clear.

## The research layer

```text
Project Details/
└── Project Details.md         One free-form seed plus durable research standards

Research/
├── Research Contract.md       Active question, claim, evidence roles, methods,
│                              outcome boundaries, and required outputs
├── Changes.md                 Dated append-only consequential changes
├── Questions.md               Append-only questions, defaults, answers,
│                              and closures
├── Status.md                  Compact current state for the researcher
└── References.md              Sources, datasets, software, tools, licenses,
                               and provenance

Outputs/
└── README.md                  Flexible destination for project deliverables

Playbooks/                     On-demand research guidance
agents/                        Per-agent continuity and session records
chats/                         Subject-focused communication
Work/                          Atomic live write coordination
Tools/                         Chat, work-claim, and Git-closeout utilities
```

## What the contract protects

The Research Contract makes the intended question visible before results can
quietly reshape it. It requires the project to name:

- the bounded question and intended claim;
- success, failure, inconclusive, non-transfer, unavailable-evidence, and
  unavailable-authority outcomes;
- evidence roles and access boundaries;
- primary methods, strongest relevant alternatives, and controls;
- metrics, uncertainty, robustness checks, and stopping rules;
- required outputs and the smallest sufficient verification path.

When evidence invalidates part of the plan, the current contract is updated and
the reason is appended to `Research/Changes.md`. The dated change record keeps
the movement visible.

## Collaboration on important work

Agents own their work and move it forward. Another model family may provide an
independent approach, a counterexample, difficult technical help, or one
focused improvement pass when that adds information. The responsible agent
uses what improves the work and continues.

Research protection comes from predeclared boundaries, strong controls, visible
changes, evidence provenance, adversarial testing, and reproducible checks
matched to the claim. `Research/Questions.md` lets agents ask the researcher
without waiting: advisory questions carry a live default, while authority
questions default to not taking the restricted action.

## Outputs fit the project

Every project leaves a final result, a methods and evidence record, source and
data provenance, visible exclusions and limitations, and an inspectable path
through the load-bearing evidence. Those needs may be served by one report or
by several artifacts.

A technical report, accessible explanation, study guide, dashboard, dataset
card, simulation, or full reproducibility packet is created when the Research
Contract identifies a reader or boundary that needs it—not because every
project must fill the same shelf.

## Requirements

- Python 3
- Git
- one or more agents with filesystem access to the project folder
- any domain-specific tools or environments the eventual Research Contract
  requires

The bundled tools use only Python's standard library. Run their tests with:

```shell
python -B Tools/test_chat.py
python -B Tools/test_work.py
python -B Tools/test_closeout.py
```

## Design and licensing

[`DESIGN-RATIONALE.md`](DESIGN-RATIONALE.md) explains what was retained,
removed, and transformed from the previous Collaboration Station Research
template. [`LICENSING.md`](LICENSING.md) maps the MIT license for code and the
CC BY 4.0 license for prose.

Created by Dandelion Engineering as a reusable research framework.
