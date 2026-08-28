import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
BASE_URL = "https://tool.starsign16.com"
GA4_ID = "G-6LFL2P1WRN"

def rebuild_clean_head(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 기존 head 추출 및 분석
    head_match = re.search(r"<head>(.*?)</head>", content, re.DOTALL | re.IGNORECASE)
    if not head_match:
        return

    orig_head = head_match.group(1)

    # 기본 타이틀 및 메타 추출 (없을 경우 기본값 fallback)
    title_match = re.search(r"<title>(.*?)</title>", orig_head, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "StarSign16 Micro Toolkit"

    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', orig_head, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else "100% Free Browser-based Utilities"

    # 2. 정밀 Canonical URL 계산
    rel_path = os.path.relpath(file_path, ROOT_DIR).replace("\\", "/")
    if rel_path.endswith("index.html"):
        clean_path = rel_path[:-10]
    else:
        clean_path = rel_path.replace(".html", "")

    clean_path = clean_path.strip("/")
    canonical_url = f"{BASE_URL}/{clean_path}" if clean_path else BASE_URL

    # 3. 규격화된 청정 Single <head> 블록 생성
    clean_head = f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{BASE_URL}/og-image.jpg">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Preconnect & CDNs -->
  <link rel="preconnect" href="https://cdn.tailwindcss.com">
  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
  <link rel="preconnect" href="https://cdnjs.cloudflare.com">
  <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google tag (gtag.js) - Single Instance -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>
</head>"""

    # 4. 기존 head 완전 교체
    new_content = re.sub(r"<head>.*?</head>", clean_head, content, flags=re.DOTALL | re.IGNORECASE)

    # 5. body 하단에 남아있을 수 있는 잔여 트래커/비콘 스크립트 제거
    new_content = re.sub(r'<!--\s*Cloudflare Web Analytics\s*-->\s*<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', new_content, flags=re.DOTALL)
    new_content = re.sub(r'<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', new_content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✨ Standardized: {rel_path}")

def run():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                rebuild_clean_head(os.path.join(root, file))

if __name__ == "__main__":
    run()