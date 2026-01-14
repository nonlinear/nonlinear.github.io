---
title: "Preview in Browser VSCode Extension"
date: 2026-01-14
description: "VSCode extension for quickly previewing HTML and web content in the browser"
status: draft
fonts:
  - safiro-medium
---

## Installation

```
code --install-extension https://github.com/nonlinear/nonlinear.github.io/raw/main/.vscode/extensions/preview-in-browser/preview-in-browser-latest.vsix
```

or [Download .vsix](https://github.com/nonlinear/nonlinear.github.io/raw/main/.vscode/extensions/preview-in-browser/preview-in-browser-latest.vsix)

## Features

- Detects hugo, runs server
- Opens Simple Browser with corresponding Hugo URL

## Roadmap

- Detects storybook, runs server
- Opens Simple Browser with corresponding storybook URL

```mermaid
flowchart TD
    A([User opens or switches to a file]) --> B{File in content/ folder?}
    B -- No --> Z[Do nothing]
    B -- Yes --> C{File is .md or .html?}
    C -- No --> Z
    C -- Yes --> D{Same as last opened file?}
    D -- Yes --> Z
    D -- No --> E[Mark as last opened file]
    E --> F{Hugo server running?}
    F -- Yes --> G[Build preview URL]
    F -- No --> H{Hugo already starting?}
    H -- Yes --> I[Wait for startup]
    H -- No --> J[Start hugo serve -D]
    J --> K[Wait 3 seconds]
    K --> G
    I --> G
    G --> L[Extract path from content/]
    L --> M[Remove file extension]
    M --> N[Append to base URL]
    N --> O[Open Simple Browser beside editor]
    O --> P[Return focus to code editor]
    P --> Q([Preview ready!])
```
