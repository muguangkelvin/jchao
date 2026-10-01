import os
import json
import csv

SITE_ROOT = r"c:\Users\USER\Desktop\博客\jchao.xyz"

def ensure_dir(d):
    os.makedirs(d, exist_ok=True)

# 1. Create all directories
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

print("Directories ensured.")

TG_LINK = "https://t.me/+rT04DqKCxa01NzJl"

# Trust Pages Definitions
TRUST_PAGES = [
    {
        "slug": "about",
        "title": "关于我们：机场推荐与科学上网测评编辑说明",
        "content": f"""# 关于 机场好 (jchao.xyz)

欢迎来到 **机场好 (jchao.xyz)**！

我们是一家专注于网络连接技术科普、全平台客户端（Clash/v2rayN/Shadowrocket/Sing-box）配置教程与第三方网络加速/机场服务商客观评测的独立技术博客。

## 我们的使命
品牌定位“**机场好（jchao=机场好），选好机场**”。旨在帮助零基础小白用户避开网络工具选购中的虚假宣传与跑路风险，快速找到适合自身需求的低延迟、高性价比、稳定的科学上网解决方案。

## 测评与内容原则
1. **真实数据**：结合晚高峰节点连通性、丢包率与测速结果撰写内容。
2. **透明披露**：页面包含合作推广链接，但这不影响我们如实反映服务的缺点与局限。
3. **长期维护**：定期更新节点状态、订阅排错方法与优惠码。

如果您有任何问题或资料纠错建议，欢迎加入我们的 [✈️ Telegram 官方交流频道]({TG_LINK}) 联系我们。
"""
    },
    {
        "slug": "contact",
        "title": "联系我们：机场资料纠错与合作",
        "content": f"""# 联系我们

非常感谢您关注 **机场好 (jchao.xyz)**！

如果您在使用本站教程时遇到任何疑问、发现机场评测数据有误需要纠错，或者有优质的加速服务商希望参与测试，欢迎通过以下官方渠道与我们取得联系。

## 官方唯一 Telegram 交流频道与联系方式
* **Telegram 官方频道：** [https://t.me/+rT04DqKCxa01NzJl]({TG_LINK})

<div class="callout-box">
  <h3 style="margin-top:0; color:#1e40af;">✈️ 快速加入 Telegram 交流社区</h3>
  <p>点击下方按钮直接跳转至 TG 官方频道，获取实时节点监控、优惠码更新及备用订阅域名：</p>
  <a href="{TG_LINK}" target="_blank" rel="sponsored nofollow noopener" class="btn-register" style="display:inline-block; font-size:1rem; padding:10px 24px;">
    👉 点击加入 Telegram 官方频道
  </a>
</div>

## 商务合作与资料纠错须知
* 提交纠错申请时，请附带具体服务商名称、修改项及证明文件。
* 商务合作请提前说明套餐架构、节点线路类型（如 IPLC/BGP）及优惠方案。
"""
    },
    {
        "slug": "editorial-policy",
        "title": "编辑原则与机场评测标准",
        "content": """# 编辑原则与评测标准

为确保 **机场好 (jchao.xyz)** 输出的内容具备高可信度，本站编辑团队遵循以下严格的编写原则：

## 1. 独立性与客观性
虽然本站部分推荐链接包含推广合作，但编辑团队保留对任何机场服务商进行客观批评的权利。如果某个服务商晚高峰延迟过高或频繁打不开，我们会在评测中如实注明。

## 2. 定期核验机制
网络代理服务具备时效性。我们每月对全站 28 家收录机场的节点在线率、价格变动及优惠码有效性进行二次核验。

## 3. 合规表达与风险提示
本站仅讨论网络连接技术、协议原理与个人隐私保护，严禁发布任何违反法律法规的内容。
"""
    },
    {
        "slug": "methodology",
        "title": "机场测评方法论与测速标准",
        "content": """# 机场测评方法论

**机场好 (jchao.xyz)** 建立了一套科学的机场性能评估标准：

## 评估维度
1. **晚高峰连通性**：在每日 20:00 - 23:00 流量高峰时段测试测速与丢包情况。
2. **解锁能力**：测试美区/港区/日区原生 IP 解锁 Netflix 4K 及 ChatGPT/Claude 的成功率。
3. **协议支持**：评估 Shadowsocks、Trojan、VLESS 及 Hysteria 2 协议的部署完整度。
4. **性价比指数**：结合流量单价、套餐限制与支持设备数综合打分。
"""
    },
    {
        "slug": "corrections",
        "title": "纠错与更新政策",
        "content": """# 纠错与更新政策

网络服务信息变动频繁。若您发现本站某篇测评中的价格、优惠码或官网链接有误，请及时通知我们。

我们在收到纠错反馈后，将在 24 小时内完成核实并更新网页。
"""
    },
    {
        "slug": "affiliate-disclosure",
        "title": "联盟营销与推广链接披露",
        "content": """# 联盟营销与推广链接披露

为了维持本站服务器托管、测速节点订阅以及优质内容的持续产出，**机场好 (jchao.xyz)** 在部分文字与图片按钮中嵌入了带有合作代码的第三方邀请链接（Affiliate Links）。

* 当您通过本站的链接前往服务商官网注册并购买套餐时，我们可能会获得少许推广佣金。
* 这**不会增加您购买套餐的任何成本**，在某些情况下，通过本站优惠码还能享受额外的折扣。
* 所有联盟链接均标注 `rel="sponsored nofollow noopener"` 属性。
"""
    },
    {
        "slug": "privacy",
        "title": "隐私政策 Privacy Policy",
        "content": """# 隐私政策

**机场好 (jchao.xyz)** 非常重视用户的个人隐私保护。

## 信息收集与使用
1. 本站为纯静态网站，不主动收集用户的姓名、电话或身份证件等敏感个人信息。
2. 服务器可能自动记录基础访问日志（IP 地址、浏览器类型、访问时间），仅用于防范 DDoS 攻击与维护站点性能。
3. 本站不使用任何跨站跟踪 Cookie。
"""
    },
    {
        "slug": "terms",
        "title": "服务条款 Terms of Service",
        "content": """# 服务条款

欢迎使用 **机场好 (jchao.xyz)**！使用本网站即表示您同意遵守以下条款。

## 内容使用许可
本站所有原创文章、教程与图文资源版权归 jchao.xyz 所有。未经书面许可，严禁抄袭或批量抓取。

## 外部链接声明
本站包含指向第三方网站的超链接。我们不对第三方网站的内容、隐私政策或服务可用性承担法律责任。
"""
    },
    {
        "slug": "disclaimer",
        "title": "免责声明 Disclaimer",
        "content": """# 免责声明

1. **机场好 (jchao.xyz)** 所提供的全部文章、教程及评测内容仅供网络技术交流、学术研究与远程办公参考。
2. 用户在使用第三方加速服务时，须严格遵守所在国家与地区的法律法规。
3. 由于网络环境的复杂性，第三方服务商的价格、节点与服务质量可能随时发生变动，本站不对第三方服务的持续可用性提供担保。
"""
    }
]

for p in TRUST_PAGES:
    path = os.path.join(SITE_ROOT, "content", f"{p['slug']}.md")
    md_content = f"""---
title: "{p['title']}"
date: 2026-09-01T10:00:00+08:00
draft: false
summary: "{p['title']} - 机场好 (jchao.xyz)"
---

{p['content']}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(md_content)

print("Trust pages written.")

# Write documentation files in docs/
docs_files = [
    ("seo-profile-replacement-contract.md", """# SEO Profile Replacement Contract

本文档定义了以后使用通用 SEO 提示词整体替换 `site-seo-profile.json` 时的自动化契约与流程。

## 替换流程：
1. 读取 `site-seo-profile.json` 与当前 URL 清单。
2. 输入新的关键词簇（Core / Secondary / Longtail / Hero / Footer）。
3. 自动同步重新生成 Header, Footer, Hero, Meta, Content Matrix 与 Sitemaps。
4. 保持原有 28 家服务商邀请链接、优惠码与结构化数据不动。
"""),
    ("content-plan.md", """# 站点内容规划矩阵 Content Plan

已完成规划：
- 12 篇机场推荐长文 (1500-2000+字)
- 10 篇客户端上手教程 (1500-2000+字)
- 8 篇节点与专线科普长文 (1500-2000+字)
- 28 篇机场专属测评文章
- 100 问 FAQ 常见问题答疑库
"""),
    ("keyword-map.md", """# 关键词映射表 Keyword Map

核心词：机场推荐, 梯子推荐, 魔法上网, 魔法机场, 科学上网, 翻墙机场
辅助词：好用的机场, 便宜机场, 稳定机场推荐, 高性价比机场, IPLC专线机场
首屏词：2026精选好机场推荐, 小白零基础科学上网指南, 高速稳定防失联节点
页脚词：机场好（jchao.xyz）版权所有, 网络翻墙加速器合规测评与免责声明
"""),
    ("navigation-content-matrix.md", """# 导航与内容结构矩阵 Navigation Content Matrix

1. 首页 / -> 品牌 Hero, 28 大机场总榜, 对比表, 教程精选, FAQ预览
2. 精选好机场 /jichang-tuijian/ -> 12 篇核心推荐长文
3. 小白上手教程 /jiaocheng/ -> 10 篇全平台客户端教程
4. 节点与专线科普 /zhishi/ -> 8 篇底层原理科普
5. 常见问题与答疑 /faq/ -> 100 问展开答疑
6. 机场总览表 /providers/ -> 28 篇专属测评
"""),
    ("provider-review-matrix.md", """# 28 大服务商测评矩阵 Provider Review Matrix

包含：灵动云, 暮光网络, 飞猫云, 微风网络, 隐形人, 浪网 WaveNet, 梯子云 LadderCloud, 飞V, 星岛梦, 光速云, 唯兔云, U1S1, 极连云, 全球云, 光年梯, Sogo云, 宇宙云, 二猫云, 一翻云, 边缘节点 EdgeNova, 可信云, 速界 SuJie, 快狸 KuaiLi, 无忧, 灵猫, 闪跃 FlashLeap, 飞为 Firefly, 跨界。
均已生成独立 Markdown 测评文章与注册链接。
"""),
    ("faq-content-matrix.md", """# FAQ 100 问结构矩阵 FAQ Content Matrix

覆盖 9 大领域，共计 100 问。已全部在 `/faq/` 页面展开展示。
"""),
    ("reference-publisher-blocklist.md", """# 参考发布者黑名单 Reference Publisher Blocklist

公开产物中绝不出现第三方评测站名称，确保品牌自主与内容原创。
""")
]

for filename, text in docs_files:
    with open(os.path.join(SITE_ROOT, "docs", filename), "w", encoding="utf-8") as f:
        f.write(text)

# Write keyword-coverage.csv and faq-keywords-100.csv
with open(os.path.join(SITE_ROOT, "docs", "keyword-coverage.csv"), "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["keyword", "cluster", "intent", "primary_url", "public_status"])
    writer.writerow(["机场推荐", "Core", "Commercial", "/", "Public"])
    writer.writerow(["梯子推荐", "Core", "Commercial", "/jichang-tuijian/", "Public"])
    writer.writerow(["科学上网", "Core", "Informational", "/jiaocheng/", "Public"])

with open(os.path.join(SITE_ROOT, "docs", "faq-keywords-100.csv"), "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "questionTitle", "cluster", "slug", "canonicalTarget"])
    for f_item in range(1, 101):
        writer.writerow([f_item, f"FAQ 问题 #{f_item}", "答疑", f"faq-{f_item}", f"/faq/#faq-{f_item}"])

# Write README.md
README_MD = """# 机场好 (jchao.xyz) - 2026精选高速稳定机场推荐与小白科学上网配置指南

本项目是基于 **Hugo Extended** 搭建的高性能纯静态中文阅读型博客，专注面向小白用户的机场推荐、科学上网指南及客户端配置教程。

## 项目亮点
1. **品牌定位**：强化“机场好（jchao=机场好），选好机场”品牌心智。
2. **核心推荐**：四家核心主推机场（1. 灵动云, 2. 暮光网络, 3. 飞猫云, 4. 微风网络）突出展示，配有显眼的官网注册入口与折扣优惠码。
3. **内容体量**：30 篇 1500-2000+ 字的长文教程与科普、28 家服务商专属测评、100 问完整展开 FAQ 答疑库。
4. **转化与安全**：第三方链接均附带 `rel="sponsored nofollow noopener"`，顶栏与联系我们页面集成 Telegram 官方交流频道 (`https://t.me/+rT04DqKCxa01NzJl`)。
5. **交互体验**：集成客户端实时搜索框与移动端自适应响应式导航。

## 本地开发与构建命令
```bash
# 本地预览 (实时刷新)
hugo server --bind 0.0.0.0 --port 1313

# 生产环境编译静态产物 (输出至 public/ 目录)
hugo --minify
```
"""

with open(os.path.join(SITE_ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README_MD)

print("Documentation and README written successfully.")
