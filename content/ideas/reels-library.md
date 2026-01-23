---
title: "Instagram Reels Library"
date: 2026-01-22
description: "Automated workflow for scraping, enriching, and organizing saved Instagram reels"
status: draft
---

## Instagram Scraping Workflow

This project automates the collection and organization of saved Instagram Reels and posts, making it easy to build a curated library of visual references and inspiration.

### The Process

1. **Scrape** → Extract links from Instagram saved collections
2. **Enrich** → Add titles and metadata to posts
3. **Untag** → Remove posts from Instagram saved (cleanup)

---

## Scripts

### 1. Scrape ([scrape_reels.py](.github/scripts/instagram/scrape_reels.py)) ✅ Live

**Purpose:** Extract links from your Instagram saved collections

**How it works:**

- Opens browser for manual Instagram login (avoids bot detection)
- Transfers cookies to headless browser for automation
- Navigates to your saved collections page
- Lists all available saved groups (e.g., "fashion-inspiration", "interesting-history")
- Prompts you to choose which group to scrape
- Scrolls and collects post links from that group
- For each post, extracts:
  - Post URL
  - Caption/title (first line of text)
  - Hashtags from caption
  - Group name as hashtag
  - **Author username** (@username)
- Marks posts with #enrich if title extraction fails
- Appends results to output file with #untag marker

**Output format:**

```markdown
- [Title from caption](https://instagram.com/p/ABC123/) #group-name #hashtag1 #hashtag2 @username #untag
```

If title extraction fails:

```markdown
- [(no title)](https://instagram.com/p/ABC123/) #group-name @username #untag #enrich
```

**Environment variables:**

- `IG_SCRAPE_OUTPUT_PATH` - Where to save (defaults to this file)
- `IG_SCRAPE_COUNT` - Posts to scrape per run (default: 10)
- `INSTAGRAM_USER` - Username
- `INSTAGRAM_PASS` - Password

**Usage:**

```bash
python3.11 .github/scripts/instagram/scrape_reels.py
```

**Todos:**

- [x] Author username extraction
- [ ] Better caption extraction (more robust selectors)

---

### 2. Enrich ([enrich_reels.py](.github/scripts/instagram/enrich_reels.py)) ✅ Live

**Purpose:** Add titles and hashtags to posts marked with #enrich

**How it works:**

- Reads markdown file and finds posts with #enrich tag
- Visits each post to extract:
  - Caption text (longest span with hashtags)
  - **AI-style title** (5-7 meaningful words, removing filler)
  - **Hashtags** from caption
  - **Language tag** (#en-US, #pt-BR, etc.) using langdetect
  - **Date tag** (#2025-01-15 format)
  - **Author username** (@username)
- Removes #enrich tag after processing (success or failure)
- Safe file writing (temp file + rename)

**Metadata tags added:**

- Language: `#en-US`, `#pt-BR`, `#es-ES`, etc.
- Date: `#2025-01-15` (post publication date)
- Author: `@username`

**Todos:**

- [x] Language detection
- [x] Better title logic (AI-style with filler removal)
- [x] Date extraction
- [x] Author username
- [ ] Handle posts with no caption/hashtags better

---

### 3. Untag ([untag_reels.py](.github/scripts/instagram/untag_reels.py)) ✅ Live

**Purpose:** Remove posts from Instagram saved collection

**How it works:**

- Reads markdown file and finds posts with #untag tag
- Opens browser for manual login
- For each #untag post:
  - Opens the post URL
  - Clicks "Remove" button (SVG with aria-label="Remove")
  - Confirms removal by checking for "Save" button appearance
  - Removes #untag tag from markdown line
- Safe file writing (temp file + rename)

**Usage:**

```bash
python3.11 .github/scripts/instagram/untag_reels.py
```

**Todos:**

- [ ] Test untag confirmation logic (Save button detection)
- [ ] Handle edge cases (already unsaved posts)

---

## Dependencies

```bash
pip install selenium undetected-chromedriver python-dotenv langdetect
```

**Why these tools:**

- `selenium` - Browser automation
- `undetected-chromedriver` - Avoids Instagram bot detection
- `python-dotenv` - Load credentials from `.env` file
- `langdetect` - Detect language from caption text

---

## Workflow Example

```bash
# 1. Scrape 10 posts from "fashion-inspiration" group
python3.11 .github/scripts/instagram/scrape_reels.py
# → Adds entries with #untag and #enrich tags, @username, hashtags

# 2. Enrich posts (add AI titles, language, date)
python3.11 .github/scripts/instagram/enrich_reels.py
# → Adds smart titles, #en-US/#pt-BR, #2025-01-15, removes #enrich

# 3. Untag posts from Instagram saved
python3.11 .github/scripts/instagram/untag_reels.py
# → Removes posts from Instagram, removes #untag tag
```

**Example output after full workflow:**

```markdown
- [Trashy Clothing reimagines Palestinian hair salons](https://instagram.com/p/ABC/) #fashion #popculture #art @illeshamarie #en-US #2024-06-15
```

---

## Saved Reels

_(Posts will appear below as you run the scraping scripts)_
