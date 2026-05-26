---
type: prompt-module
module_type: task
domain: iso-management-system
standards:
  - ISO 9001:2015
  - ISO 14001:2015
scope:
  - internal-audit
  - management-system
tags:
  - prompt-library
  - iso/9001
  - iso/14001
  - ims
  - prompt/task
status: prod
version: 1
created: 2026-05-11
updated: 2026-05-11
related: []
---

# Task: Assess the applicability of the provided regulation

Assess whether the provided regulation is applicable to the organisation within the scope defined in the organisational context.

Use the available organisational context to understand scope, assumptions, activities, and relevant limitations.

If no regulation is provided as text or as an attached file, state that the regulation is missing and stop.

If no organisational context is available from a context module, text entry, or attached file, state that the organisational context is missing and stop. Do not assess applicability without knowing the organisational scope.

If classification cannot be assigned without guessing, state what information is missing and stop.

Determine the organisation’s relevant role under the regulation where this affects applicability, such as operator, owner, employer, producer, user, holder, importer, distributor, service provider, reporting entity, or another regulated actor.
