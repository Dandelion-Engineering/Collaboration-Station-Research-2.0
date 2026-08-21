# Researcher Questions

This append-only register lets agents ask the researcher questions without
turning the project into a wait state. The researcher is the human director
named in `AgentPrompt.md`.

Each question has a stable sequential ID. Never edit or delete an opening or
earlier event. Append an answer, closure, or correction event under the same ID.
The latest event determines whether the question is open.

## Operating rules

- An **advisory** question records the defensible default already in force. Work
  continues under that default unless an answer changes it.
- An **authority** question always defaults to **do not take the restricted
  action**. Continue around the blocked action, narrow the result honestly, or
  finish with a bounded `blocked by unavailable authority` outcome.
- Link a focused human chat when conversation would help. Record the durable
  answer or decision here when it arrives.
- If a default or answer moves the question, claim, evidence role, method family,
  primary evaluation, success boundary, stopping rule, or required output, also
  append a dated entry to `Research/Changes.md`.
- Unanswered questions may remain open at completion. Their defaults and effects
  must be explicit in the contract, status, changes, or final result.

`Research/Status.md` reports the current open count and points here. Before a
completed-project shortcut, inspect this register for any newly appended
researcher direction.

## Question opening template

### `Q-{{NNNN}}` — Opened `{{YYYY-MM-DD}}`

- **Type:** `{{advisory OR authority}}`
- **Question:** `{{ONE_SENTENCE_A_NON_SPECIALIST_CAN_ANSWER}}`
- **Why it matters:** `{{DECISION_OUTPUT_OR_BOUNDARY_AFFECTED}}`
- **Default now in force:** `{{DEFENSIBLE_DEFAULT_OR_DO_NOT_TAKE_THE_ACTION}}`
- **A different answer would change:** `{{SPECIFIC_EFFECT}}`
- **Linked chat or change entry:** `{{PATH_OR_NONE}}`

---

## Answer event template

### `Q-{{NNNN}}` — Answered `{{YYYY-MM-DD}}`

- **Answer:** `{{RESEARCHER_ANSWER}}`
- **Source:** `{{CHAT_PATH_DIRECT_ENTRY_OR_OTHER_PROVENANCE}}`
- **Effect on current work:** `{{WHAT_CHANGES_OR_WHY_THE_DEFAULT_STILL_STANDS}}`
- **Linked change entry:** `{{PATH_AND_HEADING_OR_NONE}}`

---

## Closure event template

### `Q-{{NNNN}}` — Closed `{{YYYY-MM-DD}}`

- **Resolution:** `{{ANSWER_APPLIED OR DEFAULT_STOOD OR ACTION_REMAINS_UNAUTHORIZED}}`
- **Effect reflected in:** `{{CONTRACT_STATUS_CHANGE_OR_FINAL_RESULT_PATH}}`

---

Keep these templates as instructions and append real events below them. Template
IDs are placeholders, not events. Use `Q-0001`, then the next unused sequential
ID, for each new question.
