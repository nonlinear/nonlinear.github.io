import os
import glob
import xml.etree.ElementTree as ET
import json

# Pasta onde estão os snippets do Sublime
input_folder = "sublime_snippets"
output_file = "zed_snippets.json"

snippets = {}

for filepath in glob.glob(os.path.join(input_folder, "**/*.sublime-snippet"), recursive=True):
    tree = ET.parse(filepath)
    root = tree.getroot()

    content = root.find('content').text.strip()
    body = content.splitlines()

    tab_trigger = root.find('tabTrigger').text.strip() if root.find('tabTrigger') is not None else 'snippet'
    description = root.find('description').text.strip() if root.find('description') is not None else os.path.basename(filepath)

    snippets[description] = {
        "prefix": tab_trigger,
        "body": body,
        "description": description
    }

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(snippets, f, indent=2, ensure_ascii=False)

print(f"Converted {len(snippets)} snippets to {output_file}")
