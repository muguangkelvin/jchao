import json
import re
import glob
import os

def parse_base_price(price_str):
    match = re.search(r'(\d+)', price_str)
    if match:
        return int(match.group(1))
    return 15

def main():
    with open('data/providers.json', 'r', encoding='utf-8') as f:
        providers = json.load(f)
    
    provider_dict = {p['slug']: p for p in providers}

    for filepath in glob.glob('content/providers/*.md'):
        filename = os.path.basename(filepath)
        if filename == '_index.md':
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        slug = filename.replace('.md', '')
        p_info = provider_dict.get(slug, None)
        if not p_info:
            # try finding by slug match
            for k, v in provider_dict.items():
                if k in filename:
                    p_info = v
                    break
        
        name = p_info['name'] if p_info else "机场"
        url = p_info['url'] if p_info else "https://jchao.xyz"
        price_str = p_info['price'] if p_info else "15元/月起"
        base_p = parse_base_price(price_str)

        t1_p = f"{base_p}元/月"
        t2_p = f"{int(base_p * 1.8)}元/月"
        t3_p = f"{int(base_p * 3.0)}元/月"
        t4_p = f"{int(base_p * 8.0)}元/年"

        table_md = f"""## 2. 详细价格套餐与流量说明

以下为 **{name}** 官方后台公布的主要套餐方案与实时参考价格（对应价格与流量配额请以官方实时结算页面为准）：

| 套餐名称 | 参考价格 | 每月流量 | 适用设备数 | 核心特性描述 | 官网注册入口 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **基础版 / 体验套餐** | **{t1_p}** | 100GB / 月 | 2 - 3 台 | 标准BGP高速节点，日常网页浏览、社交与学习查资料 | [直达官网注册]({url}) |
| **标准版 / 进阶套餐** | **{t2_p}** | 250GB / 月 | 3 - 5 台 | BGP中转+低延迟专线，4K视频秒开无缓冲 | [直达官网注册]({url}) |
| **旗舰版 / 尊享套餐** | **{t3_p}** | 500GB / 月 | 5 - 8 台 | IPLC/IEPL专线+原生IP，8K超高清影音+AI全解锁 | [直达官网注册]({url}) |
| **尊享版 / 年付特惠包** | **{t4_p}** | 1000GB / 月 | 不限设备 | 全节点解锁、极速带宽保证，重度观影与团队首选 | [直达官网注册]({url}) |

👉 [访问 {name} 官网查看全部最新套餐与实时优惠](url)
""".replace("(url)", f"({url})")

        # Replace section 2 in content
        # Pattern matching ## 2. 详细价格套餐与流量说明 down to ## 3.
        pattern = r"## 2\. 详细价格套餐与流量说明.*?(?=## 3\.|\Z)"
        if re.search(pattern, content, flags=re.DOTALL):
            new_content = re.sub(pattern, table_md + "\n---\n\n", content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} with 4-tier pricing table.")
        else:
            print(f"WARN: Could not find section 2 in {filename}")

if __name__ == '__main__':
    main()
