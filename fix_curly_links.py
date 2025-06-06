import os
import re

def fix_curly_braces_in_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace {var} with {"{var}"} in markdown links
    def replacer(match):
        text, url = match.group(1), match.group(2)
        # Replace {var} with {"{var}"} in both text and url
        def curly_repl(m):
            return '{"{' + m.group(1) + '}"}'
        new_text = re.sub(r'\{([a-zA-Z0-9_]+)\}', curly_repl, text)
        new_url = re.sub(r'\{([a-zA-Z0-9_]+)\}', curly_repl, url)
        return f'[{new_text}]({new_url})'

    new_content = re.sub(r'\[([^\]]*?)\]\(([^)]+)\)', replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed curly braces in links: {filepath}")

def walk_and_fix(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mdx') or filename.endswith('.md'):
                fix_curly_braces_in_links(os.path.join(dirpath, filename))

if __name__ == "__main__":
    # Change this to your docs root directory
    walk_and_fix("fern/products/marketplace")
