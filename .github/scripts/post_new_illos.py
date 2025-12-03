#!/usr/bin/env python3
"""
Convert video files (MOV, MP4) to WebP format
Processes videos from internal/illustrations to add/
Outputs to static/images/illos/
"""

import os
import subprocess
import glob
from pathlib import Path

# Configuration
INPUT_FOLDER = "internal/illustrations to add"
OUTPUT_FOLDER = "static/images/illos"
VIDEO_EXTENSIONS = ["*.mp4", "*.MP4", "*.mov", "*.MOV"]

# WebP conversion settings (matched to existing files)
# Quality: 0-100 (higher is better quality)
QUALITY = 80
# Compression: 0-6 (higher is slower but better compression)
COMPRESSION = 4
# Max dimensions (maintains aspect ratio) - existing files are 512x512
MAX_WIDTH = 512
MAX_HEIGHT = 512
# Frame rate for animated WebP - existing files use 25fps
FPS = 25
# Speed multiplier (1.0 = original, 1.5 = 50% faster, 2.0 = 2x faster)
SPEED = 1.5

def ensure_output_dir():
    """Create output directory if it doesn't exist"""
    output_path = Path(OUTPUT_FOLDER)
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directory: {OUTPUT_FOLDER}")

def get_video_files():
    """Get all video files from input folder"""
    video_files = []
    input_path = Path(INPUT_FOLDER)

    if not input_path.exists():
        print(f"❌ Input folder not found: {INPUT_FOLDER}")
        return []

    for ext in VIDEO_EXTENSIONS:
        video_files.extend(input_path.glob(ext))

    return sorted(video_files)

def get_unique_filename(base_path, extension):
    """Generate unique filename by adding -1, -2, etc if file exists"""
    output_path = Path(OUTPUT_FOLDER) / f"{base_path.stem}{extension}"

    if not output_path.exists():
        return output_path

    # File exists, add counter
    counter = 1
    while True:
        output_path = Path(OUTPUT_FOLDER) / f"{base_path.stem}-{counter}{extension}"
        if not output_path.exists():
            return output_path
        counter += 1

def extract_first_frame_jpeg(input_file):
    """Extract first frame as JPEG using ffmpeg"""
    input_path = Path(input_file)
    output_path = get_unique_filename(input_path, ".jpg")
    output_filename = output_path.name

    print(f"  ⚙ Extracting first frame → {output_filename}")

    # FFmpeg command to extract first frame as JPEG
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-vf", f"scale='min({MAX_WIDTH},iw)':min'({MAX_HEIGHT},ih)':force_original_aspect_ratio=decrease",
        "-frames:v", "1",  # Extract only first frame
        "-q:v", "2",  # JPEG quality (2-31, lower is better)
        "-y",
        str(output_path)
    ]

    try:
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        print(f"  ✓ JPEG created: {output_filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to extract frame")
        return False

def convert_video_to_webp(input_file):
    """Convert a single video file to WebP using ffmpeg"""
    input_path = Path(input_file)
    output_path = get_unique_filename(input_path, ".webp")
    output_filename = output_path.name

    print(f"  ⚙ Converting to WebP → {output_filename}")

    # FFmpeg command for video to animated WebP
    # setpts: speed up video (1.5x = divide PTS by 1.5)
    # fps: set output frame rate
    # scale: resize to fit within max dimensions maintaining aspect ratio
    # loop 0: infinite loop
    # quality: WebP quality (0-100)
    # compression_level: WebP compression (0-6)
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-vf", f"setpts={1/SPEED}*PTS,fps={FPS},scale='min({MAX_WIDTH},iw)':min'({MAX_HEIGHT},ih)':force_original_aspect_ratio=decrease",
        "-loop", "0",
        "-quality", str(QUALITY),
        "-compression_level", str(COMPRESSION),
        "-y",  # Overwrite output file if exists
        str(output_path)
    ]

    try:
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        print(f"  ✓ WebP created: {output_filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to convert to WebP")
        print(f"     Error: {e.stderr.decode('utf-8')[:200]}")
        return False
    except FileNotFoundError:
        print("❌ ffmpeg not found. Please install ffmpeg:")
        print("   brew install ffmpeg")
        return False

def main():
    """Main conversion process"""
    print("=" * 60)
    print("Video to WebP Converter")
    print("=" * 60)
    print()

    # Check ffmpeg availability
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("✓ ffmpeg found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg not found. Install with: brew install ffmpeg")
        return

    print()

    # Setup
    ensure_output_dir()
    video_files = get_video_files()

    if not video_files:
        print(f"❌ No video files found in {INPUT_FOLDER}")
        return

    print(f"✓ Found {len(video_files)} video file(s)")
    print()

    # Convert each video
    success_count = 0
    failed_count = 0
    total = len(video_files)

    for idx, video_file in enumerate(video_files, 1):
        print(f"[{idx}/{total}] Processing: {video_file.name}")

        # Extract first frame as JPEG
        jpeg_success = extract_first_frame_jpeg(video_file)

        # Convert to animated WebP
        webp_success = convert_video_to_webp(video_file)

        if jpeg_success and webp_success:
            success_count += 1
        else:
            failed_count += 1
        print()

    # Summary
    print("=" * 60)
    print(f"Conversion complete!")
    print(f"✓ Successful: {success_count}")
    if failed_count > 0:
        print(f"❌ Failed: {failed_count}")
    print(f"📁 Output: {OUTPUT_FOLDER}")
    print("=" * 60)

if __name__ == "__main__":
    main()
