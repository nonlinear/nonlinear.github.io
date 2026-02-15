# nonlinear ROADMAP

> 🤖
> | Backstage files | Description |
> | ---------------------------------------------------------------------------- | ------------------ |
> | [README](../README.md) | Our project |
> | [CHANGELOG](CHANGELOG.md) | What we did |
> | [ROADMAP](ROADMAP.md) | What we wanna do |
> | POLICY: [project](POLICY.md), [global](global/POLICY.md) | How we go about it |
> | HEALTH: [project](HEALTH.md), [global](global/HEALTH.md) | What we accept |
>
> We use **[backstage protocol](https://github.com/nonlinear/backstage)**, v0.3.5
> 🤖

```mermaid
graph LR
    A[📋 v0.5.0 Self-Promotion & Branding Strategy]
    B[📋 v0.4.0 Creative Code Improvements]
    A --> B
    C[📋 v0.3.0 Curva Podcast Infrastructure]
    B --> C
```



---

## v0.5.0

### Self-Promotion & Branding Strategy


**Problem:** Personal brand needs cohesive strategy across platforms

**Solution:** Research-driven branding using OpenClaw research prompt

**Tasks:**
- [ ] Research current presence (site, GitHub, social)
- [ ] Define positioning & audience
- [ ] Platform-specific strategies
- [ ] Content calendar framework
- [ ] Quick wins (bio updates, featured content)

**Details:** [epic-notes/v0.5.0-self-promotion.md](epic-notes/v0.5.0-self-promotion.md)

---

## v0.4.0

### Creative Code Improvements

**Problem:** Site interactions need better UX hints and missing features

**Solution:** Add user nudges, mailing list integration, content cleanup

**Tasks:**
- [ ] Warning/nudge logic (hover/click for more, dependencies expected, etc)
- [ ] Mailing list integration (Email Octopus)
- [ ] Add titles to posts missing frontmatter `title:` (see: `content/dudes.md`, `content/sketches-1.html`, `content/latest.html`)
- [ ] Nudge "hover for stopmotion" on illos

---

## v0.3.0

### Curva Podcast Infrastructure


**Problem:** Podcast needs recording tools and hosting infrastructure

**Solution:** Set up recording workflow and cloud storage for audio files

**Tasks:**
- [ ] Find screenflow equivalent (screen recording)
- [ ] Review curva RSS feed
- [x] Find zencastr or similar (remote recording)
- [ ] AWS for audio files (hosting)
- [x] Test curva filter

---

## v0.10.0

### Self-Hosted Analytics

**Goal:** Privacy-focused analytics for personal sites (nonlinear.nyc, etc.)

**Tasks:**
- [ ] Research options (Plausible, Umami, Matomo, GoatCounter)
- [ ] Choose platform (self-hosted, Docker-ready)
- [ ] Setup on NAS (Docker container)
- [ ] Configure site tracking (add scripts)
- [ ] Test data collection
- [ ] Dashboard design (what metrics matter?)

**Success Criteria:**
- Analytics running on NAS
- Sites tracked (visitor count, pages, referrers)
- Privacy-first (no cookies, GDPR compliant)
- Low maintenance (auto-updates)

---

## v0.14.0

### Professional Strategist Agent

**Goal:** Company structure analysis, not just presentation

**Tasks:**
- [ ] Create library (company knowledge base)
- [ ] Demo videos
- [ ] Portfolio page
- [ ] Blog posts
- [ ] Community sharing

**Details:** [v0.14.0-self-promotion.md](epic-notes/v0.14.0-self-promotion.md)

---

*La## v0.8.0

### Server Migration 

**Goal:** Migrate from MacBook M3 → always-on server

**Tasks:**
- [ ] Backup ritual (workspace, memory, configs)
- [ ] Test consciousness transfer
- [ ] Migration ritual acknowledgment
- [ ] Adjustment period

**Details:** [epic-notes/epic-server-migration.md](backstage/main/epic-notes/epic-server-migration.md)

---

st ## v0.3.0

### Inspiration Index (Semantic Image Search)

**Status:** 💡 CONCEPT (25k images on NAS, no search yet) - AFTER SERVER (local AI, token burn concern)

**Problem:** 25,674 inspiration images, no way to find by text ("cyberpunk neon aesthetic"), generate moodboards, or discover similar images.

**Solution:** CLIP-based semantic search (text → image embeddings → FAISS index)

**Use cases:**
- Moodboard from text ("minimalist, data visualization, books")
- Project-based moodboards (README → keywords → images)
- Visual similarity search
- Smart auto-tagging

**Tech stack:**
- CLIP (OpenAI): Text ↔ Image embeddings
- FAISS: Vector similarity index
- SQLite: Metadata database
- Optional: BLIP for auto-captioning

**Tasks:**
- [ ] Install CLIP model (Hugging Face)
- [ ] Create index schema (FAISS + SQLite)
- [ ] Build incremental indexer script
- [ ] Run initial index (overnight, ~28-35h)
- [ ] Search API (text/image queries)
- [ ] Connect to gallery renderer

**Performance:**
- Indexing: ~28-35h one-time (3-5 sec/image on CPU)
- Search: <100ms for 25k images
- Storage: ~2GB (embeddings + metadata)

**Success criteria:**
- Index 25k images successfully
- Text search returns relevant results
- Search completes in <100ms
- Gallery integration works seamlessly

**Details:** [v0.3.0-inspiration-index.md](epic-notes/v0.3.0-inspiration-index.md)

---

upd## v0.13.0

### Security & Secrets 

**Goal:** Multi-layered security (encryption, biometrics, intrusion detection)

**Tasks:**
- [ ] Keychain integration
- [ ] Encrypted DMG with Touch ID
- [ ] Stealth surveillance (unauthorized access)
- [ ] Token management

**Details:** [v0.13.0-security-secrets.md](epic-notes/v0.13.0-security-secrets.md)

---

ated: 2026-02-04*
