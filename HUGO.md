# Hugo Notes

This file tracks practical Hugo patterns and anti-patterns found while editing this repository.

## Build and Publish

- Local preview:
  - `hugo serve`
- Production build:
  - `hugo`
- Output directory:
  - Configured in `config.toml` as `publishDir = "docs"`

## Frontmatter Patterns

- Required baseline fields for new content pages:
  - `title`
  - `date`
- For reveal-style slide pages, include:
  - `layout: slide`
- Quote titles that contain `:` in YAML:
  - Good: `title: "Context > Probability: Design systems as AI infrastructure"`

## Content Structure Patterns

- Flat content files can work:
  - Example: `content/wiley/into-design-systems-2026/design-systems-ai-infrastructure.md`
- Leaf bundle can also work:
  - `content/.../<slug>/index.md`
- Branch bundle can also work when needed:
  - `content/.../<slug>/_index.md`
- Keep one clear convention per section to avoid broken links.

## Image Linking Patterns

- Images in `static/` should be linked with absolute paths from site root.
- If images are in `static/images/wiley/`, use:
  - `![Alt text](/images/wiley/file.png)`
- Avoid old relative paths that point to moved folders.

## Anti-Patterns to Avoid

- Malformed frontmatter boundary:
  - Bad: `---# Heading`
  - Good: close frontmatter with `---` on its own line, then body content.
- Mixing content reshapes and path rewrites in one step without verification.
- Bulk replacing image paths without checking file existence after move/copy.

## Safe Change Workflow

1. Run `hugo --quiet` before changes (baseline).
2. Make focused edits.
3. Run `hugo --quiet` again (post-check).
4. Open one known URL and confirm rendering.
5. If paths changed, validate at least one page per content group.
