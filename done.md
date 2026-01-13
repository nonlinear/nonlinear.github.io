## December 2025

🔧 [CNAME](https://github.com/nonlinear/nonlinear.github.io/commit/d55510f2): Added or updated the CNAME file in the assets directory for domain configuration. (2025-12-04)

🔧 [dude as redirect](https://github.com/nonlinear/nonlinear.github.io/commit/52a73f91): Changed `dudes.md` to a redirect, updating tags and sitemap accordingly. (2025-12-07)

🎨 [less experiments](https://github.com/nonlinear/nonlinear.github.io/commit/903c149d): Reduced the number of experiments in the codebase, focusing on core features. (2025-12-07)

🎨 [cryboy](https://github.com/nonlinear/nonlinear.github.io/commit/65a8878b): Added new SVG and HTML assets for the “cryboy” experiment, including multiple vector variations. (2025-12-07)

🎨 [feat: add Python automation scripts](https://github.com/nonlinear/nonlinear.github.io/commit/743ef03f): Added new Python scripts for automation: syncing comics, settings, and posting new illustrations. (2025-12-04)

🔧 [fix: restore CNAME with correct domain](https://github.com/nonlinear/nonlinear.github.io/commit/9b93bbc5): Fixed the CNAME file to ensure the custom domain works for GitHub Pages. (2025-12-04)

🔧 [dedupe files](https://github.com/nonlinear/nonlinear.github.io/commit/96595896): Further deduplication and cleanup of scripts and image assets. (2025-12-05)

🔧 [dedupe](https://github.com/nonlinear/nonlinear.github.io/commit/e1f4bd9c): Deduplicated image and asset files, reducing redundancy in the image directories. (2025-12-05)

🔧 [remove removed](https://github.com/nonlinear/nonlinear.github.io/commit/f892ee2c): Cleaned up deprecated files and configuration, removing unused or obsolete content and tags. (2025-12-04)

🔧 [fix: restore nonlinear.nyc domain from **_REMOVED_**](https://github.com/nonlinear/nonlinear.github.io/commit/1f363676): Restored the main domain and updated multiple content and index files to ensure the site points to the correct address. (2025-12-04)

🔧 [latestpost Hugo shortcode](https://github.com/nonlinear/nonlinear.github.io/commit/DEC2025)
Created and refined `layouts/shortcodes/latestpost.html` to output a Markdown/HTML link to the latest post, excluding posts with `type: redirect`. - Filtering logic: uses Hugo `where` to exclude any post with `type: redirect` in frontmatter (e.g. `type: redirect` in `content/dudes.md`, `content/sketches-1.html`, `content/latest.html`). - Sorts by `Date` descending. - Renders link as HTML using `markdownify`. - Fixes: empty link text (missing titles), raw Markdown output, inclusion of redirects. - See TODO for missing titles and testing steps.

🎨 [cleaning up speeddial, starting anew](https://github.com/nonlinear/nonlinear.github.io/commit/0f67835)
Major refactor of speeddial logic and styles in `assets/css/speeddial.scss`, `content/speeddial.html`, `static/js/script/speeddial.js`

🎨 [consolidating layouts](https://github.com/nonlinear/nonlinear.github.io/commit/48d44f1)
Merged illos layout into default, updated `layouts/partials/single.html`, removed `layouts/illos/single.html`, backup in `layouts/illos/single.html.bak`

📄 [readme](https://github.com/nonlinear/nonlinear.github.io/commit/9812dfb)
Updated documentation and changelog in `readme.md`, affected: `content/speeddial.html`, `layouts/partials/load-js.html`, `static/js/script/illos.js`

🎨 [js from slug or type](https://github.com/nonlinear/nonlinear.github.io/commit/a2f567d)
Refactored JS loader to use slug/type logic in `layouts/partials/load-js.html`
Updated post content files: `content/3dcarousel.html`, `content/carousel.html`, `content/test.md`

🎨 [back to js-](https://github.com/nonlinear/nonlinear.github.io/commit/a2f567d)
Refactored JS loader to use slug/type logic in `layouts/partials/load-js.html`
Updated post content files for new JS logic

📄 [redoing jsLib and jsScript and TODO on readme](https://github.com/nonlinear/nonlinear.github.io/commit/17d5165)
Updated JS loader logic in `layouts/partials/load-js.html`
Updated TODOs in `readme.md`
Added/updated scripts in `content/speeddial.html`

🐞 [rss feeds](https://github.com/nonlinear/nonlinear.github.io/commit/02c0970)
Improved RSS logic in `layouts/_default/rss.xml` and `layouts/curva/rss.xml`
Updated `content/test.md`

🎨 [cover conditions](https://github.com/nonlinear/nonlinear.github.io/commit/344932b)
Refined cover image selection logic in `layouts/partials/head.html`
Updated `content/dudes.md`

🎨 [illos og:image default](https://github.com/nonlinear/nonlinear.github.io/commit/523d1ef)
Added default og:image logic for illos in `layouts/partials/head.html`

🐞 [rss feed fix](https://github.com/nonlinear/nonlinear.github.io/commit/a870824)
Fixed RSS output format in `config.toml`
Updated RSS templates

📄 [image priority comment](https://github.com/nonlinear/nonlinear.github.io/commit/d201d0a)
Added documentation comment for image priority in `layouts/partials/head.html`

🔧 [fix: restore nonlinear.nyc domain from **_REMOVED_**](https://github.com/nonlinear/nonlinear.github.io/commit/1f363676)
Restored the main domain and updated multiple content and index files to ensure the site points to the correct address.

🔧 [remove removed](https://github.com/nonlinear/nonlinear.github.io/commit/f892ee2c)
Cleaned up deprecated files and configuration, removing unused or obsolete content and tags.

🔧 [dedupe](https://github.com/nonlinear/nonlinear.github.io/commit/e1f4bd9c)
Deduplicated image and asset files, reducing redundancy in the image directories.

🔧 [dedupe files](https://github.com/nonlinear/nonlinear.github.io/commit/96595896)
Further deduplication and cleanup of scripts and image assets.

🔧 [fix: restore CNAME with correct domain](https://github.com/nonlinear/nonlinear.github.io/commit/9b93bbc5)
Fixed the CNAME file to ensure the custom domain works for GitHub Pages.

🎨 [feat: add Python automation scripts](https://github.com/nonlinear/nonlinear.github.io/commit/743ef03f)
Added new Python scripts for automation: syncing comics, settings, and posting new illustrations.

🎨 [cryboy](https://github.com/nonlinear/nonlinear.github.io/commit/65a8878b)
Added new SVG and HTML assets for the “cryboy” experiment, including multiple vector variations.

🎨 [less experiments](https://github.com/nonlinear/nonlinear.github.io/commit/903c149d)
Reduced the number of experiments in the codebase, focusing on core features.

🔧 [dude as redirect](https://github.com/nonlinear/nonlinear.github.io/commit/52a73f91)
Changed `dudes.md` to a redirect, updating tags and sitemap accordingly.

🔧 [CNAME](https://github.com/nonlinear/nonlinear.github.io/commit/d55510f2)
Added or updated the CNAME file in the assets directory for domain configuration.
