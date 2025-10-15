# GitHub Copilot Instructions

## Purpose
This document provides guidelines for using GitHub Copilot effectively in the ***REMOVED***.nyc project. The goal is to ensure consistency, productivity, and alignment with the project's technical and creative objectives.

---

## Project Overview
- **Framework**: Hugo static site generator
- **Languages**: HTML, SCSS, JavaScript (including p5.js)
- **Key Features**:
  - Dynamic JavaScript loading based on frontmatter (`styles` and `slug`)
  - Modularized p5.js logic for canvas creation and resizing
  - Curva podcast section with custom layouts and RSS feeds

---

## Guidelines for Copilot Usage

### 1. Dynamic JavaScript Loading
- **File**: `layouts/partials/load-js.html`
- **Logic**:
  - Load JavaScript files dynamically based on `styles` and `slug` frontmatter.
  - Prioritize `.min.js` over `.js`.
  - Support folder-based organization and alphanumeric ordering.
- **Tips**:
  - Ensure `load-js.html` is included in the relevant layout files.
  - Debug using the generated HTML to verify script inclusion.

### 2. Modularized JavaScript Logic
- **Files**: `static/js/scripts/processing-1.js`, `static/js/scripts/nav-p5.js`
- **Logic**:
  - Use p5.js for dynamic canvas creation and resizing.
  - Modularize code for reusability across layouts.
- **Tips**:
  - Follow DRY (Don't Repeat Yourself) principles.
  - Test sketches in isolation before integration.

### 3. Curva Podcast Section
- **Files**: `layouts/curva/single.html`, `layouts/curva/rss.xml`
- **Logic**:
  - Customize layouts for the Curva podcast section.
  - Ensure RSS feeds are functional and up-to-date.
- **Tips**:
  - Validate RSS feeds using online tools.
  - Maintain consistency with the site's overall design.

---

## Best Practices
- **Code Quality**:
  - Write clean, readable, and maintainable code.
  - Use comments to explain complex logic.
- **Testing**:
  - Test changes locally before committing.
  - Use `hugo serve` to preview the site.
- **Version Control**:
  - Commit changes with descriptive messages.
  - Use branches for significant updates.

---

## Common Tasks

### 1. Debugging `load-js.html`
- Verify the partial is included in the layout.
- Check the frontmatter of the content files.
- Inspect the generated HTML for script tags.

### 2. Updating JavaScript Files
- Place new scripts in `static/js/scripts/`.
- Follow the naming convention: `slug.min.js` > `slug.js`.
- Update `load-js.html` logic if necessary.

### 3. Managing Content
- Use Markdown for content files in `content/`.
- Organize assets in `static/`.
- Update RSS feeds for new podcast episodes.

---

## Additional Notes
- Refer to `readme.md` for the changelog and TODOs.
- Use GitHub issues to track bugs and feature requests.
- Collaborate with team members to ensure alignment.

---

## Contact
For questions or assistance, contact the project maintainer.