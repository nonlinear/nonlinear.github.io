---
title: "Preview in Browser VSCode Extension"
date: 2026-01-14
description: "VSCode extension for quickly previewing HTML and web content in the browser"
status: draft
fonts:
  - safiro-medium
---

A vscode extension that automatically opens browser page of any HTML or Markdown. Works with Hugo and Storybook.

## Installation

```
code --install-extension https://github.com/nonlinear/nonlinear.github.io/raw/main/.vscode/extensions/preview-in-browser/preview-in-browser-latest.vsix
```

or [Download .vsix](https://github.com/nonlinear/nonlinear.github.io/raw/main/.vscode/extensions/preview-in-browser/preview-in-browser-latest.vsix)

## Hugo flow

```mermaid
flowchart LR
    A([User opens file]) --> B{In content/ folder?}
    B -- No --> Z[Do nothing]
    B -- Yes --> C{Hugo server running?}
    C -- No --> D[Start Hugo server]
    D --> E([Open Simple Browser])
    C -- Yes --> E
```

## Storybook flow

```mermaid
flowchart LR
    A([User opens component]) --> B{Is .stories file?}
    B -- No --> Z[Do nothing]
    B -- Yes --> C{Storybook running?}
    C -- No --> D[Start Storybook]
    D --> E([Open Simple Browser])
    C -- Yes --> E
```

## Roadmap

- Simple Browser on a separate tab column
- Publish on vscode marketplace?
