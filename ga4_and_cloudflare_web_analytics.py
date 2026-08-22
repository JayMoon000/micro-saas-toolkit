import os
import re

# ==========================================
# 설정값 (필요시 실제 ID/토큰으로 변경)
# ==========================================
GA_MEASUREMENT_ID = "G-6LFL2P1WRN"  # GA4 측정 ID
CF_TOKEN = "6d000ebb184d437c8af3ee42a914a19d"   # Cloudflare Web Analytics 토큰

BASE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

# 주입할 Analytics 스크립트 템플릿
ANALYTICS_HEAD_TAG = f"""  <!-- Analytics -->
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_MEASUREMENT_ID}');

    // 커스텀 툴 액션 이벤트 트래커
    function trackToolAction(actionName, toolCategory) {{
      gtag('event', 'tool_action', {{
        'action_type': actionName,
        'tool_category': toolCategory,
        'page_path': window.location.pathname
      }});
    }}
  </script>
  <!-- Cloudflare Web Analytics -->
  <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "{CF_TOKEN}"}}'></script>
  <!-- End Analytics -->"""

def inject_analytics_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 이미 주입되어 있으면 건너뜀
    if "<!-- Analytics -->" in content:
        return False

    # <head> 태그 바로 아래에 스크립트 주입
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n{ANALYTICS_HEAD_TAG}", 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 영문 및 한국어 전체 파일 순회
target_dirs = [BASE_DIR, os.path.join(BASE_DIR, "ko")]
injected_count = 0

for directory in target_dirs:
    if not os.path.exists(directory):
        continue
    for file in os.listdir(directory):
        if file.endswith(".html"):
            full_path = os.path.join(directory, file)
            if inject_analytics_to_html(full_path):
                injected_count += 1

print(f"총 {injected_count}개 HTML 파일에 Analytics 스크립트 주입 완료!")