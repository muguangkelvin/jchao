import os
import json

SITE_ROOT = r"c:\Users\USER\Desktop\博客\jchao.xyz"

# 1. Write _index.md for all 5 sections to fix section titles in Chinese
sections_info = [
    ("jichang-tuijian", "精选好机场推荐", "2026精选好机场推荐文章列表，涵盖IPLC专线、便宜稳定机场、ChatGPT/Claude AI解锁及4K流媒体选购指南。"),
    ("jiaocheng", "小白上手教程", "全平台科学上网客户端（Windows Clash Verge / iOS Shadowrocket 小火箭 / Android / Sing-box）图文配置教程。"),
    ("zhishi", "节点与专线科普", "IPLC专线与IEPL专线区别、SS/Trojan/VLESS/HY2协议对比及GFW防火墙原理科普。"),
    ("faq", "常见问题与答疑 (100问)", "100个常见翻墙机场选购、订阅导入、超时排错与防失联问答大全。"),
    ("providers", "所有机场总览表与专属测评", "全站28家科学上网机场独立测评页、包含官网注册入口、参考价格、流量配额及优惠码。")
]

for folder, title, desc in sections_info:
    path = os.path.join(SITE_ROOT, "content", folder, "_index.md")
    content = f"""---
title: "{title}"
description: "{desc}"
date: 2026-09-01T10:00:00+08:00
---
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Section _index.md files created.")

# 2. Update layouts/_default/list.html to make entire card and button 100% clickable
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
      {{ if ne .Title $.Title }}
      <div class="article-card" onclick="window.location.href='{{ .RelPermalink }}'" style="cursor: pointer;">
        <div>
          <h4><a href="{{ .RelPermalink }}" style="color:#0f172a; text-decoration:none;">{{ .Title }}</a></h4>
          <p class="article-summary" style="margin-top:8px;">{{ .Summary | truncate 120 }}</p>
        </div>
        <div class="article-meta" style="margin-top:14px;">
          <span>{{ .Date.Format "2006-01-02" }}</span>
          <a href="{{ .RelPermalink }}" style="color: #2563eb; font-weight: bold; text-decoration: none;">阅读原文 →</a>
        </div>
      </div>
      {{ end }}
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open(os.path.join(SITE_ROOT, "layouts", "_default", "list.html"), "w", encoding="utf-8") as f:
    f.write(LIST_HTML)

# 3. Update layouts/index.html to make all homepage cards 100% clickable
INDEX_HTML = """{{ define "main" }}
  {{ partial "hero.html" . }}

  <div class="container">
    <div class="layout-grid">
      <div class="main-content">
        <!-- 1. Provider Recommendation List -->
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

        <!-- 2. Comparison Table -->
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

        <!-- 3. Recommendation Articles Section -->
        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>🚀 2026 精选好机场选购指南文章</span>
            <a href="/jichang-tuijian/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range $idx, $page := where .Site.RegularPages "Section" "jichang-tuijian" }}
              {{ if lt $idx 6 }}
              <div class="article-card" onclick="window.location.href='{{ $page.RelPermalink }}'" style="cursor: pointer;">
                <div>
                  <h4><a href="{{ $page.RelPermalink }}" style="color:#0f172a;">{{ $page.Title }}</a></h4>
                  <p class="article-summary" style="margin-top:8px;">{{ $page.Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta" style="margin-top:14px;">
                  <span>{{ $page.Date.Format "2006-01-02" }}</span>
                  <a href="{{ $page.RelPermalink }}" style="color:#2563eb; font-weight:bold;">阅读原文 →</a>
                </div>
              </div>
              {{ end }}
            {{ end }}
          </div>
        </section>

        <!-- 4. Client Tutorial Section -->
        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>💡 小白零基础上手教程</span>
            <a href="/jiaocheng/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range $idx, $page := where .Site.RegularPages "Section" "jiaocheng" }}
              {{ if lt $idx 6 }}
              <div class="article-card" onclick="window.location.href='{{ $page.RelPermalink }}'" style="cursor: pointer;">
                <div>
                  <h4><a href="{{ $page.RelPermalink }}" style="color:#0f172a;">{{ $page.Title }}</a></h4>
                  <p class="article-summary" style="margin-top:8px;">{{ $page.Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta" style="margin-top:14px;">
                  <span>{{ $page.Date.Format "2006-01-02" }}</span>
                  <a href="{{ $page.RelPermalink }}" style="color:#2563eb; font-weight:bold;">阅读原文 →</a>
                </div>
              </div>
              {{ end }}
            {{ end }}
          </div>
        </section>

        <!-- 5. Knowledge Section -->
        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>🌐 节点与专线科普</span>
            <a href="/zhishi/" style="font-size: 0.9rem;">查看全部 →</a>
          </div>
          <div class="article-grid">
            {{ range $idx, $page := where .Site.RegularPages "Section" "zhishi" }}
              {{ if lt $idx 6 }}
              <div class="article-card" onclick="window.location.href='{{ $page.RelPermalink }}'" style="cursor: pointer;">
                <div>
                  <h4><a href="{{ $page.RelPermalink }}" style="color:#0f172a;">{{ $page.Title }}</a></h4>
                  <p class="article-summary" style="margin-top:8px;">{{ $page.Summary | truncate 100 }}</p>
                </div>
                <div class="article-meta" style="margin-top:14px;">
                  <span>{{ $page.Date.Format "2006-01-02" }}</span>
                  <a href="{{ $page.RelPermalink }}" style="color:#2563eb; font-weight:bold;">阅读原文 →</a>
                </div>
              </div>
              {{ end }}
            {{ end }}
          </div>
        </section>

        <!-- 6. FAQ Quick Preview -->
        <section style="margin-bottom: 40px;">
          <div class="section-title">
            <span>❓ 常见问题 FAQ 快览</span>
            <a href="/faq/" style="font-size: 0.9rem;">查看完整 100 问 →</a>
          </div>
          {{ range $idx, $page := where .Site.RegularPages "Section" "faq" }}
            {{ if lt $idx 5 }}
            <div class="faq-item">
              <div class="faq-question">❓ <a href="{{ $page.RelPermalink }}">{{ $page.Title }}</a></div>
              <div class="faq-answer">{{ $page.Content | truncate 200 }}</div>
            </div>
            {{ end }}
          {{ end }}
        </section>
      </div>

      <!-- Sidebar -->
      <aside class="sidebar">
        <!-- Widget 1: TG Channel -->
        <div class="widget" style="background: linear-gradient(135deg, #0088cc, #005588); color: #fff;">
          <h4 style="font-size: 1.15rem; margin-bottom: 8px;">✈️ TG 官方交流频道</h4>
          <p style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 14px;">
            获取最新机场优惠码、防失联订阅备用域名与实时节点状态监控！
          </p>
          <a href="{{ .Site.Params.tgChannel }}" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #fff; color: #0088cc; font-weight: bold; padding: 10px; border-radius: 6px;">
            👉 立即加入 Telegram 频道
          </a>
        </div>

        <!-- Widget 2: Top 4 Featured -->
        <div class="widget">
          <h4 class="widget-title">🏆 TOP 4 核心主推机场</h4>
          <ul class="widget-list">
            {{ range $idx, $p := .Site.Data.providers }}
              {{ if lt $idx 4 }}
              <li>
                <div style="display:flex; justify-content: space-between; align-items:center;">
                  <a href="/providers/{{ $p.slug }}/"><strong>#{{ $p.rank }} {{ $p.name }}</strong></a>
                  <a href="{{ $p.url }}" target="_blank" rel="sponsored nofollow noopener" style="background:#dc2626; color:#fff; font-size:0.75rem; padding:2px 8px; border-radius:4px; font-weight:bold;">
                    注册
                  </a>
                </div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">{{ $p.features }}</div>
              </li>
              {{ end }}
            {{ end }}
          </ul>
        </div>

        <!-- Widget 3: Quick Setup Guides -->
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

print("List and Index layouts updated with 100% clickable cards and Chinese section titles.")
