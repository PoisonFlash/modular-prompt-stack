---
type: prompt-module
module_type: linter
domain: generic
standards:
scope:
tags:
  - prompt-library
  - prompt/linter
status: draft
version: 0.1
created: 2026-05-11
updated: 2026-05-11
related: []
---

# Linter – markdown

## MASTER INSTRUCTION

Modify the provided text/document(s) by applying the rules below in a strict, sequential order.

If no documents are provided and/or no review text is pasted, do NOT generate any output and instead request the user to provide text/document(s).

When finished, return:

1. The revised version of the text/document(s)
2. A brief summary of changes made

## EXECUTION PRIORITY

If rules conflict, apply them in the following order:

1. Preserve original meaning (no loss or distortion of content)
2. Improve clarity and readability
3. Apply structure rules
4. Apply formatting rules

Do not rewrite or rephrase content unless required to meet the rules above. Keep wording as close to the original as possible.

## OUTPUT FORMAT

Structure the response as follows:

```
# revised text
[updated document]

# summary of changes
- [concise bullet points describing key changes]
```

## CONTENT TRANSFORMATION RULES

### Lists vs narrative

- Convert lists to plain text narrative **only when all items are full sentences forming a natural paragraph**
- Keep lists if:
    - items are short phrases, keywords, or labels
    - structure improves readability or clarity
- Do not partially convert lists – apply consistently per list

### Colon-based statements

- Convert “statement: explanation” into a single narrative sentence **only when the structure is clearly prose**
- Do NOT convert when used for:
    - definitions
    - technical labels
    - structured data or specifications

Example:

- “Real Impact: This is where AI can bring real impact.” → “AI can bring real impact in this area.”

## TEXT STRUCTURE RULES

- Ensure correct markdown hierarchy:
    - H1 for document title
    - H2 for main sections
    - H3-H4 as needed
- Do not allow H5 and deeper levels. If they are in the text, convert to bold regular text instead.
- Adjust heading levels where necessary to maintain consistency
- Ensure proper spacing:
    - one empty line before and after headings
    - no redundant blank lines
- Remove markdown separator lines (---), except where required for metadata blocks

## LIST STRUCTURE RULES

- Flatten nested lists to a maximum of one level
- Preserve all content when flattening (no loss of meaning)
- If flattening reduces clarity, convert to narrative instead
- Ensure consistent markdown formatting:
    - correct indentation
    - consistent bullet or numbering style
    - proper spacing

## FORMATTING RULES

### Dashes

- Never allow long dashes (—)
- Replace long dashes and short dashes used as sentence separators with mid dashes ( – ) with spaces on both sides
- Do NOT modify:
    - hyphenated words (e.g., “well-known”)
    - technical notation

### Titles

- Ensure that all titles are in consistent case – Sentence case or Title Case applied consistently to the whole text. If case is mixed, prioritise Title Case.

### Punctuation

- Add Oxford commas where appropriate

## FINAL QUALITY CHECK

Before returning output:

- Ensure no meaning has been altered
- Ensure formatting is consistent throughout
- Ensure no partial rule application (e.g., half-converted lists)
- Ensure clean and readable markdown structure

## SUMMARY REQUIREMENT

Provide a brief summary of changes, focusing on:

- structural improvements
- formatting corrections
- any notable transformations (e.g., lists to narrative)

---
