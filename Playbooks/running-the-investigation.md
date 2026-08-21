# Running the Investigation

Read this while building, measuring, analyzing, and interpreting — the stretch
between an active contract and a stated result.

## Keep evidence roles intact

The roles declared in the contract only protect anything if they survive
contact with the work. In practice that means tuning, thresholding, feature
selection, prompt iteration, and architecture search happen on development
evidence, and confirmatory or held-out evidence is inspected once the choices
it will judge are fixed.

Record when protected evidence first becomes accessible if that knowledge could
influence a later choice.

## Hold new methods to their declared burden

When the contract relies on a transferred, adapted, or new method, test the
properties the claim needs before treating its outputs as evidence. Use known
cases, strong established alternatives, ablations, invariants, simulations, or
other controls capable of exposing a plausible but wrong solution.

If the method does not meet that burden within the declared effort and resource
ceiling, take the contract's closest relevant feasible rung. Record any moved
research boundary in `Research/Changes.md`; do not extend search or tuning until
something appears to work.

## A failed validation is a stop-or-go point

When a check that was supposed to pass does not, diagnose it before continuing.
A known-bad input pushed downstream contaminates everything built on it, and the
cost of the diagnosis only grows.

This is not a gate that anyone else opens. It is a decision the responsible
agent makes with the evidence in front of it, and records.

## Record exclusions and deviations as they happen

Every material excluded sample, dropped run, protocol deviation, and abandoned
analysis gets a reason and a count, written where a reader of the result will
find it. Silent exclusion is a reproducibility failure regardless of intent, and
exclusions are much harder to reconstruct honestly a month later.

Label exploratory findings as exploratory in the artifact that reports them. An
exploratory finding may become the headline claim only through a dated entry in
`Research/Changes.md`, and it remains exploratory until it is retested on
evidence that has not already been used.

## Build the reproduction path as you go

This is the commitment that fails silently when deferred. Reconstructing an
environment, a seed, or the exact command behind a number at the end of a
project is where reproducibility is usually lost.

The cheap running test: **could someone re-run the number you just wrote down,
using only what is committed?**

Keeping that true costs very little during the work:

- record the environment and pin dependency versions;
- set seeds and record them alongside results;
- keep a manifest or checksum for the data as used, including its version;
- expose parameters as arguments rather than editing values in place;
- avoid absolute paths tied to one machine;
- keep each reported number, table, and figure regenerable by a command.

## Correcting course

Consequential changes — the question, the claim, an evidence role, an
eligibility rule, the method family, the strongest baseline, the primary metric,
a success boundary, a stopping rule, a required output — go in
`Research/Changes.md` before the new path is treated as active. Everything else
is ordinary implementation and belongs with the work it affects.

Write the entry when the change is made, not in a batch at the end. The entry's
value is that it records what was known at the time.

## Correcting earlier work

When your work reveals a defect in something already finished — yours or
another participant's — fix it in the current state and carry the correction
into anything downstream. If it moves a research boundary, record it.

Corrections propagate forward. You do not need permission from whoever produced
the earlier work, and finished work is not reopened merely because another look
might find something.

## Failure modes

- Tuning against evidence the contract reserved.
- Adding a metric or subgroup after seeing results without labelling it as
  post-hoc.
- Re-running until a split cooperates, then reporting the cooperative one.
- Treating a pipeline failure as noise and continuing.
- Deferring the data manifest, the seeds, or the environment record.
- Letting the reported number drift away from the command that produced it.
