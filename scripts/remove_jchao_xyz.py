import glob
import re
import os

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = content
    replacements = [
        ("（jchao.xyz）", ""),
        ("(jchao.xyz)", ""),
        ("（jchao=机场好）", ""),
        ("(jchao=机场好)", ""),
        ("机场好 (jchao.xyz)", "机场好"),
        ("机场好（jchao.xyz）", "机场好"),
        ("关于 机场好 (jchao.xyz)", "关于 机场好"),
        ("关于 机场好（jchao.xyz）", "关于 机场好"),
    ]

    for old, new in replacements:
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {filepath}")

def main():
    # Clean layouts
    for root, dirs, files in os.walk('layouts'):
        for file in files:
            if file.endswith(('.html', '.json', '.xml')):
                clean_file(os.path.join(root, file))

    # Clean content
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                clean_file(os.path.join(root, file))

    # Clean data & scripts
    for root, dirs, files in os.walk('data'):
        for file in files:
            if file.endswith(('.json', '.yaml', '.toml')):
                clean_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
