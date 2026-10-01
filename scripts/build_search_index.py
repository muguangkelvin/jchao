import json
import glob
import re
import os

def generate_search_index_js():
    search_data = []

    # Alias dictionary for smart association
    alias_map = {
        "clash": "Clash, Clash Verge, Clash Meta, OpenClash, 节点配置, 订阅导入, 规则模式",
        "shadowrocket": "Shadowrocket, 小火箭, iOS, iPhone, iPad, 苹果翻墙, 节点导入",
        "singbox": "Sing-box, Singbox, Hysteria 2, VLESS, 最新协议",
        "android": "Android, 安卓, 手机翻墙, v2rayNG, Surfboard, 客户端教程",
        "windows": "Windows, 电脑翻墙, Clash for Windows, v2rayN",
        "mac": "macOS, Mac, ClashX, Surge",
        "iplc": "IPLC, IEPL, 内网专线, 游戏加速, 低延迟, 零丢包, 晚高峰不卡顿",
        "bgp": "BGP, 中转线路, 公网直连, 优化出口",
        "cheap": "便宜机场, 高性价比, 低价梯子, 7元月付, 84元包年",
        "monthly": "月付, 按月付费, 防跑路, 灵活订阅",
        "heavy": "大流量, 1000GB, 4K影音, 8K超高清, Steam下载",
        "unblock": "ChatGPT 4o, Claude 3.5, Gemini, Netflix, Disney+, TikTok, 原生IP解锁",
        "faq": "节点超时, 连不上, 订阅失败, 无法更新, 拔线跑路, 防封锁, 错误排错"
    }

    for filepath in glob.glob('content/**/*.md', recursive=True):
        filename = os.path.basename(filepath)
        if filename in ['_index.md']:
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()

        title_match = re.search(r'title:\s*["\']?(.*?)["\']?\n', raw)
        desc_match = re.search(r'description:\s*["\']?(.*?)["\']?\n', raw)
        summary_match = re.search(r'summary:\s*["\']?(.*?)["\']?\n', raw)

        # Extract tags and categories
        tags_match = re.search(r'tags:\s*\[(.*?)\]', raw)
        cats_match = re.search(r'categories:\s*\[(.*?)\]', raw)

        tags = tags_match.group(1).replace('"', '').replace("'", "") if tags_match else ""
        cats = cats_match.group(1).replace('"', '').replace("'", "") if cats_match else ""

        title = title_match.group(1) if title_match else filename.replace('.md', '')
        desc = desc_match.group(1) if desc_match else ""
        summary = summary_match.group(1) if summary_match else ""

        body_content = re.sub(r'---.*?---', '', raw, flags=re.DOTALL)
        body_plain = re.sub(r'[#*`\[\]\(\)|]', ' ', body_content)
        body_plain = re.sub(r'\s+', ' ', body_plain).strip()

        rel_dir = os.path.dirname(filepath).replace('content\\', '').replace('content/', '')
        slug = filename.replace('.md', '')

        if rel_dir == 'providers':
            permalink = f"/providers/{slug}/index.html"
            section = "providers"
        elif rel_dir == 'jichang-tuijian':
            permalink = f"/jichang-tuijian/{slug}/index.html"
            section = "jichang-tuijian"
        elif rel_dir == 'jiaocheng':
            permalink = f"/jiaocheng/{slug}/index.html"
            section = "jiaocheng"
        elif rel_dir == 'zhishi':
            permalink = f"/zhishi/{slug}/index.html"
            section = "zhishi"
        elif rel_dir == 'faq':
            permalink = f"/faq/{slug}/index.html"
            section = "faq"
        else:
            permalink = f"/{slug}/index.html"
            section = "general"

        # Generate keyword associations
        assoc_list = [tags, cats]
        for key, aliases in alias_map.items():
            if key in raw.lower() or key in title.lower() or key in slug.lower():
                assoc_list.append(aliases)

        keywords_str = " ".join(assoc_list)

        search_data.append({
            "title": title,
            "permalink": permalink,
            "section": section,
            "description": desc,
            "summary": summary if summary else desc,
            "keywords": keywords_str,
            "contents": body_plain[:800]  # Store first 800 chars of plain text for deep matching
        })

    os.makedirs('static/js', exist_ok=True)
    js_content = f"window.SITE_SEARCH_INDEX = {json.dumps(search_data, ensure_ascii=False, indent=2)};"

    with open('static/js/search-index.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Successfully generated static/js/search-index.js with {len(search_data)} enriched search items.")

if __name__ == '__main__':
    generate_search_index_js()
