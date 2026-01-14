---
title: "Search Path for EPUBs and PDFs"
date: 2026-01-13
status: live
description: "Extending file links to support auto-search within EPUBs and PDFs"
fonts:
  - safiro-medium
tags:
  - concept
  - standard
  - ebook
---

## Description

Extending bare links for EPUB and PDF files to support an auto search, using a format like: `file://FILEPATH.EXT?search="STRING"`

When accessed, this link would automatically perform a search for the given string within the file.

```mermaid
flowchart TD
    A(User clicks file path) --> B{Search path?}
    B -- No --> C[Open file, ignoring search]
    B -- Yes --> D{Is string found?}
    D -- No --> C
    D -- Yes, one entry --> E[Open file at search point, highlighted]
    D -- Yes, multiple entries --> F[Open file with search modal and results to choose]
```

> This allows for more precise AI source lists, especially on EPUBs or other files with no pagination.
