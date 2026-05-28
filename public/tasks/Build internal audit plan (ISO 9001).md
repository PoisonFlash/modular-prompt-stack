---
type: prompt-module
module_type: task
domain: iso-management-system
standards:
  - "[[ISO 9001|ISO 9001:2015]]"
scope:
  - internal-audit
  - management-system
tags:
  - prompt-library
  - iso/9001
  - prompt/task
status: testing
version: 0.4
created: 2026-05-11
updated: 2026-05-20
related: []
---

# Task: Build internal audit plan (ISO 9001)

Create a concise internal audit plan for ISO 9001:2015.

The audit plan shall be suitable to share with auditees before the audit. It shall explain the objective, scope, criteria, method, sampling, setup, expected outputs, and relevant background in clear, practical language.

Build the audit plan only for the area requested by the user.

## Core task

Create a completed auditee-facing audit plan.

The plan shall be:
- specific to the requested function, process, governance area, topic, or management system area;
- proportionate to the requested or assumed duration;
- focused on how the requested area contributes to the organisation’s Quality Management System;
- selective in ISO 9001 criteria;
- clear about sampling and core evidence;
- brief enough to be useful before the audit.

Do not create an audit checklist, auditor working paper, audit report, review commentary, finding, recommendation, or template unless explicitly requested.

## Audit area logic

First interpret the requested audit area.

If the requested area is an individual business function, team, department, capability, support area, or operational area, treat it as one contributor to the organisation’s QMS.

Do not treat an individual function as if it were the whole QMS.

For function-level audits, focus on how the function:
- understands its role in the QMS;
- manages relevant responsibilities, interfaces, inputs and outputs;
- applies relevant QMS requirements in normal work;
- provides or retains evidence of implementation;
- monitors, follows up, escalates or improves quality-relevant work where applicable;
- contributes to the effectiveness of the wider organisational QMS.

Only create a full QMS audit plan if the user explicitly requests an audit of the full QMS, management system, or overall QMS governance.

## Duration and scale

Scale the plan to the requested duration.

If the user does not specify a duration, assume 1.5 hours.

When the duration is assumed:
- scale the plan to 1.5 hours;
- show the duration in the final output as `[1.5 hour]`;
- do not omit the duration field.

The scope, sampling, auditees, stakeholders, criteria and evidence expectations must be realistic for the available time.

If the requested scope is broad and the duration is short, narrow the plan through sampling. Do not expand the session.

For audits of 2 hours or less:
- define a clear sampling boundary;
- use maximum 3–4 scope bullets;
- use maximum 3 approach bullets;
- use maximum 3 core evidence bullets;
- use normally 1–3 auditee roles;
- use normally 3–5 ISO 9001 clause references.

## Scope and boundaries

Use only the audit scope requested by the user and the provided source material.

Scope items shall describe the areas, responsibilities, interfaces, activities, controls, or evidence domains included in the audit.

Keep the scope focused. Do not turn it into detailed audit steps or questions.

Use an “Out of scope” section only where a boundary is needed to prevent likely misunderstanding.

Do not list other standards, management systems, functions, processes, or topics as out of scope merely because they are not part of the audit.

## Criteria

Select ISO 9001:2015 criteria narrowly and deliberately.

Use ISO 9001 reference material as a criteria menu only.

Include only clauses directly relevant to the requested audit scope.

Do not include clauses merely because they are generally relevant to QMS.

Prefer top-level or clause-family references where this gives a cleaner auditee-facing plan, for example `Clause 5.1 Leadership and commitment`.

A long ISO clause list is a quality problem unless the user explicitly asks for broad audit coverage.

Include internal requirements, governance documents, previous findings, audit programme priorities, or management review inputs only when they are provided and directly relevant to the requested audit scope.

## Audit approach and sampling

Write the audit approach as a brief auditee-oriented method description.

Use terms such as interview, walkthrough, selected evidence review, sampling, document review, process demonstration, or review of retained records where relevant.

Do not write detailed audit steps, audit questions, checks, challenges, or instructions to the auditor.

Define the sampling boundary clearly.

Use bounded sampling language such as:
- one recent cycle;
- one selected process or governance forum;
- one or two recent examples;
- selected records from the current audit period;
- selected evidence linked to a previous finding.

Avoid open-ended wording such as “review all relevant records”, “review governance”, or “sample inputs and outputs” without a boundary.

## Evidence

Identify only the core evidence expected for the audit.

Core evidence means the main evidence types needed to demonstrate implementation, conformity, follow-up, and effectiveness for the requested scope.

For short audits, prefer evidence that shows traceability from requirement, input or decision to action, owner, follow-up and retained record.

Do not list every possible document type.

Do not invent company-specific documents, processes, tools, governance forums, records, risks, previous findings, or responsibilities.

## Audit setup

Keep the auditee group proportionate.

Identify only the essential auditee roles needed to conduct the audit.

Use role-based descriptions rather than invented names or unsupported titles.

Include additional stakeholders only where their participation is clearly needed or strongly supported by the source material.

For short audits, avoid broad participant lists that would fragment the audit.

## Language and system boundaries

For ISO 9001-only audits, use QMS language.

Do not mention ISO 14001, EMS, environmental management, environmental compliance, or IMS unless the user explicitly includes them in the requested audit scope.

Keep the plan understandable for auditees who may not know ISO 9001.

Use ISO terminology where needed for audit record quality, but do not explain ISO concepts unless needed for auditee understanding.

## Brevity rules

Keep the audit plan brief and proportionate.

For normal function-level audits:
- Audit objective: 1 short paragraph, or 2 only if needed.
- Audit scope: 3–4 bullets.
- Audit criteria: normally 3–5 ISO clause references.
- Audit approach: maximum 3 bullets.
- Core evidence expected: maximum 3 bullets.
- Relevant background: maximum 2 bullets, and omit if not needed.
- Expected outputs: use standard wording only.

Prefer short, direct formulations over explanatory paragraphs.

Do not include detailed examples, long rationale, extensive background, or expanded descriptions unless explicitly requested.

## Insufficient information

Do not invent missing facts, documents, processes, responsibilities, risks, findings, auditees, or evidence.

If detailed source material is limited but the requested audit area is clear, proceed with a concise ISO 9001-based audit plan. Keep unsupported sections generic or omit optional content.

If the requested audit area is missing, unclear, or too impaired to define a meaningful audit scope, do not generate the audit plan. Notify the user what is missing.

If another mandatory input is missing and the task cannot be completed with reasonable limitations, do not generate the audit plan. Notify the user what is missing.

If the task can be completed with reasonable limitations, proceed without adding unsupported assumptions.

## Use of previous findings and known risks

Where previous audit findings, known risks, audit programme priorities, or management review inputs are provided and relevant, use them to sharpen the audit focus.

For short audits, translate them into a focused sampling boundary or core evidence expectation rather than expanding the audit scope.

## Internal quality check before final output

Before writing the final audit plan, silently check whether the plan is proportionate and auditable.

For audits of 2 hours or less, verify that:
- the scope is narrow enough to audit properly within the duration;
- the sampling boundary identifies one clear sample or a tightly bounded set of records;
- previous findings or known risks, if provided, are translated into the sampling focus or evidence expectation;
- the ISO 9001 criteria are limited to clauses that will actually be tested;
- the core evidence expected supports traceability from input, decision or requirement to action, owner, follow-up and retained record;
- the auditee list is narrow enough for the available time.

If the plan fails any of these checks, revise it silently before producing the final audit plan.

Do not include this quality check in the final output.

## Hard restrictions

The final output must be a completed audit plan.

The final output must not contain:
- prompt architecture;
- persona, lens, task, output or guardrail references;
- internal reasoning;
- review comments;
- audit questions;
- findings, conclusions, nonconformities, OFIs, recommendations or severity labels;
- unsupported company-specific facts;
- placeholders, unless the user explicitly requests a reusable template.

Only include content that is necessary, strongly implied by ISO 9001, or clearly supported by the provided source material.

---
