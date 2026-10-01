import os
import json
import re

SITE_ROOT = r"c:\Users\USER\Desktop\博客\jchao.xyz"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

# 1. Directories setup
dirs = [
    os.path.join(SITE_ROOT, "content"),
    os.path.join(SITE_ROOT, "content", "jichang-tuijian"),
    os.path.join(SITE_ROOT, "content", "jiaocheng"),
    os.path.join(SITE_ROOT, "content", "zhishi"),
    os.path.join(SITE_ROOT, "content", "faq"),
    os.path.join(SITE_ROOT, "content", "providers"),
    os.path.join(SITE_ROOT, "data"),
    os.path.join(SITE_ROOT, "docs"),
    os.path.join(SITE_ROOT, "layouts"),
    os.path.join(SITE_ROOT, "layouts", "_default"),
    os.path.join(SITE_ROOT, "layouts", "partials"),
    os.path.join(SITE_ROOT, "layouts", "faq"),
    os.path.join(SITE_ROOT, "layouts", "jichang-tuijian"),
    os.path.join(SITE_ROOT, "layouts", "providers"),
    os.path.join(SITE_ROOT, "static"),
    os.path.join(SITE_ROOT, "static", "css"),
    os.path.join(SITE_ROOT, "static", "js"),
    os.path.join(SITE_ROOT, "scripts")
]

for d in dirs:
    ensure_dir(d)

print("Directories created.")
