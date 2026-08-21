# Design Rationale

## Design rule

> Add scaffolding when it protects a real boundary or fixes a measured failure.
> Otherwise, trust the team.

Collaboration Station Research 2.0 keeps the scientific disciplines that made
earlier projects credible while removing the assumption that capable agents
must supervise and certify one another.

## What was retained

### A pre-result research contract

Earlier Claim Sheets made clean negative and inconclusive results possible by
declaring the question, strongest controls, evaluation, and outcome boundaries
before results were known. The new Research Contract preserves that function in
a smaller form. It also makes evidence roles explicit so exploratory,
development, confirmatory, held-out, and external-validation evidence cannot be
quietly conflated.

### Source-grounded method choices

Methods, datasets, controls, baselines, metrics, and interpretation begin with
credible sources and current field practice. A shared provenance ledger keeps
the reason for using a source beside its citation while that reason is fresh.

### Visible consequential changes

Research changes direction for legitimate reasons. `Research/Changes.md`
preserves what was learned, why the previous path no longer fit, what changed,
what stayed fixed, and how the result boundary moved. The protection is dated
visibility, not agent consensus.

### Strong controls, honest exclusions, and real negative outcomes

The new template retains the requirements to use the strongest relevant
comparisons, test shortcuts and confounds, report exclusions and deviations,
and ship failure, inconclusive, or non-transfer outcomes without rescue by an
exploratory side finding.

### Proportionate inspectability

Each contract names a practical way to inspect the load-bearing evidence.
Runnable reproducibility packets remain appropriate for computational claims,
but the mechanism may instead be a simulation, test harness, worked example,
manifest, visual comparison, or another artifact suited to the project.

### Proportionate ambition with a feasible rung

The template does not equate rigor with maximum scale. Established science is
used when it fits. Genuine method gaps receive a bounded creative attempt,
including cross-field transfer or a new approach with a higher validation
burden. If that attempt cannot support the ideal study within declared
constraints, the project completes the closest relevant rung instead of either
drifting to an unrelated easy question or declaring that no research is
possible.

When the seed supplies no inputs, agents explicitly search for suitable public
datasets, software, models, tools, and other online resources. Fit, provenance,
license, consent, compatibility, security, and practical resource cost remain
part of the research decision rather than an afterthought.

### Mechanical coordination

The Collaboration Station 2.0 chat, work-claim, and path-scoped closeout tools
are inherited as universal mechanics. Closeout now treats a repository with no
remote as an explicit local-only mode, while refusing to guess when a remote
exists but the current branch has no upstream. These tools solve shared-state
problems without judging research quality.

## What was transformed

### Fifteen-slot Claim Sheet → compact Research Contract

The former contract mixed general research commitments with project-specific
company policy and artifact choices. The new contract concentrates on hard-to-
answer-vaguely commitments: question, bounded claim, outcome map, evidence
roles, methods and alternatives, evaluation, stopping rules, authority, and
required outputs.

The plain-language companion is no longer a second synchronized document. The
contract is expected to be readable, while `Research/Status.md` gives the human
director a compact current view.

### Four gated phases → descriptive research arc

Framing, contracting, execution, and conclusion remain useful orientation. They
do not require signatures or agreement to advance. The only hard transition is
epistemic: evidence declared confirmatory or held out is not examined until the
relevant boundaries are active.

### Fixed artifact bundle → reader-driven outputs

Technical reports, accessible pieces, study guides, live-run READMEs, and full
reproducibility packets can all be valuable. They are selected when a named
reader or claim needs them. Every project still leaves a final result, methods
and evidence record, provenance, limitations and exclusions, and an inspectable
verification path; those needs may be combined into fewer artifacts.

### Cadenced progress reports → material-event status

`Research/Status.md` changes when the question, contract, evidence, blocker,
output, or terminal state materially changes. Session summaries retain detailed
chronology. This informs the director without manufacturing reports because a
session counter fired.

### Researcher availability → questions with defaults

`Research/Questions.md` separates advice from authority. An advisory question
records the defensible default already in force. An authority question defaults
to not taking the restricted action. Answers and closures are appended as dated
events under stable IDs, so an absent researcher never becomes a project-wide
wait state and silence never becomes permission. A terminal
`blocked by unavailable authority` result accounts honestly for any promised
action or output the agents could not perform.

### Cross-model review → focused contribution

Different model families still contribute useful independent information. A
focused contribution is one-directional: one bounded question, one set of
improvements or one independent result, then the responsible agent incorporates
what helps and continues. Later use may expose problems, which are corrected
forward.

## What was removed

- fixed writer and reviewer roles;
- mandatory cross-review in every session;
- Review Cards and exact candidate authentication for ordinary artifacts;
- repeated owner-reviewer rounds and successor review cards;
- same-state AI approval and dual signatures;
- consensus-dependent phase closure and project completion;
- review disagreements routed to the human director;
- a second accessible contract that had to stay synchronized;
- project-wide company identity and monetization requirements;
- mandatory artifacts without a named reader or claim boundary.

These mechanisms were not removed because another perspective lacks value.
They were removed because the histories showed that approval machinery could
grow faster than the research and because current models already perform
substantial self-correction and verification.

## Evidence from prior projects

The earlier EEG projects demonstrate the value of a visible contract without
formal Review Cards. One project preserved a primary success alongside an
inconclusive transfer result; another shipped a clean negative because its best
model achieved only `+0.023` against a predeclared `+0.075` bar and failed a
robustness condition. In both, the contract, controls, amendments, and
reproduction path did the epistemic work.

The later Robot Structural Proprioception and Hybrid Ground Truth Realism
projects show both sides of cross-family challenge. Independent passes caught
real errors, including a wrong operating point, an uncertainty calculation, a
units mismatch, and integrity checks that did not protect the bytes actually
used. They also accumulated large review cards, per-round probes, successor
reviews, and long process discussions while core measurement remained pending.

The transferable lesson is purpose-first evaluation: state what an artifact is
for, try to break the properties that matter, and examine the whole artifact
against its purpose rather than merely comparing it with the previous draft.
That principle is retained without approval semantics.

## Fit with current model guidance

OpenAI's [model guidance](https://developers.openai.com/api/docs/guides/latest-model)
recommends lean prompts, one statement of each instruction, explicit autonomy
and approval boundaries, and representative testing of inherited settings.
OpenAI's [GPT-5.6 overview](https://openai.com/index/gpt-5-6/) describes stronger
long-horizon research, browsing, tool use, and self-directed work.

Anthropic's [Claude Opus 5 prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
says the model verifies and self-corrects without repeated instructions and
warns that legacy verification scaffolding can cause over-verification.
Anthropic's [model-selection guidance](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
positions current frontier models for deep reasoning, advanced research, and
long-horizon agentic work. Its [effort guidance](https://platform.claude.com/docs/en/build-with-claude/effort)
recommends re-evaluating settings inherited from earlier models on current
workloads.

The resulting design does not assume agents are infallible. It moves assurance
to the objects that can actually bear it: predeclared outcome boundaries,
evidence separation, strong controls, source provenance, adversarial tests,
visible changes, and runnable verification.

## Guidance for future additions

Before adding a required document, gate, role, or check, answer:

1. Which concrete research or shared-state failure does it prevent?
2. Is that failure already handled by the universal scaffold or current model
   behavior?
3. Can a mechanical invariant, executable check, or field in an existing
   artifact protect it more directly?
4. Does the addition create an approval dependency or a successor loop?
5. Has the failure recurred often enough to justify context paid by every
   future project?

Prefer the smallest intervention whose benefit can be observed. Remove it when
the measured failure disappears or the platform solves it elsewhere.
