import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

def clean_duplicate_analytics_strict(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 기존 GA4 태그 전부 추출 후 단 1개만 남기기
    ga4_block = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6LFL2P1WRN"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-6LFL2P1WRN');
</script>"""

    # 기존에 삽입된 모든 gtag 관련 블록 제거
    content = re.sub(r'<!--\s*Google tag \(gtag\.js\)\s*-->.*?gtag\([\'"]config[\'"],\s*[\'"]G-6LFL2P1WRN[\'"]\);\s*</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script[^>]*src=["\']https://www\.googletagmanager\.com/gtag/js\?id=G-6LFL2P1WRN["\'][^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];.*?gtag\([\'"]config[\'"],\s*[\'"]G-6LFL2P1WRN[\'"]\);\s*</script>', '', content, flags=re.DOTALL)

    # Cloudflare Web Analytics 수동 태그 완전 제거
    content = re.sub(r'<!--\s*Cloudflare Web Analytics\s*-->\s*<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', content, flags=re.DOTALL)

    # <head> 바로 뒤에 깨끗한 GA4 단 1개만 주입
    if "</head>" in content:
        content = content.replace("</head>", f"{ga4_block}\n</head>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Strict Cleaned: {os.path.basename(file_path)}")

def run():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                clean_duplicate_analytics_strict(os.path.join(root, file))

if __name__ == "__main__":
    run()