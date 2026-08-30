import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

def verify_files():
    issues = []
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # GA4 등장 횟수 체크
                ga4_count = len(re.findall(r'G-6LFL2P1WRN', content))
                # Cloudflare beacon 존재 여부 체크
                cf_exists = "cloudflareinsights.com/beacon.min.js" in content
                
                if ga4_count > 2 or cf_exists: # config 1번 + gtag script 1번 = 총 2회 등장이 정상
                    issues.append((file, ga4_count, cf_exists))
    
    if not issues:
        print("✅ 모든 HTML 파일에서 중복 트래커가 완벽하게 제거되었음!")
    else:
        for file, count, cf in issues:
            print(f"⚠️ {file}: GA4 키 등장 {count}회, Cloudflare 수동태그 존재={cf}")

if __name__ == "__main__":
    verify_files()