import os
import re
import glob

PUBLIC_DIR = r"c:\Users\USER\Desktop\博客\jchao.xyz\public"

def check_site():
    print("=== Starting Site Build Check ===")
    if not os.path.exists(PUBLIC_DIR):
        print("ERROR: public/ directory does not exist! Please run hugo first.")
        return False

    # Check key root files
    key_files = ["index.html", "robots.txt", "sitemap.xml", "index.json", "css/style.css", "js/search.js"]
    for kf in key_files:
        path = os.path.join(PUBLIC_DIR, kf)
        if os.path.exists(path):
            print(f"[PASS] Root file exists: {kf}")
        else:
            print(f"[FAIL] Missing root file: {kf}")

    # Count total HTML files
    html_files = glob.glob(os.path.join(PUBLIC_DIR, "**", "*.html"), recursive=True)
    print(f"[INFO] Total generated HTML pages: {len(html_files)}")

    # Inspect affiliate link rel attributes in HTML
    sponsored_count = 0
    tg_link_found = 0
    affiliate_links_checked = 0

    aff_domain_keywords = ["lingdongaff", "twilightaff", "flycatvipaff", "breezenetaff", "invisibleaff", "wavenetaff", "ladderaff", "flyvaff"]

    for hf in html_files:
        with open(hf, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if "t.me/+rT04DqKCxa01NzJl" in content:
                tg_link_found += 1

            for domain in aff_domain_keywords:
                if domain in content:
                    affiliate_links_checked += 1
                    if 'rel="sponsored nofollow noopener"' in content:
                        sponsored_count += 1

    print(f"[PASS] TG Channel link found in {tg_link_found} HTML pages.")
    print(f"[PASS] Affiliate links checked: {affiliate_links_checked}, with rel='sponsored nofollow noopener': {sponsored_count}")

    # Check sitemap.xml
    sitemap_path = os.path.join(PUBLIC_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sm_text = f.read()
            if "<loc>https://jchao.xyz/" in sm_text:
                print("[PASS] sitemap.xml contains correct domain URLs.")
            else:
                print("[WARN] sitemap.xml missing domain URLs.")

    print("=== Site Check Complete ===")
    return True

if __name__ == "__main__":
    check_site()
