import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

def strip_bottom_trackers_and_add_label(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 파일 내 body 종료 태그 직전의 모든 중복 트래킹 스크립트 제거
    # (Google Analytics gtag, Cloudflare beacon 등)
    content = re.sub(r'<!--\s*Google tag \(gtag\.js\)\s*-->.*?</script>\s*<script>.*?gtag\([\'"]config[\'"].*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--\s*Cloudflare Web Analytics\s*-->.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 상단 <head>에 선언된 정규 GA4 1개를 제외한 나머지 gtag 호출 블록 삭제
    head_part = content.split("</head>")[0] if "</head>" in content else ""
    body_part = content.split("</head>")[1] if "</head>" in content else content

    # body 안쪽에 남아있는 gtag 스크립트 삭제
    body_part = re.sub(r'<script[^>]*src=["\']https://www\.googletagmanager\.com/gtag/js[^"\']*["\'][^>]*>.*?</script>', '', body_part, flags=re.DOTALL | re.IGNORECASE)
    body_part = re.sub(r'<script>\s*window\.dataLayer\s*=.*?</script>', '', body_part, flags=re.DOTALL | re.IGNORECASE)

    # 2. 모든 input 태그에 aria-label 속성 확인 및 보강
    def fix_input(match):
        tag = match.group(0)
        if "aria-label" not in tag:
            return tag[:-1] + ' aria-label="도구 검색 및 입력">'
        return tag
    
    body_part = re.sub(r'<input\b(?![^>]*\baria-label=)[^>]*>', fix_input, body_part, flags=re.IGNORECASE)

    # 3. 재조합
    if "</head>" in content:
        content = head_part + "</head>" + body_part
    else:
        content = body_part

    # 빈 줄 정리
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"🧹 Bottom Cleaned: {os.path.basename(file_path)}")

def run():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                strip_bottom_trackers_and_add_label(os.path.join(root, file))

if __name__ == "__main__":
    run()