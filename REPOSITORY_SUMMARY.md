# Repository Analysis: nonlinear.github.io

## Overview

nonlinear.github.io is a Hugo-powered static site for personal knowledge management, creative coding experiments, and digital publishing. It serves as a content-first platform for notes, illustrations, podcasts, and interactive web features, with a modular structure for rapid prototyping and documentation.

## Architecture

- **Content**: Markdown and HTML files in `content/` organized by topic and type (e.g., curva podcast, drawings, experiments).
- **Static Assets**: CSS, JS, images, and fonts in `assets/` and `static/` for site styling and interactivity.
- **Site Build**: Hugo builds the site from `content/` and outputs to `docs/` for GitHub Pages publishing.
- **Configuration**: TOML and YAML files in `config/` and `data/` for site settings, tags, and podcast metadata.
- **Layouts**: Hugo templates in `layouts/` for page rendering, shortcodes, and partials.
- **Automation**: Python scripts in `.github/scripts/` for syncing media, comics, and inspiration images.

## Key Components

- **content/**: Main source of posts, notes, and experiments
- **assets/** & **static/**: Styling, images, and JS for UI/UX
- **layouts/**: Hugo templates, shortcodes, and partials
- **data/**: YAML files for tags and podcast metadata
- **config/**: Site-wide configuration (config.toml)
- **docs/**: Build output for GitHub Pages
- **.github/scripts/**: Automation scripts for media and asset management

## Technologies Used

- Hugo (static site generator)
- Markdown & HTML
- SCSS/CSS
- JavaScript
- Python (automation scripts)
- YAML/TOML (configuration)
- Git & GitHub Pages

## Data Flow

- Content is authored in Markdown/HTML and organized in `content/`
- Hugo processes content, applies layouts/templates, and outputs static files to `docs/`
- Static assets are referenced in layouts and content for styling and interactivity
- Automation scripts sync external media and assets
- Configuration and metadata are loaded from TOML/YAML files

## Team and Ownership

- Main contributors: Nicholas Frota, nonlinear
- Nicholas Frota leads creative coding, architecture, and content
- nonlinear handles automation, infrastructure, and publishing
