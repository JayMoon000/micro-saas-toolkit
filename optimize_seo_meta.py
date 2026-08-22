import os
import re

BASE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
BASE_URL = "https://tool.starsign16.com"

# 1. 영문 허브 및 개별 툴 최적화
EN_TITLE = "StarSign16 Toolkit - Free Web Utilities"
EN_DESC = "Fast, 100% client-side privacy-first web utilities with no logins."

# 2. 한글 허브 및 개별 툴 최적화
KO_TITLE = "StarSign16 툴킷 - 100% 무료 브라우저 도구"
KO_DESC = "서버 전송 없는 안전한 16종 초경량 웹 유틸리티. 개발·업무 무료 도구 모음."

def update_seo(file_path, is_korean):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    file_name = os.path.basename(file_path).replace(".html", "")
    title = KO_TITLE if is_korean else EN_TITLE
    desc = KO_DESC if is_korean else EN_DESC
    
    # URL 경로
    if file_name == "index":
        url = f"{BASE_URL}/ko" if is_korean else f"{BASE_URL}/"
    else:
        url = f"{BASE_URL}/ko/{file_name}" if is_korean else f"{BASE_URL}/{file_name}"

    og_tags = f"""  <!-- SEO & Open Graph -->
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">"""

    # 기존 title, description, og 태그 정리
    content = re.sub(r'\s*<title>.*?</title>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<meta name="description" content=".*?">', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<!-- SEO & Open Graph -->.*?<meta property="og:url" content=".*?">', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<meta property="og:[^"]+" content=".*?">', '', content, flags=re.DOTALL)

    # <head> 태그 바로 아래에 삽입
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n{og_tags}", 1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

# 영문 및 한국어 처리
count = 0
for directory, is_ko in [(BASE_DIR, False), (os.path.join(BASE_DIR, "ko"), True)]:
    if not os.path.exists(directory):
        continue
    for file in os.listdir(directory):
        if file.endswith(".html"):
            if update_seo(os.path.join(directory, file), is_ko):
                count += 1

print(f"총 {count}개 파일 SEO 및 Open Graph 태그 최적화 완료!")