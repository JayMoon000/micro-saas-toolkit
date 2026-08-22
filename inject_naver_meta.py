import os

BASE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
NAVER_TAG = '<meta name="naver-site-verification" content="d37470492bcf7537239015a4ba52a7b063e935e6" />'

target_files = [
    os.path.join(BASE_DIR, "index.html"),
    os.path.join(BASE_DIR, "ko", "index.html")
]

for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "naver-site-verification" not in content:
            content = content.replace("<head>", f"<head>\n  {NAVER_TAG}", 1)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"태그 주입 완료: {file_path}")
        else:
            print(f"이미 태그 존재: {file_path}")

print("네이버 소유확인 메타태그 주입 작업 완료!")