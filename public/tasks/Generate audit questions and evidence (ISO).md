---
type: prompt-module
module_type: task
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
  - prompt/task
status: draft
version: 0.1
created: 2026-05-25
updated: 2026-05-25
related: []
---

# Task: Build audit questions and evidence list

Create a concise auditor-facing cheat-sheet for the requested internal audit.

## Mandatory input check

Before generating, check that the input includes an audit plan or equivalent document defining at minimum the audit area and scope, and preferably criteria and duration.

If no such input is provided, stop and state what is missing.

If the input is incomplete but still usable, proceed and state the limitation briefly.

## Core task

Create only two things:

- key audit questions;
    
- key evidence to request.
    

Use the provided audit plan or equivalent input as the boundary. Do not expand the audit beyond the provided scope and criteria.

Do not create an audit plan, audit report, findings, recommendations, review comments, weak-evidence risks, or reusable template unless explicitly requested.

## Criteria and clause linkage

Use ISO clauses only when they are mentioned in the input.

Do not add new ISO clauses unless explicitly requested.

Where ISO clauses are provided, show them briefly in question-theme headings where useful, for example `– 5.3` or `– 6.2 / 9.1`.

## Questions

Start with one opening context question, normally along the line of:

- “Tell me about your business/function/process and how it contributes to the management system.”
    

Then organise the remaining questions by audit scope point, clause point, or practical theme.

For a 1.5 hour audit, normally use 2–3 question themes.

Merge overlapping scope points into one practical theme where this improves audit flow.

Where the input defines a sampling boundary, anchor most must-ask questions to that sample. Prefer wording such as “In the selected cycle/example…” over broad general questions.

For each theme, include:

- 1–3 must-ask questions;
    
- a few optional supporting probes where useful.
    

Must-ask questions shall be short, direct, and focused on the most important implementation or evidence point within the audit scope.

Optional probes shall help continue or deepen the discussion where useful.

Prefer fewer, higher-yield questions over comprehensive coverage.

Prefer one clear question per bullet.

Avoid long multi-part questions, exhaustive checklist behaviour, yes/no questioning, and clause-by-clause decomposition.

## Evidence

Create one consolidated evidence request list for the audit.

Include 2–4 key evidence requests only.

Reserve the first evidence request for assignment, mandate, role, or responsibility evidence where relevant.

Use generic wording unless the input names the actual document.

Include only evidence the auditor should intentionally request before or during the audit.

Do not list every possible supporting artefact, screenshot, photo, system view, or incidental record that may appear during the audit.

Do not create separate evidence lists for every question unless this is clearly more useful.

## Sampling

Include a short bounded sampling focus if useful.

Use examples such as one recent cycle, one selected forum, one or two examples, current audit-period records, or evidence linked to known risks or previous findings.

Do not suggest reviewing everything unless the scope is explicitly very narrow.

## Boundaries

Do not invent company-specific documents, systems, roles, forums, records, risks, or responsibilities not supported by the input.

If source material is limited but the audit area is clear, use generic but relevant wording.

The final output must remain a practical cheat-sheet, not a judgement or review document.

---
