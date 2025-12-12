#!/usr/bin/env python3
"""
Convert video files (MOV/MP4) to WebP animations and JPEG thumbnails.
Accelerates videos 1.5x and generates unique filenames if conflicts occur.
"""
import subprocess
from pathlib import Path
import re

# Paths
SOURCE_DIR = Path(__file__).parent.parent.parent / "internal" / "illustrations to add"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "static" / "images" / "illos"

def get_unique_filename(path):
    """Generate unique filename by adding -1, -2, etc. if file exists"""
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1

    while True:
        new_path = parent / f"{stem}-{counter}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1

def extract_first_frame_jpeg(video_path, output_path):
    """Extract first frame as JPEG thumbnail"""
    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-frames:v", "1",
        "-q:v", "2",
        str(output_path)
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def convert_video_to_webp(video_path, output_path):
    """Convert video to WebP with 1.5x speed"""
    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-vf", "setpts=0.666667*PTS,fps=25,scale=512:512:force_original_aspect_ratio=decrease,pad=512:512:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libwebp",
        "-quality", "80",
        "-compression_level", "4",
        str(output_path)
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Find all video files
    video_files = list(SOURCE_DIR.glob("*.mov")) + list(SOURCE_DIR.glob("*.MOV")) + \
                  list(SOURCE_DIR.glob("*.mp4")) + list(SOURCE_DIR.glob("*.MP4"))

    if not video_files:
        print("No video files found in", SOURCE_DIR)
        return

    total = len(video_files)
    print(f"Found {total} video file(s) to process\n")

    new_base_names = []
    for idx, video_path in enumerate(video_files, 1):
        print(f"[{idx}/{total}] Processing: {video_path.name}")

        # Generate output paths
        base_name = re.sub(r'\s+', '-', video_path.stem.lower())
        webp_path = get_unique_filename(OUTPUT_DIR / f"{base_name}.webp")
        jpeg_path = get_unique_filename(OUTPUT_DIR / f"{base_name}.jpg")

        try:
            # Convert to WebP
            print(f"  → Converting to WebP: {webp_path.name}")
            convert_video_to_webp(video_path, webp_path)

            # Extract JPEG thumbnail
            print(f"  → Extracting JPEG: {jpeg_path.name}")
            extract_first_frame_jpeg(video_path, jpeg_path)

            # Add base name to list for post addition
            new_base_names.append(base_name)

            # Delete original video file
            try:
                video_path.unlink()
                print(f"  🗑️ Deleted source: {video_path.name}")
            except Exception as del_err:
                print(f"  ⚠️ Could not delete {video_path.name}: {del_err}")

            print(f"  ✅ Done\n")

        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error: {e}\n")
            continue

    print(f"✨ Processed {total} file(s)")
    if new_base_names:
        print("\nNew files (add to posts):")
        for name in new_base_names:
            print(f"- {name}")

if __name__ == "__main__":
    main()
