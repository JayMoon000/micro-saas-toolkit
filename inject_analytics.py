import os
import re

GA_MEASUREMENT_ID = "G-6LFL2P1WRN"
CF_TOKEN = "6d000ebb184d437c8af3ee42a914a19d"
BASE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

ANALYTICS_SNIPPET = f"""  <!-- Analytics: GA4 & Cloudflare -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_MEASUREMENT_ID}');
  </script>
  <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "{CF_TOKEN}"}}'></script>
  <!-- End Analytics -->"""

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 기존 GA4 단독 태그 또는 구버전 애널리틱스 블록 제거
    content = re.sub(r'\s*<!-- Google tag \(gtag\.js\) -->.*?gtag\(\'config\', \'[^\']+\'\);\s*</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<!-- Analytics: GA4 & Cloudflare -->.*?<!-- End Analytics -->', '', content, flags=re.DOTALL)

    # <head> 태그 바로 아래에 완전체 스니펫 주입
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n{ANALYTICS_SNIPPET}", 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

target_dirs = [BASE_DIR, os.path.join(BASE_DIR, "ko")]
count = 0

for directory in target_dirs:
    if not os.path.exists(directory):
        continue
    for file in os.listdir(directory):
        if file.endswith(".html"):
            if update_html(os.path.join(directory, file)):
                count += 1

print(f"총 {count}개 HTML 파일에 GA4 + Cloudflare Analytics 통합 주입 완료!")