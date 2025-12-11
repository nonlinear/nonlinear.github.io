[nonlinear.nyc](https://nonlinear.nyc) is a personal site for Nicholas Frota, built with [Hugo](https://gohugo.io/) for knowledge management, creative coding experiments, and digital publishing. It serves as a content-first platform for notes, illustrations, podcasts, and interactive web features, with a modular structure for rapid prototyping and documentation.

Repository: [nonlinear/nonlinear.github.io](https://github.com/nonlinear/nonlinear.github.io)

View [TODO](https://github.com/nonlinear/nonlinear.github.io/blob/main/TODO.md), [done](https://github.com/nonlinear/nonlinear.github.io/blob/main/done.md)

## Architecture

- **[content/](https://github.com/nonlinear/nonlinear.github.io/tree/main/content)**: Markdown and HTML files organized by topic and type (e.g., curva podcast, drawings, experiments).
- **[assets/](https://github.com/nonlinear/nonlinear.github.io/tree/main/assets)** & **[static/](https://github.com/nonlinear/nonlinear.github.io/tree/main/static)**: CSS, JS, images, and fonts for site styling and interactivity.
- **Site Build**: [Hugo](https://gohugo.io/) builds the site from `content/` and outputs to [docs/](https://github.com/nonlinear/nonlinear.github.io/tree/main/docs) for GitHub Pages publishing.
- **[config/](https://github.com/nonlinear/nonlinear.github.io/tree/main/config)**: TOML files for site settings.
- **[data/](https://github.com/nonlinear/nonlinear.github.io/tree/main/data)**: YAML files for tags and podcast metadata.
- **[layouts/](https://github.com/nonlinear/nonlinear.github.io/tree/main/layouts)**: Hugo templates, shortcodes, and partials for page rendering.
- **[.github/scripts/](https://github.com/nonlinear/nonlinear.github.io/tree/main/.github/scripts)**: Python scripts for syncing media, comics, and inspiration images.

## Key Components

- **[content/](https://github.com/nonlinear/nonlinear.github.io/tree/main/content)**: Main source of posts, notes, and experiments
- **[assets/](https://github.com/nonlinear/nonlinear.github.io/tree/main/assets)** & **[static/](https://github.com/nonlinear/nonlinear.github.io/tree/main/static)**: Styling, images, and JS for UI/UX
- **[layouts/](https://github.com/nonlinear/nonlinear.github.io/tree/main/layouts)**: Hugo templates, shortcodes, and partials
- **[data/](https://github.com/nonlinear/nonlinear.github.io/tree/main/data)**: YAML files for tags and podcast metadata
- **[config/](https://github.com/nonlinear/nonlinear.github.io/tree/main/config)**: Site-wide configuration (config.toml)
- **[docs/](https://github.com/nonlinear/nonlinear.github.io/tree/main/docs)**: Build output for GitHub Pages
- **[.github/scripts/](https://github.com/nonlinear/nonlinear.github.io/tree/main/.github/scripts)**: Automation scripts for media and asset management

## Technologies Used

- [Hugo](https://gohugo.io/) (static site generator)
- Markdown & HTML
- SCSS/CSS
- JavaScript
- Python (automation scripts)
- YAML/TOML (configuration)
- Git & GitHub Pages
