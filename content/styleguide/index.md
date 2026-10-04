---
title: "Styleguide — content elements"
type: page
layout: styleguide
url: "/styleguide/"
---

The full inventory of content elements the site must render. This page is the
**exercise**: enumerate every element *before* designing it. Everything here is
placeholders — the point is coverage, not beauty.

{{< sg "h1" >}}{{< /sg >}}

## Headings

The type scale (h1–h6) — one family, well used.

### H3 — section

#### H4 — sub-section

##### H5 — rarely used

###### H6 — caption scale

## Paragraphs

{{< lorem n=2 >}}

A paragraph with **bold**, *italic*, `inline code`, and a [link](https://nonlinear.nyc).
Also ~~strikethrough~~, H~2~O subscript, and E=mc^2^ superscript.

## Lists

Unordered:

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
  - Nested item — sed do eiusmod
  - Nested item — tempor incididunt
- Ut labore et dolore magna aliqua

Ordered:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Sed do eiusmod tempor

Definition list:

Term
: Lorem ipsum dolor sit amet definition.

## Blockquote

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
> incididunt ut labore et dolore magna aliqua.
>
> — Attribution, source

## Code

Inline `const x = 1`. Block:

```js
// fenced code block with language
function hello(name) {
  return `Hello, ${name}`;
}
```

```
// fenced code block, no language
plain text preformatted
```

Indented code (4 spaces) also supported by Markdown.

## Tables

| Element | Status | Notes |
|---|---|---|
| Headings | draft | scale TBD |
| Lists | draft | nested ok |
| Tables | draft | responsive? |

## Media

Image (single):

{{< img label="single image — figure" >}}

Image with caption:

{{< img label="image with caption" >}}

Mermaid diagram:

{{< mmd >}}
flowchart TD
  A[content element] --> B{renders?}
  B -->|yes| C[done]
  B -->|no| D[TODO]
{{< /mmd >}}

## Dividers

---

## Footnotes

A sentence with a footnote.[^1]

[^1]: Lorem ipsum footnote text.

## Callouts

<!-- TODO: callout/alert component (note, tip, warning) — pattern-library component:callout -->

{{< lorem n=1 >}}

## Embedded / interactive (later)

<!-- TODO: video embed, image gallery, carousel, tabs, accordion — list first, design later -->
