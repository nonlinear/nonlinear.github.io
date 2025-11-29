import os
import shutil

src = "/media/backup/immich-donttouch/254eb16f-767b-492a-a239-21e193b1c12f"
dst = "/media/backup/personal/immich"

# Recursively find all files
all_files = []
for root, dirs, files in os.walk(src):
    for file in files:
        all_files.append(os.path.join(root, file))

# Copy in chunks of 500
chunk_size = 500
for i in range(0, len(all_files), chunk_size):
    chunk_folder = os.path.join(dst, f"{i//chunk_size+1:03d}")
    os.makedirs(chunk_folder, exist_ok=True)
    for f in all_files[i:i+chunk_size]:
        shutil.copy2(f, chunk_folder)
