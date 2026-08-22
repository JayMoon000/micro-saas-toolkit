import os
from datetime import datetime

BASE_URL = "https://tool.starsign16.com"
BASE_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"
TODAY = datetime.today().strftime('%Y-%m-%d')

tools = [
    "word-counter",
    "text-formatter",
    "lorem-generator",
    "markdown-previewer",
    "image-compressor",
    "background-remover",
    "image-resizer",
    "favicon-generator",
    "json-formatter",
    "base64-tool",
    "regex-tester",
    "url-parser",
    "dday-calculator",
    "discount-calc",
    "qr-generator",
    "loan-compound-calc"
]

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

# 1. 메인 허브 (영문 / 한글)
xml_lines.append(f'  <url>\n    <loc>{BASE_URL}/</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>1.0</priority>\n  </url>')
xml_lines.append(f'  <url>\n    <loc>{BASE_URL}/ko</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>1.0</priority>\n  </url>')

# 2. 개별 툴 16종 (영문 / 한글)
for tool in tools:
    # 영문 툴
    xml_lines.append(f'  <url>\n    <loc>{BASE_URL}/{tool}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>0.8</priority>\n  </url>')
    # 한글 툴
    xml_lines.append(f'  <url>\n    <loc>{BASE_URL}/ko/{tool}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>0.8</priority>\n  </url>')

xml_lines.append('</urlset>')

sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines))

print(f"총 {len(tools)*2 + 2}개 URL이 포함된 sitemap.xml 생성 완료!")