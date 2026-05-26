---
type: prompt-module
module_type: output_format
domain: iso-management-system
standards:
  - ISO 14001:2015
  - ISO 9001:2015
scope:
  - internal-audit
  - management-system
  - legal-monitoring
tags:
  - prompt-library
  - iso/9001
  - iso/14001
  - lagbevakning
  - prompt/output
status: prod
version: 1
created: 2026-05-11
updated: 2026-05-11
related:
  - "[[Master Connector]]"
  - "[[Review regulation applicability (own operations)]]"
---

# Output format – Regulation applicability

Generate exactly three blocks of text, separated by blank lines.

```markdown
Applicability: [Direct / Indirect / Not applicable] – [short reason] 
 
[Short compliance-register comment explaining: main regulatory target, why the organisation is or is not directly in scope, and the practical own-operations relevance. 2-4 sentences maximum. Do not label this block.]
  
[Shorter one-line version. Do not label this block.]
```

Do not include headings, field labels, intro text, outro text, sources, or references.

---
