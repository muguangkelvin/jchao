// High-Performance Omnibox Fuzzy Search Engine for "机场好" (jchao.xyz)
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const resultsContainer = document.getElementById("search-results-modal");
  const searchIcon = document.querySelector(".search-icon-img");
  let searchIndex = window.SITE_SEARCH_INDEX || null;
  let selectedIndex = -1;

  if (!searchInput || !resultsContainer) return;

  // Clickable search icon
  if (searchIcon) {
    searchIcon.style.cursor = "pointer";
    searchIcon.addEventListener("click", function () {
      searchInput.focus();
    });
  }

  function getIndexPath() {
    const scripts = document.getElementsByTagName("script");
    for (let script of scripts) {
      if (script.src && script.src.includes("search.js")) {
        return script.src.replace(/js\/search\.js.*$/, "index.json");
      }
    }
    return "index.json";
  }

  function loadSearchIndex() {
    if (window.SITE_SEARCH_INDEX && window.SITE_SEARCH_INDEX.length > 0) {
      searchIndex = window.SITE_SEARCH_INDEX;
      return Promise.resolve(searchIndex);
    }
    if (searchIndex && searchIndex.length > 0) return Promise.resolve(searchIndex);

    const indexPath = getIndexPath();
    return fetch(indexPath)
      .then(res => res.json())
      .then(data => {
        searchIndex = data;
        window.SITE_SEARCH_INDEX = data;
        return searchIndex;
      })
      .catch(err => {
        console.warn("Fetch index fallback to inline index", err);
        return window.SITE_SEARCH_INDEX || [];
      });
  }

  const sectionMap = {
    "jichang-tuijian": "精选好机场",
    "jiaocheng": "小白上手教程",
    "zhishi": "节点与专线科普",
    "faq": "常见问题 FAQ",
    "providers": "机场测评与注册",
    "about": "关于我们"
  };

  function highlightKeywords(text, tokens) {
    if (!text) return "";
    let safeText = text.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    tokens.forEach(token => {
      if (!token || token.length === 0) return;
      const regex = new RegExp(`(${token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
      safeText = safeText.replace(regex, '<mark style="background:#fef08a; color:#854d0e; padding:0 2px; border-radius:2px;">$1</mark>');
    });
    return safeText;
  }

  function performSearch(rawQuery) {
    const query = rawQuery.trim().toLowerCase();
    if (!query || !searchIndex || searchIndex.length === 0) {
      resultsContainer.innerHTML = "";
      resultsContainer.classList.remove("active");
      selectedIndex = -1;
      return;
    }

    const tokens = query.split(/\s+/).filter(t => t.length > 0);
    const scoredMatches = [];

    searchIndex.forEach(item => {
      const title = (item.title || "").toLowerCase();
      const desc = (item.description || "").toLowerCase();
      const summary = (item.summary || "").toLowerCase();
      const contents = (item.contents || "").toLowerCase();
      const section = (item.section || "").toLowerCase();
      const mappedSec = (sectionMap[item.section] || "").toLowerCase();

      const combinedText = `${title} ${desc} ${summary} ${contents} ${section} ${mappedSec}`;

      let matchCount = 0;
      let score = 0;

      tokens.forEach(token => {
        if (title.includes(token)) {
          matchCount++;
          score += 100;
        } else if (desc.includes(token) || summary.includes(token)) {
          matchCount++;
          score += 40;
        } else if (combinedText.includes(token)) {
          matchCount++;
          score += 10;
        }
      });

      if (matchCount > 0) {
        if (combinedText.includes(query)) score += 50;
        if (title.includes(query)) score += 150;
        scoredMatches.push({ item, score, matchCount });
      }
    });

    scoredMatches.sort((a, b) => b.score - a.score);

    const topMatches = scoredMatches.slice(0, 10);

    if (topMatches.length > 0) {
      let html = `<div style="font-size:0.75rem; color:#64748b; padding:6px 12px; border-bottom:1px solid #e2e8f0; background:#f8fafc; font-weight:bold; display:flex; justify-content:space-between; align-items:center;">
        <span>🔍 找到 ${scoredMatches.length} 条关联结果</span>
        <span style="font-weight:normal; font-size:0.7rem; color:#94a3b8;">↑↓ 键选择，Enter 打开</span>
      </div>`;

      topMatches.forEach(({ item }, idx) => {
        const secLabel = sectionMap[item.section] || item.section || "文章";
        let snippet = item.summary || item.description || item.contents || "";
        if (snippet.length > 75) snippet = snippet.substring(0, 75) + "...";

        const highlightedTitle = highlightKeywords(item.title, tokens);
        const highlightedSnippet = highlightKeywords(snippet, tokens);

        html += `<div class="search-result-item ${idx === selectedIndex ? 'selected' : ''}" data-url="${item.permalink}" style="padding:10px 12px; border-bottom:1px solid #f1f5f9; cursor:pointer; transition:background 0.15s;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <a href="${item.permalink}" class="search-title" style="font-weight:700; color:#0f172a; text-decoration:none; font-size:0.88rem;">${highlightedTitle}</a>
            <span style="font-size:0.7rem; background:#eff6ff; color:#2563eb; padding:2px 7px; border-radius:4px; font-weight:600; flex-shrink:0; margin-left:8px;">${secLabel}</span>
          </div>
          ${snippet ? `<div style="font-size:0.78rem; color:#64748b; line-height:1.45;">${highlightedSnippet}</div>` : ''}
        </div>`;
      });
      resultsContainer.innerHTML = html;
      resultsContainer.classList.add("active");
    } else {
      resultsContainer.innerHTML = `<div style="padding:16px; font-size:0.85rem; color:#64748b; text-align:center;">
        未找到与 "<strong style="color:#ef4444;">${rawQuery}</strong>" 相关的词汇文章<br>
        <span style="font-size:0.75rem; color:#94a3b8; margin-top:6px; display:block;">试搜关键词：灵动云 / 暮光网络 / Clash / 小火箭 / IPLC / 按量计费 / 节点超时</span>
      </div>`;
      resultsContainer.classList.add("active");
    }
  }

  // Bind input events
  searchInput.addEventListener("focus", function () {
    loadSearchIndex().then(() => {
      if (this.value.trim()) performSearch(this.value);
    });
  });

  searchInput.addEventListener("input", function () {
    loadSearchIndex().then(() => performSearch(this.value));
  });

  // Keyboard navigation
  searchInput.addEventListener("keydown", function (e) {
    const items = resultsContainer.querySelectorAll(".search-result-item");
    if (!items.length) return;

    if (e.key === "ArrowDown") {
      e.preventDefault();
      selectedIndex = (selectedIndex + 1) % items.length;
      updateSelection(items);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      selectedIndex = (selectedIndex - 1 + items.length) % items.length;
      updateSelection(items);
    } else if (e.key === "Enter") {
      e.preventDefault();
      if (selectedIndex >= 0 && items[selectedIndex]) {
        const targetUrl = items[selectedIndex].getAttribute("data-url");
        if (targetUrl) window.location.href = targetUrl;
      } else if (items[0]) {
        const targetUrl = items[0].getAttribute("data-url");
        if (targetUrl) window.location.href = targetUrl;
      }
    } else if (e.key === "Escape") {
      resultsContainer.classList.remove("active");
    }
  });

  function updateSelection(items) {
    items.forEach((el, idx) => {
      if (idx === selectedIndex) {
        el.style.background = "#eff6ff";
      } else {
        el.style.background = "transparent";
      }
    });
  }

  resultsContainer.addEventListener("click", function (e) {
    const item = e.target.closest(".search-result-item");
    if (item) {
      const url = item.getAttribute("data-url");
      if (url) window.location.href = url;
    }
  });

  document.addEventListener("click", function (e) {
    if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
      resultsContainer.classList.remove("active");
    }
  });

  // Mobile navigation menu toggle
  const toggleBtn = document.getElementById("mobile-menu-toggle");
  const mainNav = document.getElementById("main-nav");
  if (toggleBtn && mainNav) {
    toggleBtn.addEventListener("click", function () {
      mainNav.classList.toggle("open");
    });
  }
});
