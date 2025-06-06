import os
import re

def fix_autolinks_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <http://...> or <https://...> with [http://...](http://...)
    def replacer(match):
        url = match.group(1)
        # Remove trailing punctuation from inside the link, but keep it outside
        m = re.match(r'(.+?)([.,;:!?)]*)$', url)
        if m:
            clean_url, trailing = m.groups()
            return f'[{clean_url}]({clean_url}){trailing}'
        return f'[{url}]({url})'

    new_content = re.sub(r'<(https?://[^ >]+)>', replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed autolinks in: {filepath}")

def walk_and_fix(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mdx') or filename.endswith('.md'):
                fix_autolinks_in_file(os.path.join(dirpath, filename))

if __name__ == "__main__":
    # Change this to your docs root directory
    walk_and_fix("fern/products/marketplace")