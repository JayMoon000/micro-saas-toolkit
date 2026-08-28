import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

def clean_and_optimize_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 서드파티 외부 스크립트 최적화 (FontAwesome, Tailwind, CDN 스크립트에 defer/async 적용)
    # 기존 외부 js 호출 태그에 defer 추가
    def optimize_script(match):
        tag = match.group(0)
        if "src=" in tag and not ("defer" in tag or "async" in tag):
            return tag[:-1] + " defer>"
        return tag

    content = re.sub(r'<script\s+[^>]*src=["\']https?://[^"\']+["\'][^>]*></script>', optimize_script, content)

    # 2. GA4 스크립트 중복 완전 제거 (단 1개만 남기기)
    ga4_pattern = r'<!--\s*Google tag \(gtag\.js\)\s*-->\s*<script[^>]*src=["\']https://www\.googletagmanager\.com/gtag/js\?id=G-6LFL2P1WRN["\'][^>]*>.*?</script>\s*<script>.*?gtag\([\'"]config[\'"],\s*[\'"]G-6LFL2P1WRN[\'"]\);\s*</script>'
    ga4_blocks = list(re.finditer(ga4_pattern, content, re.DOTALL))
    if len(ga4_blocks) > 1:
        for block in ga4_blocks[1:]:
            content = content.replace(block.group(0), "")

    # 3. Cloudflare Web Analytics 스크립트 중복 제거
    cf_pattern = r'<!--\s*Cloudflare Web Analytics\s*-->\s*<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>'
    cf_blocks = list(re.finditer(cf_pattern, content, re.DOTALL))
    if len(cf_blocks) > 1:
        for block in cf_blocks[1:]:
            content = content.replace(block.group(0), "")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"🧹 Cleaned & Optimized: {os.path.basename(file_path)}")

def run_cleanup():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                clean_and_optimize_file(os.path.join(root, file))

if __name__ == "__main__":
    run_cleanup()