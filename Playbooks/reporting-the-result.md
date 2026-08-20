# Reporting the Result

Read this when producing the outputs the Research Contract promised.

## The final result record

Every project leaves one artifact that answers the research question. It states
which outcome occurred — success, failure, inconclusive, non-transfer, or
blocked by unavailable evidence — and carries the methods, comparisons,
exclusions, deviations, and limitations needed to understand that answer.

Small projects can satisfy this with a single report. Larger ones may separate
it into a technical account, a public explanation, and supporting records. The
contract decides the output set; the reader can judge whether it serves its
purpose.

## Writing at true strength

Match the verb to the evidence. *Consistent with*, *shows*, and *demonstrates*
are three different claims, and a reader in the field will notice which one the
result supports.

Every claim in the report should be traceable to a specific result, and every
load-bearing number should exist somewhere a reader can check it. If a sentence
cannot be traced, it is an impression — either support it or cut it.

The headline must stay inside the outcome map. When the result sits near a
boundary, say where it sits rather than choosing the flattering side.

Limitations are the ones that could change the conclusion. A limitations section
listing only harmless caveats is a way of appearing candid while hiding the
thing that matters.

## Negative and inconclusive results

These are complete results, and they are frequently the more useful ones.

What makes a negative result valuable is its **detection floor**: what was
tested, at what strength, and what size of effect the design would have found.
*No effect was observed* is nearly useless. *No effect above X was observed with
a design sensitive to X under these conditions* is a real contribution and
protects the next investigator from repeating it.

An inconclusive result should state precisely what prevented resolution and what
a successor would need — more data, more capacity, a different measurement, a
different question.

Do not rescue a result by relaxing the outcome map after seeing it. If a
boundary genuinely needs to move, it moves through a dated entry in
`Research/Changes.md`, where a reader can see when it moved and what was known.

## The reproduction or verification path

Scale it to the claim. The requirement is that an outside reader can inspect the
load-bearing evidence, not that every project ship the largest possible packet.

Depending on the claim, that path may be a runnable packet, a test harness, a
notebook, a simulation, a worked example, a dataset manifest, a visual
comparison, or a runbook.

Whatever the form, it must actually run from a clean start, and it must
reproduce the numbers the conclusion depends on. Where it cannot cover something
— private data, hardware, cost, runtime — say so explicitly and describe what
would be needed. An untested packet is a claim about reproducibility rather than
evidence of it.

## Optional outputs, and when each earns its place

- **Public explanation** — when a non-specialist audience exists. It carries the
  same outcome as the technical account, in plain language, without upgrading
  the claim.
- **Orientation guide** — when someone must judge whether to trust the work
  without reading the code: what the project asked, why the design answers it,
  and how a reader can tell whether the result holds.
- **Dataset, model, or method card** — when the artifact will be reused by
  others and its terms and limits travel with it.
- **Dashboard, simulation, or live view** — when the evidence is easier to
  inspect interactively than to describe.

Do not produce an output because a previous project had one.

## Before the outputs are finished

The outputs must agree with each other and with the contract. When they
disagree, the evidence decides and everything else is updated to match.

No template placeholder should remain in anything a reader receives.
