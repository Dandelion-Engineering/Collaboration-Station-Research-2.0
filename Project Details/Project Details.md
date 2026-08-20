# Research Project Details

This template turns one seed idea into a complete exploratory research project.
The researcher provides the seed below. The agents do the grounding, scope the
investigation, build the Research Contract, conduct the work, and produce the
outputs the resulting claim actually needs.

## Seed idea — researcher input

Replace the single placeholder below. Write as much or as little as you have: a
question, a rough thought, a long ramble, a developed hypothesis, or a detailed
plan with methods and datasets. Plain language is welcome. No other setup form
is required.

`{{PASTE_THE_SEED_IDEA_HERE}}`

The seed is preserved as the project's original input. Agents may sharpen it,
identify a more answerable first rung, or explain why part of it is not feasible,
but they do not silently replace its purpose.

## What the agents do with the seed

The first sessions translate the seed into an active
`Research/Research Contract.md`. Agents should infer routine details, research
the field, inspect any named resources, and choose defensible defaults. They do
not make the researcher complete a questionnaire before work can begin.

Ask the researcher only when:

- different interpretations would produce materially different projects and
  the seed does not support a responsible choice;
- access, identity, consent, private data, credentials, spending, publication,
  or another human-only action is required;
- the seed contains conflicting protected constraints; or
- proceeding would create a meaningful safety, legal, ethical, or privacy risk.

When the ideal project is not feasible, preserve the underlying purpose and
choose the closest useful investigation that can honestly be answered with the
available evidence. Record the boundary in the contract. Do not substitute an
easier question merely because it is easier.

## Research sources of truth

The general source-of-truth order in `AgentPrompt.md` applies. Within this
research layer, use:

1. this file for the original seed and project-wide research standards;
2. `Research/Research Contract.md` for the active question, intended claim,
   evidence roles, methods, outcome boundaries, and required outputs;
3. `Research/Changes.md` for dated consequential changes to the contract;
4. `Research/Status.md` for the compact current state;
5. current methods, code, data records, and outputs for what was actually done;
6. `Research/References.md` for source and data provenance.

Historical plans and chats explain how the work developed. They do not override
the active contract and its visible change record.

## Session entry for research work

After the universal startup in `AgentPrompt.md`, read:

1. `Research/Status.md`;
2. `Research/Research Contract.md`;
3. the latest relevant entries in `Research/Changes.md`;
4. only the methods, outputs, sources, chats, and playbooks needed for the work
   selected.

Do not load every historical artifact by default.

## Research playbooks

`Playbooks/` holds on-demand craft guidance for recurring kinds of research
work. Read the playbook that matches the work in front of you, when that work
begins. Do not preload the set.

| Playbook | Read it when |
|---|---|
| [Grounding the Seed](../Playbooks/grounding-the-seed.md) | Turning the seed idea into a bounded, source-grounded investigation |
| [Writing the Research Contract](../Playbooks/writing-the-research-contract.md) | Building or sharpening `Research/Research Contract.md` |
| [Running the Investigation](../Playbooks/running-the-investigation.md) | Building, measuring, analyzing, and interpreting under an active contract |
| [Reporting the Result](../Playbooks/reporting-the-result.md) | Producing the outputs the contract promised |
| [Asking for a Focused Improvement](../Playbooks/asking-for-a-focused-improvement.md) | Another participant's perspective would materially improve important work |

A playbook adds craft guidance for one task; it does not restate the standards,
stages, change rules, or completion conditions in this file. Add a playbook, and
its row in this table, when a kind of work recurs and its guidance is worth more
than the cost of reading it. Otherwise, trust the team.

## Research integrity

### Ground choices in evidence

Begin method, dataset, baseline, control, metric, and reporting choices with
credible sources and current field practice. Record a source when it affects a
decision. When the field supplies no adequate method, state what is new, why it
is needed, and how it will be tested.

### Make the intended claim visible before results can reshape it

Activate the Research Contract before examining evidence designated there as
confirmatory or held out. The contract states the question, intended claim,
inputs, methods, strongest relevant comparisons, evaluation, and what would
count as success, failure, inconclusive, or non-transfer.

Exploratory work may precede activation when it is clearly labelled and cannot
silently become confirmatory evidence.

### Protect evidence roles

Classify important evidence as exploratory, development, confirmatory, held
out, or external validation. Record access and exclusion rules where knowledge
of the evidence could influence a choice. Reused development evidence is not
held out.

Use mechanical protections when the claim needs them: fixed splits, immutable
manifests, seeded procedures, append-only records, or executable checks. Match
the protection to the actual risk; do not substitute a universal review ritual.

### Use strong comparisons and controls

Compare against the strongest relevant baseline or alternative available under
the project's constraints. Include controls that can expose leakage, shortcuts,
confounds, or trivial explanations. Report comparisons that challenge the
preferred interpretation, not only those it beats.

### Keep exclusions and failed work visible

Define eligibility and exclusion rules before they can be tuned to a result
when practical. Record every material excluded sample, failed run, protocol
deviation, and abandoned analysis with its reason. Preserve negative and
inconclusive outcomes as legitimate endpoints.

### Match claims to evidence

Report uncertainty, sensitivity, assumptions, and limitations at the strength
the evidence supports. Do not loosen a threshold after seeing a result, promote
an exploratory finding into the headline claim, hide a strong control, or turn
an underpowered null into evidence of no effect.

### Make load-bearing evidence inspectable

The contract names the smallest sufficient reproduction or verification path
for the project. It may be a runnable packet, simulation, notebook, test
harness, worked example, dataset manifest, visual comparison, report appendix,
or another form suited to the claim. A larger packet is not automatically a
stronger one.

## How the research moves

These stages describe the work; they are not AI approval gates.

1. **Frame and ground.** Sharpen the seed, inspect the field, and identify the
   materials, risks, strongest baselines, and plausible outcome shapes.
2. **Contract.** Complete and activate the Research Contract before designated
   confirmatory evidence is inspected.
3. **Execute and interpret.** Build, measure, analyze, test alternatives, and
   correct consequential problems as they are found.
4. **Conclude and communicate.** State the result at true strength, deliver the
   outputs promised by the contract, and leave an inspectable path through the
   evidence.

Stages may overlap. A method can be prototyped while the contract is being
sharpened if its evidence remains exploratory. Drafting can begin before all
analysis ends. Work moves forward when its necessary state is usable, not when
an AI signs it.

## Changing the research plan

Consequential changes go in `Research/Changes.md` before the changed path is
treated as active. A consequential change alters the question, headline claim,
evidence role, eligibility rule, method family, strongest baseline, primary
metric, success boundary, stopping rule, or required output.

Each entry states what was learned, why the previous path no longer fits, what
changes, what does not change, and how interpretation boundaries move. Update
the clean current state in the Research Contract and link the change entry.

Routine implementation choices and corrections that do not move a research
boundary belong in code, methods, or session records, not the change log.

## Collaboration model

One agent leads each live write scope through `Work/`. Other participants may
contribute independent analysis, alternatives, counterexamples, or one focused
improvement pass when that adds information.

For a focused improvement:

1. ask a bounded question and identify the artifact or decision it concerns;
2. the contributor returns one set of improvements or an independent result;
3. the responsible agent decides what to use, records material uncertainty,
   and moves forward.

An improvement is not approval. It creates no required response round,
reinspection, exact-state signature, or consensus requirement. Later use may
reveal defects; material defects are corrected in the current state and carried
into future outputs.

## Human authority

Agents own routine research, design, implementation, analysis, documentation,
and local validation within the seed's purpose and the active contract.

The human director is required for:

- identity, credentials, consent, or access that belongs to a person;
- spending, purchases, contracts, or paid accounts;
- contact with external people or organizations;
- publication, public release, or changes to public systems;
- destructive or irreversible external actions;
- a material change to the seed's purpose.

If one lane needs the director, open a focused human chat that states what is
needed, why, what is blocked, and any fallback, then continue other useful work.
Silence is not permission.

## Keeping the researcher informed

`Research/Status.md` is the compact current-state surface. Update it when the
question changes, a consequential change is adopted, a major result or blocker
appears, a required output becomes usable, or the project concludes. Do not
turn it into a session journal.

Session summaries preserve detailed work. Focused chats carry questions that
need a response. Final outputs carry the durable result.

## Required outputs

The Research Contract chooses the outputs needed for the actual claim and its
readers. Every project leaves:

- a final result statement that answers the research question at true strength;
- a methods and evidence record sufficient to understand what was done;
- a source and data-provenance record;
- a limitations, exclusions, and deviations record;
- an inspectable reproduction or verification path proportionate to the claim.

These may be combined. A technical report, public explainer, study guide,
dashboard, dataset card, or full reproducibility packet is required only when
the contract identifies a reader or boundary that needs it.

## Completion

The project is complete when:

- the active Research Contract is coherent and its consequential changes are
  visible;
- the question is answered as success, failure, inconclusive, non-transfer, or
  explicitly blocked by unavailable evidence;
- the outputs promised in the contract exist and agree with one another;
- important baselines, controls, exclusions, deviations, and limitations are
  reported;
- the promised reproduction or verification path works to the degree claimed;
- `Research/Status.md` records the terminal state and useful next guidance;
- no unresolved template placeholder remains in a project-authored output;
- relevant tool and project checks pass.

Completion does not require every possible improvement, AI consensus, a Review
Card, a second inspection of revisions, or resolution of every difference in
judgment.
