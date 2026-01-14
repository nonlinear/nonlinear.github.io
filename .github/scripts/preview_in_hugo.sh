#!/bin/zsh
# Preview current file in Hugo server (Simple Browser if in content/)
# Usage: preview_in_hugo.sh <file_path>

FILE_PATH="$1"

# Check if Hugo is running
if ! pgrep -f 'hugo serve' > /dev/null; then
    echo "Starting Hugo server..."
    nohup hugo serve -D > hugo.log 2>&1 &
    sleep 3
fi

# Check if file is in content/ (either as full path or relative)
IS_CONTENT=false
if [[ "$FILE_PATH" == content/* ]] || [[ -f "content/$FILE_PATH" ]]; then
    IS_CONTENT=true
fi

# Remove 'content/' prefix and '.md'/'.html' extension
URL_PATH=$(echo "$FILE_PATH" | sed 's|^content/||' | sed 's|\.md$||' | sed 's|\.html$||')

# If file is in content/, open in Simple Browser, else in default browser
if [[ "$IS_CONTENT" == true ]]; then
    open "vscode://github-enterprise.simple-browser/open?url=http://localhost:1313/$URL_PATH/"
else
    open "http://localhost:1313/$URL_PATH/"
fi
