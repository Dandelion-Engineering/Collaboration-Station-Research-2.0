# Writing the Research Contract

Read this when building or sharpening `Research/Research Contract.md`.

The contract's job is to make the question, the evidence, and the outcome
boundaries visible before results can reshape them. Its protective power comes
entirely from commitments that are hard to satisfy vaguely.

## The test for every commitment

> Could a reasonable person holding only this contract and the final results
> disagree about which outcome occurred?

If yes, the commitment is not sharp enough yet. Apply the test slot by slot.

## Slot craft

**Question.** One question, answerable with the evidence the project can
actually obtain. Words like *explore*, *investigate*, or *look at whether X is
promising* usually mean the question has not been chosen yet. A conjunction
often hides two questions; pick the one this project answers.

**Intended claim.** Write the sentence you hope to be able to say at the end,
then delete every word the achievable evidence would not support. What remains
is the claim. If it is not falsifiable at this project's scale, it is a research
programme, not a claim.

**Claim boundary.** Name the stronger statement readers will extend your result
to, and disclaim it here rather than in a limitations section nobody reaches.

**Outcome map.** Success, failure, inconclusive, non-transfer, blocked by
unavailable evidence, and blocked by unavailable authority need observable
conditions.

- Weak: *the method performs meaningfully better than baseline.*
- Strong: *a paired improvement of at least X on metric M across all N held-out
  units, with the interval excluding zero, and holding under the pre-declared
  robustness check.*

Two properties matter more than precision. Failure must be **reachable** — if no
plausible result would count as failure, this is not a contract. And a
robustness clause should exist, so a single fortunate split cannot carry
success on its own.

**Inconclusive** is the guard against calling an underpowered null a clean
negative. Declare in advance what would make a null uninformative: sample size,
model capacity, tuning budget, measurement floor, or coverage. Without that
line, every negative result invites the argument that the attempt was too small.

**Blocked** outcomes identify a missing prerequisite, not a vague difficulty.
Unavailable evidence means the question could not be resolved after the
declared proportionate search or attempt. Unavailable authority means the work
requires a human-only action that was not authorized. In either case, name the
bounded work that can still be completed and what would allow resumption.

**Evidence roles.** State what makes held-out evidence held out, and when it
becomes accessible. Once evidence has been inspected or tuned against, it is
development evidence; relabelling it later does not restore it.

**Materials and online resources.** If the seed supplies no inputs, name the
public datasets, software, models, tools, repositories, or other resources the
project will use or evaluate. Record fit, access path, version, provenance,
license or consent, compatibility, and compute, storage, time, or cost limits.

**Methods and baselines.** The strongest relevant comparison available under the
project's constraints, not the most convenient one. A baseline that is easy to
beat usually indicates the comparison was chosen after the method.

State which parts of the approach are established, transferred from another
field, adapted, or new. A new method must have tests capable of showing that the
properties needed for the claim are actually correct.

**Controls.** For each, ask what could produce this result even if the effect is
not real — leakage, a shortcut feature, a confound, a trivial predictor,
selection — and name the check that would reveal it.

**Capacity and stopping rules.** These separate *no effect* from *not enough
attempt*, and they prevent an investigation from expanding until something
works. Bound the literature search, cross-field transfer search, prototyping,
tuning, and compute before results exist. Name the closest relevant feasible
rung the project will take if the ideal path cannot meet its burden.

**Researcher questions.** Every open question needs an entry in
`Research/Questions.md`. Advisory questions carry a live default. Authority
questions default to not taking the restricted action. A question that changes
a contract boundary also needs a dated `Research/Changes.md` entry.

**Outputs.** Every named output needs a reader, minimum content, and evidence of
completion. If no reader can be named, do not name the output.

## Activation

The contract becomes active when it is complete and coherent and the project is
ready to inspect evidence designated confirmatory or held out. Set the status,
the version, and the date.

Activation is a state transition in the research, not an approval event. The
agent leading the contract activates it. Focused input from another participant
may improve it first; nothing signs it.

Work done while the contract is a draft remains exploratory, and stays
exploratory unless it is repeated on evidence that has not been used.

## Keeping the contract clean

The contract states the current plan. Its history lives in `Research/Changes.md`.

When a consequential boundary moves, append the dated entry first, then update
the contract to the new clean state and link the entry. Do not edit an outcome
threshold in place — the dated trail is what makes the difference between an
honest correction and a quietly loosened bar visible to a reader.

## Failure modes

- Thresholds written after the first results are visible.
- Success conditions stated as adjectives.
- A failure condition no realistic result could meet.
- An outcome map that omits inconclusive.
- A blocked outcome that names no unavailable prerequisite or resumption path.
- Materials listed without roles, licenses, or access rules.
- A novel method whose correctness is assumed rather than tested.
- A creative search with no effort ceiling or relevant fallback rung.
- An open researcher question without an explicit default.
- Outputs copied from another project rather than derived from this claim.
