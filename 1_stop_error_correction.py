import os
import re

base_dir = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
ko_dir = os.path.join(base_dir, "ko")

# 1. 영문 파일 전체 수정 (루트)
for file in os.listdir(base_dir):
    if file.endswith(".html"):
        path = os.path.join(base_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 헤더 허브 및 언어 전환 링크 절대 경로화
        content = content.replace('href="index.html"', 'href="/"')
        content = content.replace('href="ko/index.html"', 'href="/ko"')
        content = re.sub(r'href="ko/([a-zA-Z0-9-]+)\.html"', r'href="/ko/\1"', content)
        
        # 영문 허브(index.html) 내부 툴 카드 링크 변환
        if file == "index.html":
            content = re.sub(r'href="([a-zA-Z0-9-]+)\.html"', r'href="/\1"', content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. 한국어 파일 전체 수정 (ko 폴더)
if os.path.exists(ko_dir):
    for file in os.listdir(ko_dir):
        if file.endswith(".html"):
            path = os.path.join(ko_dir, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 헤더 허브 및 언어 전환 링크 절대 경로화 (순서 중요)
            content = content.replace('href="../index.html"', 'href="/"')
            content = content.replace('href="index.html"', 'href="/ko"')
            content = re.sub(r'href="\.\./([a-zA-Z0-9-]+)\.html"', r'href="/\1"', content)
            
            # 한국어 허브(ko/index.html) 내부 툴 카드 링크 변환
            if file == "index.html":
                content = re.sub(r'href="([a-zA-Z0-9-]+)\.html"', r'href="/ko/\1"', content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print("모든 HTML 파일 내부 링크 절대 경로 변환 완료!")