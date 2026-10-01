import os
import json
import csv

SITE_ROOT = r"c:\Users\USER\Desktop\博客\jchao.xyz"

def ensure_dir(d):
    os.makedirs(d, exist_ok=True)

# 1. Directories
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

# 2. Config hugo.toml
CONFIG_TOML = """baseURL = "https://jchao.xyz/"
languageCode = "zh-cn"
title = "机场好 (jchao.xyz) - 2026精选高速稳定机场推荐与小白科学上网配置指南"
theme = ""
summaryLength = 120
enableRobotsTXT = true

[outputs]
  home = ["HTML", "RSS", "JSON"]
  page = ["HTML"]
  section = ["HTML", "RSS"]

[taxonomies]
  category = "categories"
  tag = "tags"

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.tableOfContents]
    startLevel = 2
    endLevel = 4
    ordered = false

[params]
  description = "机场好 (jchao.xyz) 是面向小白用户的科学上网与机场推荐指南站。提供2026便宜稳定IPLC专线机场测评、Clash/Shadowrocket/Sing-box全平台配置教程与节点订阅排错答疑。"
  keywords = "机场推荐, 梯子推荐, 魔法上网, 魔法机场, 科学上网, 翻墙机场, 便宜机场, 稳定机场推荐, IPLC专线机场, 翻墙软件"
  tgChannel = "https://t.me/+rT04DqKCxa01NzJl"
"""

with open(os.path.join(SITE_ROOT, "hugo.toml"), "w", encoding="utf-8") as f:
    f.write(CONFIG_TOML)

with open(os.path.join(SITE_ROOT, "config.toml"), "w", encoding="utf-8") as f:
    f.write(CONFIG_TOML)

# 3. CSS
STYLE_CSS = """/* Yue Theme Inspired Clean & Modern Stylesheet */
:root {
  --primary: #2563eb;
  --primary-hover: #1d4ed8;
  --accent: #dc2626;
  --accent-hover: #b91c1c;
  --success: #16a34a;
  --bg: #f8fafc;
  --surface: #ffffff;
  --text: #0f172a;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --radius: 10px;
  --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans CH", sans-serif;
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--primary); text-decoration: none; transition: color 0.2s; }
a:hover { color: var(--primary-hover); }

.container {
  max-width: 1180px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header */
header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 10px;
}
.brand-logo {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--primary);
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.brand-tagline {
  font-size: 0.85rem;
  color: var(--text-muted);
  display: none;
}
@media(min-width: 768px) { .brand-tagline { display: inline-block; } }

nav.main-nav {
  display: flex;
  gap: 18px;
}
nav.main-nav a {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text);
  padding: 6px 10px;
  border-radius: 6px;
}
nav.main-nav a:hover, nav.main-nav a.active {
  background-color: #eff6ff;
  color: var(--primary);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-box {
  position: relative;
}
.search-input {
  padding: 8px 14px;
  border: 1px solid var(--border);
  border-radius: 20px;
  font-size: 0.85rem;
  width: 180px;
  transition: width 0.3s, border-color 0.3s;
}
.search-input:focus {
  outline: none;
  width: 230px;
  border-color: var(--primary);
}

.btn-tg-header {
  background-color: #0088cc;
  color: #ffffff !important;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 7px 14px;
  border-radius: 20px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 2px 4px rgba(0,136,204,0.2);
}
.btn-tg-header:hover {
  background-color: #0077b5;
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--text);
}

@media(max-width: 900px) {
  nav.main-nav { display: none; }
  nav.main-nav.open {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    background: var(--surface);
    padding: 15px 20px;
    border-bottom: 1px solid var(--border);
    box-shadow: var(--shadow-lg);
  }
  .menu-toggle { display: block; }
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
  color: #ffffff;
  padding: 50px 0 45px;
  text-align: center;
  border-bottom: 4px solid #3b82f6;
}
.hero-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.18);
  padding: 6px 16px;
  border-radius: 30px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 16px;
  letter-spacing: 0.5px;
}
.hero h1 {
  font-size: 2.2rem;
  font-weight: 900;
  line-height: 1.3;
  margin-bottom: 18px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}
.hero-cluster-text {
  font-size: 1.05rem;
  line-height: 1.8;
  max-width: 850px;
  margin: 0 auto 24px;
  color: #e0f2fe;
  background: rgba(0, 0, 0, 0.15);
  padding: 14px 20px;
  border-radius: 8px;
  border-left: 4px solid #60a5fa;
  text-align: left;
}
.hero-actions {
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
}
.btn-hero-main {
  background: #f59e0b;
  color: #0f172a !important;
  font-weight: 800;
  padding: 12px 28px;
  border-radius: 8px;
  font-size: 1rem;
  box-shadow: 0 4px 10px rgba(245, 158, 11, 0.4);
}
.btn-hero-main:hover { background: #d97706; }
.btn-hero-sub {
  background: rgba(255,255,255,0.2);
  color: #ffffff !important;
  font-weight: 700;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 1rem;
  border: 1px solid rgba(255,255,255,0.4);
}
.btn-hero-sub:hover { background: rgba(255,255,255,0.3); }

/* Main Layout Grid */
.layout-grid {
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 30px;
  margin: 40px 0;
}
@media(max-width: 960px) {
  .layout-grid { grid-template-columns: 1fr; }
}

.section-title {
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.provider-card-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.provider-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 22px;
  box-shadow: var(--shadow);
  display: grid;
  grid-template-columns: 80px 1fr auto;
  gap: 20px;
  align-items: center;
  position: relative;
  transition: transform 0.2s, box-shadow 0.2s;
}
.provider-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.provider-card.top-4 {
  border: 2px solid #3b82f6;
  background: linear-gradient(180deg, #ffffff 0%, #f0f7ff 100%);
}
.rank-badge {
  background: #3b82f6;
  color: #fff;
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 900;
}
.top-4 .rank-badge {
  background: linear-gradient(135deg, #dc2626, #f59e0b);
}
.rank-num { font-size: 1.4rem; line-height: 1; }
.rank-label { font-size: 0.65rem; text-transform: uppercase; margin-top: 2px; }

.provider-info h3 {
  font-size: 1.25rem;
  margin-bottom: 6px;
}
.provider-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin: 6px 0;
}
.tag {
  background: #e2e8f0;
  color: #334155;
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 600;
}
.tag.tag-ai { background: #dbeafe; color: #1e40af; }
.tag.tag-coupon { background: #fef3c7; color: #92400e; }

.provider-meta-row {
  display: flex;
  gap: 16px;
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-top: 6px;
}

.provider-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-width: 140px;
}

/* EYE-CATCHING REGISTER BUTTON */
.btn-register {
  background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
  color: #ffffff !important;
  font-weight: 800;
  font-size: 0.95rem;
  text-align: center;
  padding: 10px 16px;
  border-radius: 6px;
  box-shadow: 0 4px 8px rgba(220, 38, 38, 0.3);
  transition: transform 0.2s, background 0.2s;
  display: block;
}
.btn-register:hover {
  background: linear-gradient(135deg, #b91c1c 0%, #dc2626 100%);
  transform: scale(1.03);
}

.btn-detail {
  background: #f1f5f9;
  color: #334155 !important;
  font-weight: 600;
  font-size: 0.85rem;
  text-align: center;
  padding: 8px 14px;
  border-radius: 6px;
  border: 1px solid var(--border);
}
.btn-detail:hover { background: #e2e8f0; }

@media(max-width: 650px) {
  .provider-card {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .rank-badge { margin: 0 auto; }
  .provider-meta-row { justify-content: center; flex-wrap: wrap; }
  .provider-actions { flex-direction: row; justify-content: center; }
}

.table-responsive {
  overflow-x: auto;
  margin: 20px 0;
  background: var(--surface);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}
table.cmp-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.9rem;
}
table.cmp-table th, table.cmp-table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
}
table.cmp-table th {
  background: #f1f5f9;
  font-weight: 700;
  color: var(--text);
}
table.cmp-table tr:hover { background: #f8fafc; }

.article-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.article-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s;
}
.article-card:hover { transform: translateY(-3px); }
.article-card h4 {
  font-size: 1.1rem;
  margin-bottom: 10px;
  line-height: 1.4;
}
.article-summary {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 14px;
}
.article-meta {
  font-size: 0.78rem;
  color: #94a3b8;
  display: flex;
  justify-content: space-between;
}

.widget {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: var(--shadow);
}
.widget-title {
  font-size: 1.1rem;
  font-weight: 800;
  margin-bottom: 14px;
  padding-bottom: 6px;
  border-bottom: 2px solid var(--primary);
}
.widget-list { list-style: none; }
.widget-list li {
  padding: 8px 0;
  border-bottom: 1px dashed var(--border);
  font-size: 0.9rem;
}
.widget-list li:last-child { border-bottom: none; }

.article-header {
  margin-bottom: 30px;
  text-align: center;
}
.article-header h1 {
  font-size: 2.1rem;
  line-height: 1.3;
  margin-bottom: 14px;
  color: #0f172a;
}
.article-meta-header {
  font-size: 0.85rem;
  color: var(--text-muted);
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.article-body {
  font-size: 1.05rem;
  line-height: 1.85;
  color: #1e293b;
  background: var(--surface);
  padding: 35px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}
.article-body h2 {
  font-size: 1.5rem;
  margin: 32px 0 16px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border);
  color: #0f172a;
}
.article-body h3 {
  font-size: 1.25rem;
  margin: 24px 0 12px;
  color: #1e293b;
}
.article-body p { margin-bottom: 18px; }
.article-body ul, .article-body ol { margin: 0 0 18px 24px; }
.article-body li { margin-bottom: 6px; }

.callout-box {
  background: #eff6ff;
  border-left: 4px solid var(--primary);
  padding: 16px 20px;
  margin: 20px 0;
  border-radius: 0 8px 8px 0;
  font-size: 0.95rem;
}
.callout-box.warning {
  background: #fef2f2;
  border-left-color: var(--accent);
}

.faq-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  margin-bottom: 16px;
  padding: 20px;
  box-shadow: var(--shadow);
}
.faq-question {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.faq-answer {
  font-size: 0.95rem;
  line-height: 1.75;
  color: #334155;
}

footer {
  background: #0f172a;
  color: #94a3b8;
  padding: 50px 0 30px;
  margin-top: 60px;
  border-top: 4px solid var(--primary);
  font-size: 0.9rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 30px;
}
@media(max-width: 768px) {
  .footer-grid { grid-template-columns: 1fr; }
}
.footer-about h4, .footer-links h4 {
  color: #ffffff;
  font-size: 1.1rem;
  margin-bottom: 14px;
}
.footer-seo-p {
  line-height: 1.7;
  font-size: 0.88rem;
  margin-bottom: 12px;
}
.footer-links ul { list-style: none; }
.footer-links li { margin-bottom: 8px; }
.footer-links a { color: #cbd5e1; }
.footer-links a:hover { color: #ffffff; }

.footer-bottom {
  text-align: center;
  padding-top: 24px;
  border-top: 1px solid #1e293b;
  font-size: 0.8rem;
}

#search-results-modal {
  display: none;
  position: absolute;
  top: 45px;
  right: 0;
  width: 350px;
  max-height: 400px;
  overflow-y: auto;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
  z-index: 2000;
  padding: 10px;
}
#search-results-modal.active { display: block; }
.search-result-item {
  padding: 8px;
  border-bottom: 1px solid var(--border);
}
.search-result-item a { font-weight: 700; font-size: 0.9rem; }
"""

with open(os.path.join(SITE_ROOT, "static", "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(STYLE_CSS)

# 4. JS
SEARCH_JS = """// Search Script
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const resultsContainer = document.getElementById("search-results-modal");
  let searchIndex = null;

  if (searchInput) {
    searchInput.addEventListener("focus", function () {
      if (!searchIndex) {
        fetch("/index.json")
          .then(res => res.json())
          .then(data => { searchIndex = data; })
          .catch(err => console.error("Error loading search index:", err));
      }
    });

    searchInput.addEventListener("input", function () {
      const query = this.value.trim().toLowerCase();
      if (!query || !searchIndex) {
        resultsContainer.innerHTML = "";
        resultsContainer.classList.remove("active");
        return;
      }

      const matches = searchIndex.filter(item => {
        return (item.title && item.title.toLowerCase().includes(query)) ||
               (item.contents && item.contents.toLowerCase().includes(query)) ||
               (item.summary && item.summary.toLowerCase().includes(query));
      }).slice(0, 8);

      if (matches.length > 0) {
        let html = "";
        matches.forEach(item => {
          html += `<div class="search-result-item">
            <a href="${item.permalink}">${item.title}</a>
            <div style="font-size:0.75rem; color:#64748b;">${item.section || "文章"}</div>
          </div>`;
        });
        resultsContainer.innerHTML = html;
        resultsContainer.classList.add("active");
      } else {
        resultsContainer.innerHTML = `<div style="padding:10px; font-size:0.85rem; color:#64748b;">未找到匹配文章</div>`;
        resultsContainer.classList.add("active");
      }
    });

    document.addEventListener("click", function (e) {
      if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
        resultsContainer.classList.remove("active");
      }
    });
  }

  const toggleBtn = document.getElementById("mobile-menu-toggle");
  const mainNav = document.getElementById("main-nav");
  if (toggleBtn && mainNav) {
    toggleBtn.addEventListener("click", function () {
      mainNav.classList.toggle("open");
    });
  }
});
"""

with open(os.path.join(SITE_ROOT, "static", "js", "search.js"), "w", encoding="utf-8") as f:
    f.write(SEARCH_JS)

# 5. Base Layout
BASEOF_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Title }}{{ end }}</title>
  <meta name="description" content="{{ if .Description }}{{ .Description }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <meta name="keywords" content="{{ .Site.Params.keywords }}">
  <link rel="canonical" href="{{ .Permalink }}">
  <link rel="stylesheet" href="/css/style.css">
  <script src="/js/search.js" defer></script>

  <meta property="og:title" content="{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }}{{ end }}">
  <meta property="og:description" content="{{ if .Description }}{{ .Description }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <meta property="og:url" content="{{ .Permalink }}">
  <meta property="og:type" content="{{ if .IsPage }}article{{ else }}website{{ end }}">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "{{ if .IsPage }}BlogPosting{{ else }}WebSite{{ end }}",
    "headline": "{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }}{{ end }}",
    "url": "{{ .Permalink }}",
    "description": "{{ if .Description }}{{ .Description }}{{ else }}{{ .Site.Params.description }}{{ end }}",
    "inLanguage": "zh-CN",
    "publisher": {
      "@type": "Organization",
      "name": "机场好 (jchao.xyz)",
      "url": "https://jchao.xyz"
    }
  }
  </script>
</head>
<body>
  {{ partial "header.html" . }}
  
  <main>
    {{ block "main" . }}{{ end }}
  </main>

  {{ partial "footer.html" . }}
</body>
</html>
"""

with open(os.path.join(SITE_ROOT, "layouts", "_default", "baseof.html"), "w", encoding="utf-8") as f:
    f.write(BASEOF_HTML)

HEADER_HTML = """<header>
  <div class="container header-inner">
    <div class="brand">
      <a href="/" class="brand-logo">jchao.xyz 机场好</a>
      <span class="brand-tagline">2026精选好机场推荐与科学上网指南</span>
    </div>

    <nav class="main-nav" id="main-nav">
      {{ range .Site.Data.site_seo.navigationItems }}
        <a href="{{ .url }}">{{ .label }}</a>
      {{ end }}
    </nav>

    <div class="header-right">
      <div class="search-box">
        <input type="text" id="search-input" class="search-input" placeholder="搜索文章/教程/FAQ...">
        <div id="search-results-modal"></div>
      </div>
      <a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener" class="btn-tg-header">
        ✈️ TG 官方频道
      </a>
      <button class="menu-toggle" id="mobile-menu-toggle" aria-label="切换导航菜单">☰</button>
    </div>
  </div>
</header>
"""

with open(os.path.join(SITE_ROOT, "layouts", "partials", "header.html"), "w", encoding="utf-8") as f:
    f.write(HEADER_HTML)

FOOTER_HTML = """<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <h4>关于 机场好 (jchao.xyz)</h4>
        <p class="footer-seo-p">
          机场好（jchao.xyz）版权所有。本站专注2026精选好机场推荐、性价比机场、Clash机场测评与节点选择指南，持续整理便宜机场、稳定机场推荐、IPLC专线机场、科学上网梯子与全平台客户端配置教程。
        </p>
        <p class="footer-seo-p">
          免责声明与合作披露：本站为独立网络技术科普与测评站点，页面包含第三方合作与邀请链接，点击链接注册可能为本站带来维持运营的推广收益。价格、流量及节点套餐请以服务提供商官网实际结算页面为准。
        </p>
      </div>

      <div class="footer-links">
        <h4>快速导航</h4>
        <ul>
          <li><a href="/jichang-tuijian/">精选好机场推荐</a></li>
          <li><a href="/jiaocheng/">小白上手教程</a></li>
          <li><a href="/zhishi/">节点与专线科普</a></li>
          <li><a href="/faq/">常见问题与答疑</a></li>
          <li><a href="/providers/">所有机场总览表</a></li>
        </ul>
      </div>

      <div class="footer-links">
        <h4>信任与条款</h4>
        <ul>
          <li><a href="/about/">关于我们</a></li>
          <li><a href="/contact/">联系我们</a></li>
          <li><a href="/editorial-policy/">编辑原则</a></li>
          <li><a href="/methodology/">评测方法</a></li>
          <li><a href="/affiliate-disclosure/">联盟披露</a></li>
          <li><a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener">TG 交流频道</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; 2026 机场好 (jchao.xyz). All Rights Reserved. 保持连接，探索世界。</p>
    </div>
  </div>
</footer>
"""

with open(os.path.join(SITE_ROOT, "layouts", "partials", "footer.html"), "w", encoding="utf-8") as f:
    f.write(FOOTER_HTML)

HERO_HTML = """<section class="hero">
  <div class="container">
    <span class="hero-badge">2026精选好机场推荐 · 科学上网全平台配置指南</span>
    <h1>2026精选高速稳定机场推荐与小白科学上网配置指南</h1>
    
    <div class="hero-cluster-text">
      <strong>品牌心智（jchao=机场好）：</strong>面向小白用户与资深玩家提供2026精选好机场推荐、性价比机场、Clash机场推荐与梯子选购指南。全面覆盖便宜稳定IPLC专线机场、4K流媒体解锁节点、全平台客户端（Windows/macOS/iOS Shadowrocket/Android/Sing-box）一键导入教程与节点超时错误排错答疑，助您零基础选好机场，秒开外网加速！
    </div>

    <div class="hero-actions">
      <a href="/jichang-tuijian/" class="btn-hero-main">🚀 查看 2026 机场推荐榜</a>
      <a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener" class="btn-hero-sub">✈️ 加入 TG 交流频道</a>
    </div>
  </div>
</section>
"""

with open(os.path.join(SITE_ROOT, "layouts", "partials", "hero.html"), "w", encoding="utf-8") as f:
    f.write(HERO_HTML)

PROVIDER_CARD_HTML = """<div class="provider-card {{ if le .rank 4 }}top-4{{ end }}">
  <div class="rank-badge">
    <span class="rank-num">#{{ .rank }}</span>
    <span class="rank-label">{{ if le .rank 4 }}主推{{ else }}精选{{ end }}</span>
  </div>
  
  <div class="provider-info">
    <h3><a href="/providers/{{ .slug }}/">{{ .name }}</a></h3>
    <div class="provider-tags">
      <span class="tag tag-ai">AI: {{ .ai_unlock }}</span>
      {{ if .coupon }}<span class="tag tag-coupon">优惠码: {{ .coupon }}</span>{{ end }}
    </div>
    <p style="font-size: 0.9rem; color: #475569; margin: 4px 0;">{{ .features }}</p>
    <div class="provider-meta-row">
      <span><strong>价格：</strong>{{ .price }}</span>
      <span><strong>流量：</strong>{{ .traffic }}</span>
      <span><strong>线路：</strong>{{ .nodes }}</span>
    </div>
  </div>

  <div class="provider-actions">
    <a href="{{ .url }}" target="_blank" rel="sponsored nofollow noopener" class="btn-register">⚡ 官网注册</a>
    <a href="/providers/{{ .slug }}/" class="btn-detail">📖 详细测评</a>
  </div>
</div>
"""

with open(os.path.join(SITE_ROOT, "layouts", "partials", "provider_card.html"), "w", encoding="utf-8") as f:
    f.write(PROVIDER_CARD_HTML)

INDEX_HTML = """{{ define "main" }}
  {{ partial "hero.html" . }}

  <div class="container">
    <div class="layout-grid">
      <div class="main-content">
        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>🌟 2026 核心主推与精选好机场推荐</span>
            <span style="font-size: 0.85rem; color: #64748b; font-weight: normal;">已人工实时核验节点与线路</span>
          </div>

          <div class="provider-card-grid">
            {{ range .Site.Data.providers }}
              {{ partial "provider_card.html" . }}
            {{ end }}
          </div>
        </section>

        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>📊 28 大热门机场线路与价格对比表</span>
          </div>
          <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 12px;">
            提示：下表整理了全站28家翻墙机场的入口价格、流量配额、线路特色及AI解锁支持情况。请点击“官网注册”直达官方后台选购套餐。
          </p>
          <div class="table-responsive">
            <table class="cmp-table">
              <thead>
                <tr>
                  <th>排名</th>
                  <th>机场名称</th>
                  <th>参考价格</th>
                  <th>每月流量</th>
                  <th>线路类型/特色</th>
                  <th>AI Unlock</th>
                  <th>直达注册</th>
                </tr>
              </thead>
              <tbody>
                {{ range .Site.Data.providers }}
                <tr>
                  <td><strong>#{{ .rank }}</strong></td>
                  <td><a href="/providers/{{ .slug }}/"><strong>{{ .name }}</strong></a></td>
                  <td><span style="color: #dc2626; font-weight: bold;">{{ .price }}</span></td>
                  <td>{{ .traffic }}</td>
                  <td>{{ .nodes }}</td>
                  <td><span style="font-size: 0.8rem; background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px;">{{ .ai_unlock }}</span></td>
                  <td>
                    <a href="{{ .url }}" target="_blank" rel="sponsored nofollow noopener" style="background: #dc2626; color: #fff; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">
                      官网注册
                    </a>
                  </td>
                </tr>
                {{ end }}
              </tbody>
            </table>
          </div>
        </section>

        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>🚀 2026 精选好机场选购指南文章</span>
            <a href="/jichang-tuijian/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range first 6 (where .Site.RegularPages "Section" "jichang-tuijian") }}
              <div class="article-card">
                <div>
                  <h4><a href="{{ .Permalink }}">{{ .Title }}</a></h4>
                  <p class="article-summary">{{ .Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta">
                  <span>{{ .Date.Format "2006-01-02" }}</span>
                  <span>精选推荐</span>
                </div>
              </div>
            {{ end }}
          </div>
        </section>

        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>💡 小白零基础上手教程</span>
            <a href="/jiaocheng/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range first 6 (where .Site.RegularPages "Section" "jiaocheng") }}
              <div class="article-card">
                <div>
                  <h4><a href="{{ .Permalink }}">{{ .Title }}</a></h4>
                  <p class="article-summary">{{ .Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta">
                  <span>{{ .Date.Format "2006-01-02" }}</span>
                  <span>配置教程</span>
                </div>
              </div>
            {{ end }}
          </div>
        </section>

        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>🌐 节点与专线科普</span>
            <a href="/zhishi/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range first 6 (where .Site.RegularPages "Section" "zhishi") }}
              <div class="article-card">
                <div>
                  <h4><a href="{{ .Permalink }}">{{ .Title }}</a></h4>
                  <p class="article-summary">{{ .Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta">
                  <span>{{ .Date.Format "2006-01-02" }}</span>
                  <span>技术科普</span>
                </div>
              </div>
            {{ end }}
          </div>
        </section>

        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>❓ 常见问题 FAQ 快览</span>
            <a href="/faq/" style="font-size: 0.9rem;">查看完整 100 问 →</a>
          </div>
          {{ range first 5 (where .Site.RegularPages "Section" "faq") }}
            <div class="faq-item">
              <div class="faq-question">❓ <a href="{{ .Permalink }}">{{ .Title }}</a></div>
              <div class="faq-answer">{{ .Content | truncate 200 }}</div>
            </div>
          {{ end }}
        </section>
      </div>

      <aside class="sidebar">
        <div class="widget" style="background: linear-gradient(135deg, #0088cc, #005588); color: #fff;">
          <h4 style="font-size: 1.15rem; margin-bottom: 8px;">✈️ TG 官方交流频道</h4>
          <p style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 14px;">
            获取最新机场优惠码、防失联订阅备用域名与实时节点状态监控！
          </p>
          <a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #fff; color: #0088cc; font-weight: bold; padding: 10px; border-radius: 6px;">
            👉 立即加入 Telegram 频道
          </a>
        </div>

        <div class="widget">
          <h4 class="widget-title">🏆 TOP 4 核心主推机场</h4>
          <ul class="widget-list">
            {{ range first 4 .Site.Data.providers }}
              <li>
                <div style="display:flex; justify-content: space-between; align-items:center;">
                  <a href="/providers/{{ .slug }}/"><strong>#{{ .rank }} {{ .name }}</strong></a>
                  <a href="{{ .url }}" target="_blank" rel="sponsored nofollow noopener" style="background:#dc2626; color:#fff; font-size:0.75rem; padding:2px 8px; border-radius:4px; font-weight:bold;">
                    注册
                  </a>
                </div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">{{ .features }}</div>
              </li>
            {{ end }}
          </ul>
        </div>

        <div class="widget">
          <h4 class="widget-title">🛠️ 客户端使用指南</h4>
          <ul class="widget-list">
            <li><a href="/jiaocheng/ios-shadowrocket-setup/">iOS 小火箭 Shadowrocket 配置</a></li>
            <li><a href="/jiaocheng/windows-clash-verge-guide/">Windows Clash Verge 配置教程</a></li>
            <li><a href="/jiaocheng/android-clash-meta-guide/">Android Clash Meta 配置导入</a></li>
            <li><a href="/jiaocheng/sing-box-universal-tutorial/">Sing-box 通用订阅配置教程</a></li>
            <li><a href="/jiaocheng/mac-clash-nyanpasu-setup/">macOS Clash 配置教程</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)

SINGLE_HTML = """{{ define "main" }}
<div class="container" style="margin-top: 30px;">
  <div class="layout-grid">
    <div class="main-content">
      <article>
        <header class="article-header">
          <h1>{{ .Title }}</h1>
          <div class="article-meta-header">
            <span>📅 发布日期：{{ .Date.Format "2006-01-02" }}</span>
            <span>✍️ 作者：机场好编辑部</span>
            <span>⏱️ 预计阅读：{{ .ReadingTime }} 分钟</span>
          </div>
        </header>

        <div class="article-body">
          {{ if ne .Section "providers" }}
            <div class="callout-box">
              <h3 style="margin-top:0; color:#1e40af; font-size:1.15rem;">🔥 2026 编辑部推荐四家高速稳定机场</h3>
              <p style="font-size:0.9rem; margin-bottom:12px;">以下为本站严格筛选并深度测试的 4 家核心服务商，覆盖低延迟专线、4K影音及高性价比年付套餐：</p>

              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:12px;">
                {{ range first 4 .Site.Data.providers }}
                <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.85rem;">
                  <div style="font-weight:bold; color:#1e293b; font-size:1rem; margin-bottom:4px;">#{{ .rank }} {{ .name }}</div>
                  <div style="color:#dc2626; font-weight:bold; margin-bottom:4px;">{{ .price }}</div>
                  <div style="color:#64748b; margin-bottom:8px; height:36px; overflow:hidden;">{{ .features }}</div>
                  <a href="{{ .url }}" target="_blank" rel="sponsored nofollow noopener" class="btn-register" style="font-size:0.8rem; padding:6px 10px;">
                    ⚡ 官网注册入口
                  </a>
                </div>
                {{ end }}
              </div>
            </div>
          {{ end }}

          {{ .Content }}
        </div>
      </article>

      <div style="margin-top: 40px;">
        <h3>📌 相关推荐阅读</h3>
        <div class="article-grid" style="margin-top: 15px;">
          {{ range first 3 (where .Site.RegularPages "Section" .Section) }}
            {{ if ne .Permalink $.Permalink }}
              <div class="article-card">
                <h4><a href="{{ .Permalink }}">{{ .Title }}</a></h4>
                <p class="article-summary">{{ .Summary | truncate 80 }}</p>
              </div>
            {{ end }}
          {{ end }}
        </div>
      </div>
    </div>

    <aside class="sidebar">
      <div class="widget" style="background: linear-gradient(135deg, #0088cc, #005588); color: #fff;">
        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">✈️ TG 交流群与订阅</h4>
        <p style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 12px;">
          如遇节点超时或订阅更新失败，请加入 TG 官方频道获取实时通知。
        </p>
        <a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #fff; color: #0088cc; font-weight: bold; padding: 8px; border-radius: 6px; font-size:0.85rem;">
          加入 Telegram 频道
        </a>
      </div>

      {{ if .TableOfContents }}
      <div class="widget">
        <h4 class="widget-title">📖 文章目录</h4>
        <div style="font-size: 0.88rem; line-height: 1.6;">
          {{ .TableOfContents }}
        </div>
      </div>
      {{ end }}

      <div class="widget">
        <h4 class="widget-title">🏆 4 大主推机场</h4>
        <ul class="widget-list">
          {{ range first 4 .Site.Data.providers }}
            <li>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <a href="/providers/{{ .slug }}/"><strong>#{{ .rank }} {{ .name }}</strong></a>
                <a href="{{ .url }}" target="_blank" rel="sponsored nofollow noopener" style="background:#dc2626; color:#fff; font-size:0.75rem; padding:2px 8px; border-radius:4px; font-weight:bold;">
                  注册
                </a>
              </div>
            </li>
          {{ end }}
        </ul>
      </div>
    </aside>
  </div>
</div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "_default", "single.html"), "w", encoding="utf-8") as f:
    f.write(SINGLE_HTML)

LIST_HTML = """{{ define "main" }}
<div class="container" style="margin-top: 30px;">
  <div class="section-title">
    <span>{{ .Title }}</span>
  </div>
  <p style="font-size:0.95rem; color:#64748b; margin-bottom:20px;">
    {{ .Description }}
  </p>

  <div class="article-grid">
    {{ range .Pages }}
      <div class="article-card">
        <div>
          <h4><a href="{{ .Permalink }}">{{ .Title }}</a></h4>
          <p class="article-summary">{{ .Summary | truncate 120 }}</p>
        </div>
        <div class="article-meta">
          <span>{{ .Date.Format "2006-01-02" }}</span>
          <span>阅读原文 →</span>
        </div>
      </div>
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "_default", "list.html"), "w", encoding="utf-8") as f:
    f.write(LIST_HTML)

FAQ_LIST_HTML = """{{ define "main" }}
<div class="container" style="margin-top: 30px;">
  <div class="section-title">
    <span>❓ 科学上网与机场选购 FAQ 常见问题大全 (100 问完整解答)</span>
  </div>
  <p style="font-size:1rem; color:#475569; margin-bottom:24px; background:#eff6ff; padding:16px; border-radius:8px; border-left:4px solid #2563eb;">
    本页面汇集了小白零基础选购翻墙机场、全平台客户端（Clash / Shadowrocket / Sing-box / v2rayN）配置、IPLC专线原理、防失联技巧及常见报错（Timeout、DNS污染、订阅解析失败）的 100 个核心高频疑问与详细干货解答。全问答直接展开，供您快速查阅。
  </p>

  <div style="margin-bottom: 30px;">
    {{ range .Pages }}
      <div class="faq-item" id="{{ .Slug }}">
        <h3 class="faq-question">❓ <a href="{{ .Permalink }}">{{ .Title }}</a></h3>
        <div class="faq-answer">
          {{ .Content }}
        </div>
        <div style="font-size:0.8rem; color:#94a3b8; margin-top:10px; display:flex; justify-content:space-between;">
          <span>分类领域：常见问题答疑</span>
          <a href="{{ .Permalink }}">查看独立问答页面 →</a>
        </div>
      </div>
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "faq", "list.html"), "w", encoding="utf-8") as f:
    f.write(FAQ_LIST_HTML)

with open(os.path.join(SITE_ROOT, "layouts", "faq", "single.html"), "w", encoding="utf-8") as f:
    f.write(SINGLE_HTML)

PROVIDERS_LIST_HTML = """{{ define "main" }}
<div class="container" style="margin-top: 30px;">
  <div class="section-title">
    <span>全站 28 家机场服务商总览与详细评测列表</span>
  </div>
  <p style="font-size:0.95rem; color:#64748b; margin-bottom:24px;">
    本页面列出了本站收录并评测的全部 28 家科学上网翻墙机场。包含灵动云、暮光网络、飞猫云、微风网络等核心主推品牌及各大特色性价比专线机场。点击“官网注册”直接跳转至官方注册页面。
  </p>

  <div class="provider-card-grid">
    {{ range .Site.Data.providers }}
      {{ partial "provider_card.html" . }}
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "providers", "list.html"), "w", encoding="utf-8") as f:
    f.write(PROVIDERS_LIST_HTML)

with open(os.path.join(SITE_ROOT, "layouts", "providers", "single.html"), "w", encoding="utf-8") as f:
    f.write(SINGLE_HTML)

INDEX_JSON = """[{{ range $index, $page := .Site.RegularPages }}{{ if $index }},{{ end }}{
  "title": {{ $page.Title | jsonify }},
  "permalink": {{ $page.Permalink | jsonify }},
  "section": {{ $page.Section | jsonify }},
  "summary": {{ $page.Summary | plainify | jsonify }},
  "contents": {{ $page.Plain | jsonify }}
}{{ end }}]"""

with open(os.path.join(SITE_ROOT, "layouts", "_default", "index.json"), "w", encoding="utf-8") as f:
    f.write(INDEX_JSON)

print("Site assets and templates completely generated.")
