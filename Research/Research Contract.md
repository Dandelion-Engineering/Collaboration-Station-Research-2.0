# Research Contract

**Project:** `{{AGENT_DERIVED_PROJECT_TITLE}}`  
**Status:** Draft — not yet active  
**Contract version:** 0.1  
**Last updated:** `{{YYYY-MM-DD}}`  
**Related change entries:** None

This document is the clean current contract for the investigation. Agents build
it from the free-form seed in `Project Details/Project Details.md` and credible
sources. Complete it before examining evidence designated as confirmatory or
held out. Exploratory work performed while it is a draft remains exploratory.

## 1. Research question

### Question

`{{ONE_ANSWERABLE_QUESTION}}`

### Why it matters

`{{DECISION_UNDERSTANDING_OR_CAPABILITY_THIS_ANSWER_SUPPORTS}}`

### Intended claim

If the evidence supports it, the project expects to be able to say:

> `{{ONE_BOUNDED_DECLARATIVE_CLAIM}}`

### Claim boundary

This project will not claim:

- `{{IMPORTANT_NON_CLAIM}}`
- `{{IMPORTANT_NON_CLAIM}}`

## 2. Outcome map

Define these before confirmatory evidence is inspected. Use observable
conditions, not adjectives such as "good" or "meaningful" without a rule.

### Success

`{{PREDECLARED_SUCCESS_CONDITIONS}}`

### Failure or bounded negative

`{{PREDECLARED_FAILURE_CONDITIONS}}`

### Inconclusive

`{{CONDITIONS_THAT_PREVENT_A_CLEAN_YES_OR_NO}}`

### Non-transfer or scope-limited outcome

`{{CONDITIONS_UNDER_WHICH_THE_RESULT_DOES_NOT_GENERALIZE}}`

## 3. Materials and evidence roles

| Material or source | Role | Access or split rule | Eligibility and exclusions | License / consent / provenance |
|---|---|---|---|---|
| `{{DATASET_INPUT_SYSTEM_OR_CORPUS}}` | `{{exploratory OR development OR confirmatory OR held-out OR external-validation}}` | `{{RULE}}` | `{{RULE}}` | `{{DETAILS}}` |

Record when confirmatory or held-out evidence first becomes accessible if that
knowledge could shape methods or thresholds.

## 4. Methods, alternatives, and controls

### Primary approach

`{{METHOD_AND_WHY_IT_FITS_THE_QUESTION}}`

### Strongest relevant baselines or alternatives

- `{{BASELINE_AND_WHY_IT_IS_STRONG}}`
- `{{BASELINE_AND_WHY_IT_IS_STRONG}}`

### Controls and shortcut checks

- `{{CONTROL_OR_LEAKAGE_CHECK_AND_WHAT_IT_CAN_REVEAL}}`
- `{{CONTROL_OR_LEAKAGE_CHECK_AND_WHAT_IT_CAN_REVEAL}}`

### Capacity or escalation plan

`{{HOW_THE_INVESTIGATION_AVOIDS_CONFUSING_AN_UNDERSIZED_OR_UNDERPOWERED_ATTEMPT_WITH_A_SETTLED_NEGATIVE}}`

### Stopping rules

`{{WHEN_TO_STOP_SCALING_SEARCHING_OR_COLLECTING_AND_WHY}}`

## 5. Evaluation and interpretation

### Unit of analysis

`{{INDEPENDENT_UNIT_AND_SAMPLE_SIZE_LOGIC}}`

### Primary metrics or decision procedure

`{{METRICS_TESTS_THRESHOLDS_AND_UNCERTAINTY_INTERVALS}}`

### Robustness and sensitivity

`{{PERTURBATIONS_SUBGROUPS_ALTERNATIVE_SPECIFICATIONS_OR_LEAVE_ONE_OUT_CHECKS}}`

### Missing data, multiplicity, and deviations

`{{PREDECLARED_HANDLING_RULES}}`

### Interpretation rules

`{{HOW_RESULTS_MAP_TO_SUCCESS_FAILURE_INCONCLUSIVE_OR_NON_TRANSFER_WITHOUT_POST_HOC_PROMOTION}}`

## 6. Operational plan

### Work sequence

1. `{{READY_UNIT}}`
2. `{{READY_UNIT}}`
3. `{{READY_UNIT}}`

### Compute, time, and resource ceiling

`{{AVAILABLE_ENVIRONMENT_AND_LIMITS}}`

### Safety, privacy, legal, and human-only boundaries

`{{BOUNDARIES_AND_ANY_REQUIRED_HUMAN_ACTION}}`

## 7. Required outputs and inspectability

Name only outputs with a real reader or boundary to serve.

| Output | Reader and purpose | Minimum content | Completion evidence |
|---|---|---|---|
| Final result record | `{{READER}}` | Question, methods, results, limitations, conclusion | `{{EVIDENCE}}` |
| Reproduction or verification path | `{{READER}}` | `{{RUNBOOK_TEST_HARNESS_SIMULATION_WORKED_EXAMPLE_OR_OTHER}}` | `{{WHAT_WILL_BE_RUN_OR_CHECKED}}` |
| `{{OPTIONAL_OUTPUT}}` | `{{READER_AND_PURPOSE}}` | `{{MINIMUM_CONTENT}}` | `{{EVIDENCE}}` |

### Source and data provenance

`Research/References.md` records sources, datasets, licenses, and the decisions
they informed. Additional manifests or data cards required:

`{{ADDITIONAL_PROVENANCE_ARTIFACTS_OR_NONE}}`

### Exclusions, deviations, and limitations

These will be recorded in:

`{{OUTPUT_SECTION_OR_FILE}}`

## 8. Known uncertainty at activation

- `{{OPEN_UNCERTAINTY_THAT_DOES_NOT_PREVENT_STARTING}}`

## Activation checklist

- [ ] The question and intended claim are bounded.
- [ ] Success, failure, inconclusive, and non-transfer conditions are explicit.
- [ ] Important evidence has a declared role and access rule.
- [ ] Methods, strongest baselines, controls, metrics, and stopping rules are source-grounded.
- [ ] Exclusions, deviations, and uncertainty handling are specified.
- [ ] Required outputs and their readers are named.
- [ ] Human-only, safety, privacy, legal, compute, and budget boundaries are clear.
- [ ] Every `{{DOUBLE_BRACED_PLACEHOLDER}}` has been replaced.

When the checklist is satisfied, set **Status** to `Active`, set version `1.0`,
and record the activation date. Activation is a research-state transition, not
an AI approval event.
