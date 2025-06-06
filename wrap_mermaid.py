import os

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
                # Stop if we hit another code block
                if lines[j].strip() == "```":
                    j += 1
                    break
                # Stop if we hit a blank line followed by a non-diagram line (optional, can be removed for more aggressive wrapping)
                if lines[j].strip() == "" and (j+1 >= len(lines) or not lines[j+1].strip()):
                    new_lines.append(lines[j])
                    j += 1
                    break
                new_lines.append(lines[j])
                j += 1
            # Always close the code block
            if not new_lines[-1].strip() == "```":
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
    process_all_files("fern/products/drive")
