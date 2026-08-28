import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

def fix_zirofix_final(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Cloudflare 비콘 태그 수동 삽입분 제거 (Cloudflare 대시보드 주입과 충돌 방지)
    content = re.sub(
        r'<!--\s*Cloudflare Web Analytics\s*-->\s*<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. GA4 gtag 중복 완벽 단일화 검증
    # 모든 gtag 스크립트 블록을 찾아서 첫 번째만 남김
    gtag_pattern = r'<!--\s*Google tag \(gtag\.js\)\s*-->.*?gtag\([\'"]config[\'"],\s*[\'"]G-6LFL2P1WRN[\'"]\);\s*</script>'
    gtag_matches = list(re.finditer(gtag_pattern, content, re.DOTALL))
    if len(gtag_matches) > 1:
        for extra in gtag_matches[1:]:
            content = content.replace(extra.group(0), "")

    # 3. CDN Tailwind 및 FontAwesome 최적화 (preconnect 추가)
    if 'https://cdn.tailwindcss.com' in content and 'rel="preconnect" href="https://cdn.tailwindcss.com"' not in content:
        content = content.replace(
            "<head>",
            '<head>\n  <link rel="preconnect" href="https://cdn.tailwindcss.com">\n  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">'
        )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✨ Fixed Final: {os.path.basename(file_path)}")

def run():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                fix_zirofix_final(os.path.join(root, file))

if __name__ == "__main__":
    run()