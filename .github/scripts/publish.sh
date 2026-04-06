#!/bin/bash
# Automated publish script for nonlinear.github.io
# Ensures Hugo builds to docs/ and commits/pushes correctly

set -e  # Exit on error

echo "🔨 Building Hugo with docs output..."
rm -rf resources/_gen
hugo --config config.toml -d docs

echo "📦 Staging docs changes..."
git add docs

echo "💬 Committing..."
git commit -m "rebuild: hugo publish to docs" || echo "No changes to commit"

echo "🚀 Pushing to main..."
git push origin main

echo "✅ Publish complete!"
