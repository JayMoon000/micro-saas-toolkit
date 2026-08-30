import os
from PIL import Image, ImageDraw, ImageFont

SAVE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
OUT_PATH = os.path.join(SAVE_DIR, "youtube_banner_fixed.png")

# 1. 유튜브 공식 배너 규격 (2048 x 1152)
WIDTH, HEIGHT = 2048, 1152
img = Image.new("RGBA", (WIDTH, HEIGHT), (2, 6, 23, 255)) # Dark Slate 배경 (#020617)
draw = ImageDraw.Draw(img)

# 세이프존 중심 좌표: Y축 576 기준 상하 169px (Y: 407 ~ 745)
SAFE_CENTER_Y = HEIGHT // 2

# 폰트 로드 (윈도우 맑은 고딕)
try:
    font_title = ImageFont.truetype("malgunbd.ttf", 68)
    font_sub = ImageFont.truetype("malgunbd.ttf", 36)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# 텍스트 그리기 (중앙 세이프존 안쪽 정렬)
title_text = "StarSign16"
sub_text = "100% 무료 온디바이스 웹 유틸리티 툴킷"

# 타이틀 (시안색/화이트)
draw.text((WIDTH // 2, SAFE_CENTER_Y - 45), title_text, fill=(56, 189, 248), font=font_title, anchor="mm")
# 서브텍스트 (밝은 그레이)
draw.text((WIDTH // 2, SAFE_CENTER_Y + 45), sub_text, fill=(241, 245, 249), font=font_sub, anchor="mm")

# 저장
os.makedirs(SAVE_DIR, exist_ok=True)
img.save(OUT_PATH, "PNG")
print(f"✅ Banner generated perfectly inside safe-zone: {OUT_PATH}")