#!/usr/bin/env python3
import sys
import json

url = sys.argv[1] if len(sys.argv) > 1 else ""
command = {
    "command": "simpleBrowser.show",
    "args": [url]
}
print(json.dumps(command))
