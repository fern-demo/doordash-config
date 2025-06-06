import os

def clean_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the first line that starts with [Previous or [Next
    cut_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('[Previous') or line.strip().startswith('[Next'):
            cut_idx = i
            break

    if cut_idx is not None:
        lines = lines[:cut_idx]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Cleaned: {filepath}")

def walk_and_clean(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mdx') or filename.endswith('.md'):
                filepath = os.path.join(dirpath, filename)
                clean_markdown_file(filepath)

if __name__ == "__main__":
    # Set this to the root directory where your markdown files are
    walk_and_clean("fern/products/marketplace") 