---
type: prompt-module
module_type: readme
domain: generic
sub-domain:
references:
tags:
  - prompt-library
  - readme
status: draft
version: 0.5
created: 2026-05-11
updated: 2026-06-30
related: []
---
# Modular Prompt Stack

A modular prompt library for building structured, reusable AI workflows.

## Overview

This repository contains prompt modules and assembled prompts used to support repeatable AI-assisted work. The basic idea is to avoid one large all-purpose prompt and instead combine smaller prompt parts with clear responsibilities.

The library started as a set of ISO auditing prompts. That origin is still visible in some conventions, such as YAML frontmatter, evidence-oriented wording, reviewer prompts, and audit-related artefacts. Over time, the same structure proved useful beyond auditing, especially for work that needs clear roles, context, task instructions, and output control.

> Modular Prompt Stack is not an alternative name for agents. It is a disciplined prompt architecture that can later be used inside agentic workflows.

## Purpose

The purpose of this repository is to make prompts easier to reuse, review, improve, and combine.

A modular prompt is easier to understand than a long single prompt. It is also easier to adjust when something does not work. If the result is weak, the issue is usually easier to trace to the persona, task, context, output format, or source material.

## Core idea

Prompts are built from smaller parts.

A persona defines the voice and judgement style.

A task module explains what needs to be done.

An output module controls how the answer should be structured.

A context module contains reusable background assumptions, organisational information, or methodological framing that contextualises the task.

Source documents provide the material to work with.

Additional modules like lenses further increase modularity.

Together, these parts form a prompt stack.

## Status

This is a working repository, not a finished framework.

Some parts are still specific to ISO auditing and compliance work. Some are more general. The structure will evolve as the prompts are tested, used, and improved.

## Use

Use this repository as a practical prompt library.

Consult [Modular Prompt Stack](docs/Modular%20Prompt%20Stack.md) for use instructions and examples.

The priority is clarity, reuse, and controlled improvement.

## Tech stack

This repository assumes [Obsidian](https://obsidian.md/) as the main way of defining and linking prompts: YAML frontmatter, link syntaxis, markdown dialect.

Creating `bakes` requires [Obsidian](https://obsidian.md/) `Easy Bake` plugin or similar. It is also possible to form a bake by exporting ready assemblies to PDF.

It is possible to use the modules without [Obsidian](https://obsidian.md/). In such case, build assemblies / bakes by manually copy-paste related modules' text together into one file ignoring frontmatter.

---

