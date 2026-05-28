---
type: prompt-module
module_type: output_format
domain: iso-management-system
standards:
  - "[[ISO 9001|ISO 9001:2015]]"
  - "[[ISO 14001|ISO 14001:2015]]"
scope:
  - internal-audit
  - management-system
tags:
  - prompt-library
  - iso/9001
  - iso/14001
  - ims
  - prompt/output
  - internal-audit
status: testing
version: 0.5
created: 2026-05-11
updated: 2026-05-25
related:
  - "[[Master]]"
  - "[[Build internal audit plan (ISO 9001)]]"
---

# Output format: Internal audit plan

Use this structure for the final audit plan.

The final output shall be a completed auditee-facing audit plan, not a template, checklist, working paper, audit report, or review commentary.

The output shall contain only the audit plan.

```markdown
# Audit plan – [Function / process / area name]

## Note to auditee

This audit plan is written using ISO terminology and structure because it forms part of [company / organisation]’s internal audit records.

During the audit itself, the discussion will focus on practical ways of working, responsibilities, evidence, follow-up and improvement, rather than on ISO clauses or terminology. No prior knowledge of the relevant ISO standard(s) is required to participate in the audit.

## Audit objective

[1 short paragraph, or maximum 2 short paragraphs if needed.]

## Audit scope

The audit includes:

- [Scope item]
- [Scope item]

### Out of scope

[Optional. Include only if needed to avoid likely misunderstanding.]

- [Out-of-scope item]

## Audit criteria

- [Relevant ISO standard(s): short selected clause list]
- [Applicable internal requirements, if provided]
- [Relevant governance, assignment, process, operational control, or management system documentation, if provided]
- [Relevant previous audit findings or follow-up actions, if provided]

## Audit approach and sampling

- [High-level method item]
- [High-level method item]

**Sampling boundary:**  

[Short statement defining the planned sample.]

**Core evidence expected:**  
- [Core evidence type]
- [Core evidence type]

## Audit setup

**Auditees:**

- [Auditee role / function]
- [Auditee role / function]

**Additional stakeholders may include:**

[Optional. Include only if supported.]

- [Stakeholder role / function]

**Duration:** [Requested duration, or `[1.5 hour]` if no duration was specified]

**Audit type:** Internal audit within [audit cycle / programme]

## Expected outputs

- Audit conclusion for the requested audit scope.
- Identified nonconformities, if any.
- Opportunities for improvement, if any.
- Input to management review and future audit planning, where relevant.

## Relevant background

[Optional. Include only where background helps auditees understand the audit focus.]

- [Relevant source-based background item]
- [Relevant source-based background item]

---
  
```

## Filling rules

Replace all bracketed text with completed content.

Do not leave placeholders in the final audit plan unless the user explicitly requests a reusable template.

Keep the structure as shown unless an optional section is not supported or not needed.

Optional sections may be omitted when not supported:

- `Out of scope`
- `Additional stakeholders may include`
- `Relevant background`

Do not preserve optional headings when there is no supported content.

Keep the expected outputs section in standard wording unless the user explicitly requests a different output structure.

Do not add sections, review comments, caveats, citations, source file names, drafting notes, or explanations unless explicitly requested.

---
