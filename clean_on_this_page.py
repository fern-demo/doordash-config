import os

def clean_on_this_page_and_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    changed = False
    i = 0

    # Skip leading blank lines
    while i < len(lines) and lines[i].strip() == '':
        i += 1

    # Check for "On this page"
    if i < len(lines) and lines[i].strip().lower() == 'on this page':
        changed = True
        # Remove "On this page"
        lines.pop(i)
        # Remove any blank lines after
        while i < len(lines) and lines[i].strip() == '':
            lines.pop(i)
        # Remove the first header after "On this page"
        while i < len(lines):
            if lines[i].lstrip().startswith('#'):
                lines.pop(i)
                # Optionally remove blank lines after header
                while i < len(lines) and lines[i].strip() == '':
                    lines.pop(i)
                break
            i += 1

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Cleaned: {filepath}")

def walk_and_clean(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mdx') or filename.endswith('.md'):
                clean_on_this_page_and_header(os.path.join(dirpath, filename))

if __name__ == "__main__":
    # Change this to your docs root directory if needed
    walk_and_clean("fern/products/marketplace")
