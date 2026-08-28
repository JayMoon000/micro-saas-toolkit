import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
BASE_URL = "https://tool.starsign16.com"
GA4_ID = "G-6LFL2P1WRN"

def purge_and_clean_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 파일 전체에서 GA4, Cloudflare, FontAwesome, 외부 스크립트 중복 흔적 모조리 제거
    content = re.sub(r'<!--\s*Google tag \(gtag\.js\)\s*-->.*?gtag\([\'"]config[\'"],\s*[\'"]G-6LFL2P1WRN[\'"]\);\s*</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*src=["\']https://www\.googletagmanager\.com/gtag/js\?id=[^"\']+["\'][^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--\s*Cloudflare Web Analytics\s*-->.*?static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*cdn\.tailwindcss\.com[^>]*></script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 2. 메타 및 Canonical 추출/정리
    title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "StarSign16 Micro Toolkit"

    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else "100% Free Browser-based Utilities"

    rel_path = os.path.relpath(file_path, ROOT_DIR).replace("\\", "/")
    if rel_path.endswith("index.html"):
        clean_path = rel_path[:-10]
    else:
        clean_path = rel_path.replace(".html", "")

    clean_path = clean_path.strip("/")
    canonical_url = f"{BASE_URL}/{clean_path}" if clean_path else BASE_URL

    # 3. 깨끗한 헤더 표준 블록 정의 (GA4 딱 1회 주입)
    clean_head = f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical_url}">
  
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{BASE_URL}/og-image.jpg">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="preconnect" href="https://cdn.tailwindcss.com">
  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>
</head>"""

    # 4. 헤더 교체 및 빈 줄 정리
    content = re.sub(r"<head>.*?</head>", clean_head, content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"🧹 Purged & Fixed: {rel_path}")

def run():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                purge_and_clean_html(os.path.join(root, file))

if __name__ == "__main__":
    run()