# Grounding the Seed

Read this when turning the seed idea into a bounded, answerable investigation.

**Input:** the free-form seed in `Project Details/Project Details.md`, plus any
resources it names.

**Output:** enough grounding to draft `Research/Research Contract.md`, and the
sources that informed it recorded in `Research/References.md`.

## What grounding has to produce

Before a contract can be written, the project needs defensible answers to:

- how this kind of question is currently investigated in the field;
- what the strongest relevant baseline or alternative is, and why it is strong;
- which metrics and reporting conventions the field uses, and whether they fit
  this question;
- the known confounds, shortcuts, and failure modes for this kind of work;
- what materials or data exist, on what terms, and in what condition;
- which public datasets, software, models, tools, and other online resources can
  supply missing inputs within the project's constraints;
- and what has already been answered, so the project does not re-derive it.

If you cannot state the strongest baseline and why it is strong, or name the
most likely confound, grounding is not finished. Keep reading rather than
starting to build.

## Using sources honestly

Verify a link or DOI when you add it. Do not reconstruct citations from memory
at the end of a project; they will be wrong, and the record is what an outside
reader uses to check the reasoning.

Record a source when it changes a decision, and record which decision it
changed. A reference that informed nothing is bibliography, not evidence.

Ground the choices you did not make as well as the one you did. Reading only
about the method you already prefer produces a well-cited version of an
unexamined assumption.

## Find usable resources, not only papers

When the seed supplies no dataset, implementation, model, software, or tool,
search for suitable public resources before treating the input as unavailable.
Inspect registries, repositories, archives, benchmark sites, and authoritative
project pages appropriate to the field.

Availability is not suitability. Before relying on a resource, verify:

- what version or snapshot is actually accessible;
- license, consent, privacy, and permitted-use boundaries;
- provenance, documentation, known quality problems, and population fit;
- file format, dependencies, hardware, runtime, storage, and monetary cost;
- whether the project can preserve a manifest, checksum, environment, or other
  record sufficient to identify what was used.

Prefer an established fit-for-purpose resource over building a new one when it
answers the same question. Build or adapt only when the gap matters to the
claim.

## Finding the answerable rung

Seeds arrive at every size. The common gaps are that the question is not
answerable with available evidence, the material does not exist or cannot be
used, or the seed describes an interest rather than a question.

Useful moves:

- narrow the population, condition, regime, or scale until the question can be
  answered with evidence that exists;
- substitute the closest usable material and state the boundary that creates;
- split an ambitious question into a first rung that is answerable now and name
  what the later rungs would require;
- convert an open-ended interest into the specific decision or understanding an
  answer would support.

Preserve the seed's purpose. Do not stop at “no research project can be done,”
and do not swap in an unrelated easy question. Choose the most informative rung
that is feasible under the project's compute, time, money, materials, access,
safety, legal, and ethical constraints. A useful rung may be a feasibility
study, data audit, benchmark, simulation, theoretical analysis, method
prototype, experimental design, or proof of a current limit. Record why the
ideal rung was unavailable and what would make it possible later.

## When the field has no adequate method

Sometimes the honest finding of grounding is that no established method fits.
Use this order:

1. confirm that established methods in the primary field do not fit;
2. inspect adjacent fields for an analogous problem and a method that can
   transfer with stated assumptions;
3. combine or adapt established components where their interaction can be
   tested;
4. make a bounded attempt at a new solution when the remaining gap matters;
5. if the attempt does not establish what the claim needs, step down to the
   closest relevant feasible rung rather than extending the search indefinitely.

State what is new, why existing methods do not answer the question, what
cross-field ideas were considered, and how the new approach will be tested
against strong alternatives, controls, and known cases. A novel method may be
exploratory before it is validated, but it cannot carry a stronger claim merely
because it is plausible. The Research Contract sets the effort ceiling and
fallback before results make either convenient.

## When a second reading of the field helps

Two participants searching the same literature independently sometimes return
materially different pictures: a baseline one missed, a contradicting result, a
metric the field has moved away from. That difference is information.

Ask for an independent reading when the field is unfamiliar, contested, or when
a method choice will be expensive to reverse. It is not a routine step for every
topic, and matching readings prove less than they appear to.

## Failure modes

- Citing from memory, then verifying at the end.
- Treating a single survey or a single lab's output as the field.
- Grounding the chosen method and nothing it competes with.
- Accepting a dataset without checking license, consent, version, or condition.
- Treating the absence of a supplied dataset or implementation as evidence that
  no usable public resource exists.
- Inventing a new method before checking established and transferable ones.
- Extending a creative search until something appears to work, without a
  stopping rule or relevant fallback rung.
- Sharpening the question so far that it is answerable but no longer worth
  answering.
