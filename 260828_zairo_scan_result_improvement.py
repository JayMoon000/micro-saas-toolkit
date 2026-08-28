import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
BASE_URL = "https://tool.starsign16.com"
DEFAULT_OG_IMAGE = f"{BASE_URL}/og-image.jpg"

def create_llms_txt(root_dir):
    llms_content = f"""# StarSign16 Micro Toolkit
> 100% Free, Client-Side Browser Utilities (Zero Server Cost & Zero Data Collection)

URL: {BASE_URL}

## Core Philosophy
- All tools run 100% client-side in the user's browser.
- No signup, no limits, no watermarks, no server-side data storage.

## Available Tools
- {BASE_URL}/ko/background-remover : AI Image Background Remover
- {BASE_URL}/ko/markdown-previewer : Real-time Markdown Editor & Previewer
- {BASE_URL}/ko/qr-generator : Clean QR Code Generator & Downloader
- {BASE_URL}/ko/image-resizer : Client-Side Image Resizer & Converter
- {BASE_URL}/ko/regex-tester : Real-time Regular Expression Tester & Explainer
- {BASE_URL}/ko/base64-tool : Base64 Encoder / Decoder
- {BASE_URL}/ko/epub-converter : 1-sec Client-side EPUB Ebook Converter
- {BASE_URL}/ko/word-counter : Real-time Korean/English Word Counter
- {BASE_URL}/ko/chart-generator : 3-sec Pastel Chart Visualizer
- {BASE_URL}/ko/calendar-maker : Natural Language Calendar Event Generator
"""
    file_path = os.path.join(root_dir, "llms.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(llms_content.strip())
    print("✅ Created: llms.txt")

def patch_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 상대 경로 기반 Canonical URL 계산
    rel_path = os.path.relpath(file_path, ROOT_DIR).replace("\\", "/")
    if rel_path.endswith("index.html"):
        canonical_path = rel_path[:-10]
    else:
        canonical_path = rel_path
    
    canonical_url = f"{BASE_URL}/{canonical_path}".rstrip("/")
    if canonical_url == BASE_URL:
        canonical_url = f"{BASE_URL}/"

    # Canonical 태그 교체/추가
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    if '<link rel="canonical"' in content:
        content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>', canonical_tag, content)
    else:
        content = content.replace("</head>", f"  {canonical_tag}\n</head>")

    # 2. Open Graph Image 태그 보강
    og_image_tag = f'<meta property="og:image" content="{DEFAULT_OG_IMAGE}">'
    if '<meta property="og:image"' not in content:
        content = content.replace("</head>", f"  {og_image_tag}\n</head>")

    # 3. DNS Preconnect 태그 보강 (Third-party scripts 최적화)
    preconnect_tags = """  <link rel="preconnect" href="https://cdnjs.cloudflare.com">
  <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">"""
    if "cdnjs.cloudflare.com" in content and '<link rel="preconnect" href="https://cdnjs.cloudflare.com">' not in content:
        content = content.replace("<head>", f"<head>\n{preconnect_tags}")

    # 4. Form input label / aria-label 보강
    def add_aria_label(match):
        input_tag = match.group(0)
        if "aria-label" not in input_tag:
            return input_tag[:-1] + ' aria-label="Input field">'
        return input_tag
    
    content = re.sub(r'<input[^>]+type=["\'](?:text|search)["\'][^>]*>', add_aria_label, content)

    # 5. GA4 및 Analytics 중복 제거 (G-6LFL2P1WRN 기준)
    ga4_matches = list(re.finditer(r'<!-- Google tag \(gtag\.js\) -->.*?https://www.googletagmanager.com/gtag/js\?id=G-6LFL2P1WRN.*?</script>', content, re.DOTALL))
    if len(ga4_matches) > 1:
        for extra in ga4_matches[1:]:
            content = content.replace(extra.group(0), "")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"🛠️ Patched: {rel_path}")

def run_all():
    create_llms_txt(ROOT_DIR)
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                patch_html_file(os.path.join(root, file))

if __name__ == "__main__":
    run_all()