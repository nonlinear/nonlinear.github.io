# [nonlinear.nyc](https://nonlinear.nyc)

---

# Todo

## Creative code

- [ ] Warning/nudge logic (hover/click for more, dependencies expected, etc)
- [ ] Mailing list, Email Octopus

## Curva 

- [ ] Find screenflow equivalent
- [ ] Review curva RSS feed
- [x] Find zencastr or similar
- [ ] AWS for audio files
- [x] Test curva filter

---

# Done

## September 2025

**[presentation]** - [cleaning up speeddial, starting anew](https://github.com/nonlinear/nonlinear.github.io/commit/0f67835)  
    Major refactor of speeddial logic and styles in `assets/css/speeddial.scss`, `content/speeddial.html`, `static/js/script/speeddial.js`

**[presentation]** - [consolidating layouts](https://github.com/nonlinear/nonlinear.github.io/commit/48d44f1)  
    Merged illos layout into default, updated `layouts/partials/single.html`, removed `layouts/illos/single.html`, backup in `layouts/illos/single.html.bak`

**[documentation]** - [readme](https://github.com/nonlinear/nonlinear.github.io/commit/9812dfb)  
    Updated documentation and changelog in `readme.md`, affected: `content/speeddial.html`, `layouts/partials/load-js.html`, `static/js/script/illos.js`

**[presentation]** - [js from slug or type](https://github.com/nonlinear/nonlinear.github.io/commit/a2f567d)  
    Refactored JS loader to use slug/type logic in `layouts/partials/load-js.html`  
    Updated post content files: `content/3dcarousel.html`, `content/carousel.html`, `content/test.md`

**[presentation]** - [back to js-](https://github.com/nonlinear/nonlinear.github.io/commit/a2f567d)  
    Refactored JS loader to use slug/type logic in `layouts/partials/load-js.html`  
    Updated post content files for new JS logic

**[documentation]** - [redoing jsLib and jsScript and TODO on readme](https://github.com/nonlinear/nonlinear.github.io/commit/17d5165)  
    Updated JS loader logic in `layouts/partials/load-js.html`  
    Updated TODOs in `readme.md`  
    Added/updated scripts in `content/speeddial.html`

**[bug]** - [rss feeds](https://github.com/nonlinear/nonlinear.github.io/commit/02c0970)  
    Improved RSS logic in `layouts/_default/rss.xml` and `layouts/curva/rss.xml`  
    Updated `content/test.md`

**[presentation]** - [cover conditions](https://github.com/nonlinear/nonlinear.github.io/commit/344932b)  
    Refined cover image selection logic in `layouts/partials/head.html`  
    Updated `content/dudes.md`

**[presentation]** - [illos og:image default](https://github.com/nonlinear/nonlinear.github.io/commit/523d1ef)  
    Added default og:image logic for illos in `layouts/partials/head.html`

**[bug]** - [rss feed fix](https://github.com/nonlinear/nonlinear.github.io/commit/a870824)  
    Fixed RSS output format in `config.toml`  
    Updated RSS templates

**[documentation]** - [image priority comment](https://github.com/nonlinear/nonlinear.github.io/commit/d201d0a)  
    Added documentation comment for image priority in `layouts/partials/head.html`
