---
title: Post documentation
description: how to write posts
status: draft
class:
  - post
date: 2025-06-14
---

## class

- animatewithsass
- mixins

## js

- [gsap.min](https://greensock.com/gsap) {#gsapmin}: GSAP is a powerful JavaScript animation library for smooth, high-performance animations of CSS, SVG, canvas, and more.
- [ScrollTrigger.min](https://greensock.com/scrolltrigger) {#scrolltriggermin}: A GSAP plugin to trigger animations based on scroll position. Great for scroll-driven effects. Dependencies: [gsap.min](#gsapmin)
- [ScrollSmoother.min](https://greensock.com/scrollsmoother) {#scrollsmoothermin}: A GSAP plugin that smooths page scrolling for a fluid experience, useful for parallax and easing abrupt scrolls. Dependencies: [gsap.min](#gsapmin), [ScrollTrigger.min](#scrolltriggermin)
- [ScrollToPlugin.min](https://greensock.com/scrolltoplugin) {#scrolltopluginmin}: A GSAP plugin to animate smooth scrolling to specific page positions or elements. Useful for smooth navigation. Dependencies: [gsap.min](#gsapmin)
- [SplitText.min](https://greensock.com/splittext) {#splittextmin}: A GSAP plugin that splits text into lines, words, or characters for detailed text animations. Dependencies: [gsap.min](#gsapmin)
- [imagesloaded.pkgd.min](https://imagesloaded.desandro.com/) {#imagesloadedpkgdmin}: JavaScript library that detects when images have fully loaded, useful to trigger scripts depending on loaded images.


## css

## import

if you want to add a css file per post
1. make sure to use `static/POST/css/STYLE1.css` (or `STYLE2`, `STYLE3`, in order)
2. write on frontmatter `import: STYLE1, STYLE2, STYLE3`
