import os

def rename_md_to_mdx(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, filename[:-3] + '.mdx')
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    # Change this to your target directory
    rename_md_to_mdx("fern/products/marketplace")