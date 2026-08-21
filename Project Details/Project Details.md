# Research Project Details

This template turns one seed idea into a complete exploratory research project.
The researcher provides the seed below. The agents do the grounding, scope the
investigation, build the Research Contract, conduct the work, and produce the
outputs the resulting claim actually needs.

In this research layer, **researcher** means the human director named in
`AgentPrompt.md`.

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
the field, inspect any named resources, actively look for suitable public
datasets, software, models, tools, and other online materials when none are
provided, and choose defensible defaults. They do not make the researcher
complete a questionnaire before work can begin.

### Keep the investigation proportionate and researchable

Match the investigation to the ambition of the seed and to the available
compute, time, money, materials, access, safety, and legal boundaries.

- When established science can answer the question, use the strongest relevant
  established methods rather than inventing novelty for its own sake.
- When no adequate method is established, make a bounded creative attempt:
  inspect adjacent fields for transferable methods, combine compatible ideas,
  or develop a new approach. A new approach carries a high evidential burden;
  test the properties needed for the claim against strong alternatives,
  controls, and known cases before relying on it.
- If the ideal study remains infeasible after an honest, contract-bounded
  attempt, reduce it to the closest useful rung that still serves the seed's
  purpose. That rung may be a feasibility study, data audit, benchmark,
  simulation, theoretical analysis, method prototype, experimental design, or
  proof of a current limit.

Do not end at “no research project can be done.” Every seed should produce the
most informative feasible project and an honest result, even when that result
only establishes what can be tested now, what failed, and what a stronger study
would require. Record material scope changes in `Research/Changes.md`; do not
silently replace the seed with an unrelated easier question.

### Questions do not create a wait state

Agents may ask for preferences, clarification, or human-only authority whenever
an answer would help. Record each question in the append-only
`Research/Questions.md` register and link any active chat.

Treat `Research/Questions.md` as the project-specific researcher-request surface
referenced by `AgentPrompt.md`; inspect it before using the completed-project
shortcut.

An advisory question states the defensible default already in force, and work
continues. An authority question defaults to **do not take the restricted
action**; agents route around it, narrow the result honestly, or finish in a
bounded authority-blocked state. An unanswered question never authorizes
access, consent, spending, publication, external contact, a material change of
purpose, or another human-only action. If a default changes a research boundary,
record the change separately in `Research/Changes.md`.

## Research sources of truth

The general source-of-truth order in `AgentPrompt.md` applies. Within this
research layer, use:

1. this file for the original seed and project-wide research standards;
2. `Research/Research Contract.md` for the active question, intended claim,
   evidence roles, methods, outcome boundaries, and required outputs;
3. `Research/Changes.md` for dated consequential changes to the contract;
4. `Research/Questions.md` for questions, defaults, answers, and closures;
5. `Research/Status.md` for the compact current state;
6. current methods, code, data records, and outputs for what was actually done;
7. `Research/References.md` for source, data, software, and material provenance.

Historical plans and chats explain how the work developed. They do not override
the active contract and its visible change record.

## Session entry for research work

After the universal startup in `AgentPrompt.md`, read:

1. `Research/Status.md`;
2. `Research/Research Contract.md`;
3. the latest relevant entries in `Research/Changes.md`;
4. open events in `Research/Questions.md` that affect the selected work;
5. only the methods, outputs, sources, chats, and playbooks needed for the work
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
decision. When the seed does not provide materials, search for fit-for-purpose
public datasets, software, models, tools, and other accessible resources before
concluding they are unavailable. Verify provenance, version, license, consent,
security, compatibility, and practical cost before depending on them.

When the field supplies no adequate method, state what is new, why it is needed,
which established or cross-field ideas it builds on, and how the properties
needed for the claim will be tested. Novelty is not evidence of correctness.

### Make the intended claim visible before results can reshape it

Activate the Research Contract before examining evidence designated there as
confirmatory or held out. The contract states the question, intended claim,
inputs, methods, strongest relevant comparisons, evaluation, and what would
count as success, failure, inconclusive, non-transfer, blocked by unavailable
evidence, or blocked by unavailable authority.

Exploratory work may precede activation when it is clearly labelled and cannot
silently become confirmatory evidence.

### Protect evidence roles

Classify important evidence as exploratory, development, confirmatory, held
out, or external validation. Record access and exclusion rules where knowledge
of the evidence could influence a choice. Reused development evidence is not
held out.

Use mechanical protections when the claim needs them: fixed splits, immutable
manifests, seeded procedures, append-only records, or executable checks. Match
the protection to the actual risk.

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

These stages describe the work and may overlap when evidence roles remain clear.

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
analysis ends. Work moves forward when its necessary state is usable.

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

## Human authority

Agents own routine research, design, implementation, analysis, documentation,
and local validation within the seed's purpose and the active contract.

The researcher is required for:

- identity, credentials, consent, or access that belongs to a person;
- spending, purchases, contracts, or paid accounts;
- contact with external people or organizations;
- publication, public release, or changes to public systems;
- destructive or irreversible external actions;
- a material change to the seed's purpose.

An unanswered authority question does not authorize its action. Record the
default and its effect in `Research/Questions.md`.

## Keeping the researcher informed

`Research/Status.md` is the compact current-state surface. Its next-action field
names the project's next useful action; each agent's continuity summary names
that agent's next resumable action. Update Status when the question changes, a
consequential change is adopted, a major result or blocker appears, a required
output becomes usable, or the project concludes. Do not turn it into a session
journal.

`Research/Status.md` also reports the number of open questions and points to
`Research/Questions.md`. The register preserves defaults and the effects of any
answers; focused chats carry the conversation. Final outputs carry the durable
result.

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

If unavailable evidence or authority prevents a promised output, the final
result record replaces any pretense of completion with the unavailable
prerequisite, the output it prevented, the bounded work completed, and the
condition under which a successor could resume.

## Completion

The project is complete when:

- the active Research Contract is coherent and its consequential changes are
  visible;
- the question is answered as success, failure, inconclusive, non-transfer, or
  explicitly blocked by unavailable evidence or unavailable authority;
- the outputs promised in the contract exist and agree with one another, or a
  terminal blocked record accounts explicitly for each prevented output;
- important baselines, controls, exclusions, deviations, and limitations are
  reported;
- the promised reproduction or verification path works to the degree claimed;
- every unanswered question has an explicit default, and its effect is reflected
  in the contract, changes, or final result as appropriate;
- `Research/Status.md` records the terminal state and useful next guidance;
- no unresolved template placeholder remains in a project-authored output;
- relevant tool and project checks pass.

Researcher answers are not a completion condition. The project finishes on the
strongest honest result available within the seed's purpose and its declared
constraints.
