import os
from PIL import Image, ImageDraw, ImageFont

SAVE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
OUT_PATH = os.path.join(SAVE_DIR, "ph_comparison_chart_en.png")

# 1. Product Hunt 갤러리 규격 (1280 x 720)
WIDTH, HEIGHT = 1280, 720
img = Image.new("RGBA", (WIDTH, HEIGHT), (15, 23, 42, 255)) # Dark Navy 배경 (#0F172A)
draw = ImageDraw.Draw(img)

# 폰트 로드 (Segoe UI - Modern English Font)
try:
    # 윈도우 기본 Segoe UI 사용 (볼드, 레귤러)
    font_bold = ImageFont.truetype("segoeuib.ttf", 48)
    font_sub_bold = ImageFont.truetype("segoeuib.ttf", 36)
    font_body = ImageFont.truetype("segoeui.ttf", 28)
except:
    # 폰트 없을 경우 기본값
    font_bold = ImageFont.load_default()
    font_sub_bold = ImageFont.load_default()
    font_body = ImageFont.load_default()

# 텍스트 레이아웃 좌표
col1, col2, col3 = 80, 520, 920
row1, row2, row3, row4, row5, row6 = 80, 180, 290, 400, 510, 620
col2_w, col3_w = 340, 340 # Column Width

# 타이틀
draw.text((col1, row1), "Feature Comparison", fill=(241, 245, 249), font=font_bold)
draw.text((col1, row1 + 60), "StarSign16 vs. Existing Premium Tools", fill=(148, 163, 184), font=font_body)

# 테이블 헤더
# draw.rectangle([(col2, row2), (col2 + col2_w, row2 + 70)], fill=(51, 65, 85, 255)) # Box
draw.text((col1, row2), "Key Feature", fill=(148, 163, 184), font=font_sub_bold)
draw.text((col2, row2), "Existing Tools", fill=(239, 68, 68), font=font_sub_bold) # Red
draw.text((col3, row2), "StarSign16 Toolkit", fill=(34, 211, 238), font=font_sub_bold) # Cyan

# 테이블 라인
draw.line([(col1, row2 + 60), (col3 + col3_w, row2 + 60)], fill=(51, 65, 85, 255), width=2)

# 행 데이터
data = [
    ("Login Requirement", "YES (Mandatory)", "NO (Zero-Barrier)"),
    ("Commercial License", "Paid Plan Needed", "100% Free (Unlimited)"),
    ("Data Privacy", "Server Transmission", "100% On-Device (Local)"),
    ("Watermarks/Limits", "YES (On Free Tier)", "NO (None)"),
    ("Full HD Downloads", "YES (Requires $$)", "YES (Original High-Res)")
]

y_pos = row3
for feature, existing, starsign in data:
    draw.text((col1, y_pos), feature, fill=(241, 245, 249), font=font_body)
    draw.text((col2, y_pos), existing, fill=(239, 68, 68), font=font_body)
    draw.text((col3, y_pos), starsign, fill=(34, 211, 238), font=font_body)
    draw.line([(col1, y_pos + 45), (col3 + col3_w, y_pos + 45)], fill=(51, 65, 85, 255), width=1)
    y_pos += 85

# 저장
os.makedirs(SAVE_DIR, exist_ok=True)
img.save(OUT_PATH, "PNG")
print(f"✅ Product Hunt Comparison Chart generated (EN): {OUT_PATH}")