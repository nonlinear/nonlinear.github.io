#!/usr/bin/env python3
"""
Find visually similar images (JPG/PNG) in static/images/illos, even if names differ.
Uses average hash (aHash) for fast, fuzzy matching.
Prints a report of likely duplicates.
"""
from pathlib import Path
from PIL import Image
import imagehash
from collections import defaultdict

ILLOS_DIR = Path(__file__).parent.parent.parent / "static" / "images" / "illos"

# Hamming distance threshold for similarity (lower = stricter, 5-10 is typical for aHash)
SIMILARITY_THRESHOLD = 6

def get_image_hash(path):
    try:
        with Image.open(path) as img:
            return imagehash.average_hash(img)
    except Exception as e:
        print(f"Error hashing {path.name}: {e}")
        return None

def main():
    image_files = list(ILLOS_DIR.glob("*.jpg")) + list(ILLOS_DIR.glob("*.png"))
    hashes = []
    print(f"🔍 Hashing {len(image_files)} images...")
    for path in image_files:
        h = get_image_hash(path)
        if h is not None:
            hashes.append((path.name, h))

    # Find similar pairs
    print("\n🔗 Looking for similar images (threshold: {}):\n".format(SIMILARITY_THRESHOLD))
    reported = set()
    markdown_lines = []
    pair_num = 1
    for i, (name1, hash1) in enumerate(hashes):
        for name2, hash2 in hashes[i+1:]:
            dist = hash1 - hash2
            if dist <= SIMILARITY_THRESHOLD:
                key = tuple(sorted([name1, name2]))
                if key not in reported:
                    line = (
                        f"{pair_num}. **{name1}** "
                        f'<img src="/images/illos/{name1}" alt="{name1}" height="200" width="200" />'
                        f"  |  **{name2}** "
                        f'<img src="/images/illos/{name2}" alt="{name2}" height="200" width="200" />'
                        f"  (distance: {dist})"
                    )
                    markdown_lines.append(line)
                    reported.add(key)
                    pair_num += 1
    if markdown_lines:
        # Write to project content/ directory, not static/content/
        project_root = ILLOS_DIR.parent.parent.parent
        md_path = project_root / "content" / "dedupe.md"
        md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w") as f:
            f.write(
                "---\n"
                "title: Possible Duplicate Illos\n"
                "date: 2025-12-11\n"
                "status: draft\n"
                "---\n\n"
            )
            f.write("# Possible Duplicate Illos\n\n")
            for line in markdown_lines:
                f.write(line + "\n")
        print(f"\n📝 Markdown report written to {md_path}")
    else:
        print("✅ No likely duplicates found.")

if __name__ == "__main__":
    main()
