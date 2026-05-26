---
type: prompt-module
module_type: readme
domain: generic
standards:
scope:
tags:
  - prompt-library
  - readme
status: draft
version: 0.2
created: 2026-05-11
updated: 2026-05-20
related: []
---

# Modular Prompt Stack

## Core Idea

A task is not handled by one large prompt. It is assembled from reusable modules, where each module has a clearly limited role: connection logic, persona, context, task instruction, output format, and input documents.

This prompt library uses a modular prompt-stack architecture. Each task is assembled from reusable modules: a master connector, optional persona, optional context, task instruction, output format, and input documents.

The design follows established prompt-engineering principles: separating instruction, context, input data, and output format; using role prompting for reviewer perspective; applying context engineering to control the information available to the model; and using prompt chaining for multi-step workflows such as, e.g., audit planning, evidence review, and audit reporting.

## Architecture

A modular prompt stack using role prompting, context engineering, task-specific instruction, and structured output control.

```mermaid

flowchart LR
    M[Master connector] -->|Defines how modules interact| A[Prompt assembly]

    P[Persona] -->|Judgement style, tone| A
    L[Lens] -->|Task-oriented lens| A
    C[Context] -->|Background facts and assumptions| A
    T[Task] -->|What work to perform| A
    O[Output format] -->|How answer should be structured| A
    I[Input documents] -->|Material to analyse or use| A

    A --> R[Final response]

```

## Logic

Master connector = how to combine modules
Persona = who is thinking and speaking
Lens = how the persona performs
Context = what background matters
Task = what to do
Output = how to present it
Input = what to work on

## Governance

Each module must do one job only.

The persona must not contain task instructions.
The lens only informs perspective.
The task must not contain personality.
The context must not become evidence unless instructed.
The output format must not decide the substance.
The master connector must coordinate, not analyse.

## Example

Persona: professional auditor
Lens: reviewer
Task: review audit plan
Context: organisation and scope
Output: specific output format

---
