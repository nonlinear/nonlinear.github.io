#!/bin/zsh
# Preview current file in Hugo server
# Usage: preview_in_hugo.sh <file_path>

FILE_PATH="$1"

# Remove 'content/' prefix and '.md' extension
URL_PATH=$(echo "$FILE_PATH" | sed 's|^content/||' | sed 's|\.md$||' | sed 's|\.html$||')

# Check if Hugo is running
if ! pgrep -f 'hugo serve' > /dev/null; then
    echo "Starting Hugo server..."
    nohup hugo serve -D > hugo.log 2>&1 &
    sleep 3
fi

# Open browser with the specific page
open "http://localhost:1313/$URL_PATH"
