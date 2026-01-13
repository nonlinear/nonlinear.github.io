# Scripts Catalog

Automation scripts for content synchronization, media management, and development workflows.

## 📚 Literature & Content Sync

### sync_literature.py

**Purpose**: Synchronize literature library from Airtable to local MCP index
**Usage**: Keeps book database current for RAG-powered literature searches
**Run**: `python3 .github/scripts/sync_literature.py`

### sync_comics.py

**Purpose**: Download and organize comic book files from remote sources
**Usage**: Automated comic library management
**Run**: `python3 .github/scripts/sync_comics.py`

### missing_comics.py

**Purpose**: Identify gaps in comic collection
**Usage**: Audit tool to find missing issues or files
**Run**: `python3 .github/scripts/missing_comics.py`

## 📊 Airtable Integration

### airtable-sync.js

**Purpose**: General Airtable synchronization utility
**Usage**: Bidirectional sync between Airtable bases and local data
**Run**: `node .github/scripts/airtable-sync.js`

### sync_rot_airtable.js

**Purpose**: Sync ROT (Review of Things) data with Airtable
**Usage**: Specialized sync for review tracking system
**Run**: `node .github/scripts/sync_rot_airtable.js`

## 🖼️ Image & Media Management

### sync_inspiration_images.py

**Purpose**: Download and organize design inspiration images
**Usage**: Curate visual reference library
**Run**: `python3 .github/scripts/sync_inspiration_images.py`

### download_exercise_images.js

**Purpose**: Download exercise-related images from external sources
**Usage**: Populate exercise library with visuals
**Run**: `node .github/scripts/download_exercise_images.js`

### square_images.py

**Purpose**: Crop and resize images to square aspect ratio
**Usage**: Image preprocessing for consistent thumbnails
**Run**: `python3 .github/scripts/square_images.py`

### post_new_illos.py

**Purpose**: Post new illustrations to content management system
**Usage**: Automated illustration publishing workflow
**Run**: `python3 .github/scripts/post_new_illos.py`

## ⚙️ Development & System

### Sync_settings.py

**Purpose**: Synchronize VS Code settings across environments
**Usage**: Keep editor configuration consistent
**Run**: `python3 .github/scripts/Sync_settings.py`
**Note**: Available as VS Code task "🔄 Sync settings"

### Start_hugo.sh

**Purpose**: Start Hugo static site generator development server
**Usage**: Launch local Hugo preview
**Run**: `bash .github/scripts/Start_hugo.sh`

---

## Task Integration

Several scripts are integrated as VS Code tasks in `.vscode/tasks.json`:

- **🔄 Sync settings** → `Sync_settings.py`
- **🔄 Sync comics** → `sync_comics.py`

Run these via `Tasks: Run Task` command in VS Code.
