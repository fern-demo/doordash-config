import os
import re

MEDIA_EXTENSIONS = (
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp",
    ".mp4", ".webm", ".mov", ".mp3", ".wav", ".ogg"
)

def remove_media_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # Remove markdown images: ![alt](url)
        line = re.sub(r'!\[.*?\]\(.*?\)', '', line)
        # Remove HTML <img ...>
        line = re.sub(r'<img[^>]*>', '', line)
        # Remove lines that are just a media URL (http or local)
        stripped = line.strip()
        if (stripped.lower().endswith(MEDIA_EXTENSIONS) and
            (stripped.startswith("http") or not stripped or not re.search(r'\w', stripped))):
            continue
        new_lines.append(line)

    if new_lines != lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Cleaned media: {filepath}")

def walk_and_clean_media(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mdx') or filename.endswith('.md'):
                remove_media_from_file(os.path.join(dirpath, filename))

if __name__ == "__main__":
    # Change this to your docs root directory if needed
    walk_and_clean_media("fern/products/")
