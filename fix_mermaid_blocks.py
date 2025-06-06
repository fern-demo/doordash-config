import os
import re

# Mermaid block starters
MERMAID_STARTERS = [
    'graph TD', 'graph LR', 'sequenceDiagram', 'classDiagram', 'stateDiagram', 'erDiagram', 'journey', 'gantt', 'pie'
]

def is_mermaid_start(line):
    return any(line.strip().startswith(starter) for starter in MERMAID_STARTERS)

def wrap_mermaid_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_mermaid = False
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect start of a Mermaid block
        if is_mermaid_start(line):
            # Check if already wrapped
            if i > 0 and lines[i-1].strip() == "```mermaid":
                # Already wrapped, just copy lines until end of block
                new_lines.append(line)
                i += 1
                while i < len(lines) and lines[i].strip() != "```":
                    new_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    new_lines.append(lines[i])  # add closing ```
                    i += 1
            else:
                # Not wrapped, so wrap it
                new_lines.append("```mermaid\n")
                while i < len(lines) and (lines[i].strip() == "" or is_mermaid_start(lines[i]) or re.match(r'^[A-Za-z0-9_\-\[\]\(\)\{\}\|><=:. /\'\"]+$', lines[i].strip())):
                    new_lines.append(lines[i])
                    i += 1
                new_lines.append("```\n")
        else:
            new_lines.append(line)
            i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def fix_broken_mermaid_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        # Look for the broken pattern: ```mermaid, graph TD, ```, then diagram lines
        if (
            i + 2 < len(lines)
            and lines[i].strip() == "```mermaid"
            and lines[i+1].strip().startswith("graph")
            and lines[i+2].strip() == "```"
        ):
            # Start a new mermaid block
            new_lines.append("```mermaid\n")
            new_lines.append(lines[i+1])  # graph TD or similar

            # Collect all subsequent diagram lines
            j = i + 3
            while j < len(lines):
                # Stop if we hit another code block or a blank line followed by non-diagram
                if lines[j].strip() == "```":
                    j += 1
                    break
                new_lines.append(lines[j])
                j += 1
            new_lines.append("```\n")
            i = j
        else:
            new_lines.append(lines[i])
            i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def process_all_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md') or filename.endswith('.mdx'):
                filepath = os.path.join(dirpath, filename)
                fix_broken_mermaid_blocks(filepath)
                print(f"Fixed: {filepath}")

if __name__ == "__main__":
    # Change this to your docs root directory
    process_all_files("fern/products/drive")
