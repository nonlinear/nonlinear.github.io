---
layout: slide

title: "Ship It! Vibe Coding Your First Figma Plugin"
speaker: Davy Fung
company: Atlassian Design System
time: Friday, March 20 - 9:30 PM
link: https://www.intodesignsystems.com/agenda/vibe-coding-figma-plugin
date: 2026-03-20
---
# Ship It! Vibe Coding Your First Figma Plugin

---

![](/images/wiley/screenshot-16-35-35.png)

---

![](/images/wiley/screenshot-16-38-06.png)

---

![](/images/wiley/screenshot-16-42-00.png)

---

![](/images/wiley/screenshot-16-43-24.png)

---

> ### Build a [headless / (W×H)px Ul] Figma plugin that [does

---

> X main goal]. [does X action].

Build a [headless / (W×H)px UIl Figma plugin that [does
X main goall.
The user should see: [Describe VI elements, inputs, buttons, and
loading states - if applicablel
How it should work:
• It should look at [selected layers / all layers / specific types
of objects on the page]
• [Step 1 of the behavior/logic]
• [step 2 of the behavior/logic]
• [What edge cases to avoid / What to do if there's no selection]
• [what success notification to show at the end]

---

# IDS - Making your first Figma plugin!

---

## Prompt 1

---

- If nothing is selected, close with "Please select at least one frame"

---

## Prompt 2
Build a Figma plugin (320x320px UI) that helps organise presentation slides.

---

**Arrange slides** - Sort selected frames (or all top-level frames if none selected) numerically by name, then
lay them out left to right with a configurable gap (default 40px). Include a toggle in the UI: if "Wrap in
auto-layout" is checked, place the frames inside a new horizontal auto-layout frame called "Davy's AutoLayout":
otherwise just reposition them in place. Show a gap input (number field) and the toggle checkbox in the UI.

---

**Renumber slides** - Sort selected frames (or all top-level frames if none selected) left to right by position.
Rename each using a configurable prefix (default "Slide "') and a configurable start number (default "1") - e.
g. "SLide 1", "Slide 2". Show a prefix text input and a start-number input in the UI.
Show a status notification after each action.

---

## Prompt 3
Build a Figma plugin (360x520px UI) that audits unstyled text across the current page.