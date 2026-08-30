import os

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

KO_HTML = """<!DOCTYPE html>
<html lang="ko" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI 배경 제거 (누끼 따기) - StarSign16 Toolkit</title>
  <meta name="description" content="100% 온디바이스 고정밀 AI 배경 분리 도구. 서버 업로드 없는 무료 누끼 제거기.">
  <link rel="canonical" href="https://tool.starsign16.com/ko/background-remover">
  
  <meta property="og:title" content="AI 배경 제거 (누끼 따기) - StarSign16 Toolkit">
  <meta property="og:description" content="100% 온디바이스 고정밀 AI 배경 분리 도구. 서버 업로드 없는 무료 누끼 제거기.">
  <meta property="og:url" content="https://tool.starsign16.com/ko/background-remover">
  <meta property="og:image" content="https://tool.starsign16.com/og-image.jpg">
  <meta property="og:type" content="website">

  <link rel="preconnect" href="https://cdn.tailwindcss.com">
  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-6LFL2P1WRN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-6LFL2P1WRN');
  </script>

  <!-- IMGLY Background Removal -->
  <script src="https://cdn.jsdelivr.net/npm/@imgly/background-removal@1.4.5/dist/bundle.js"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-cyan-500 selection:text-white">
  
  <!-- Header -->
  <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-40">
    <div class="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between">
      <a href="/ko" class="text-sm font-medium text-slate-400 hover:text-cyan-400 transition-colors flex items-center gap-1.5">
        &larr; StarSign16 툴킷 허브
      </a>
      <a href="/background-remover" class="text-xs px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">
        English
      </a>
    </div>
  </header>

  <!-- Main Content -->
  <main class="flex-1 max-w-4xl mx-auto px-4 py-8 w-full flex flex-col items-center">
    <div class="text-center mb-8">
      <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-cyan-950/60 border border-cyan-800/60 text-cyan-400">이미지 & 미디어</span>
      <h1 class="text-2xl sm:text-3xl font-bold mt-2 text-slate-100">AI 배경 제거 (누끼 따기)</h1>
      <p class="text-sm text-slate-400 mt-1">고정밀 온디바이스 AI 모델 기반 배경 분리. 내 컴퓨터 메모리에서 100% 로컬 연산됩니다.</p>
    </div>

    <!-- Drop Zone -->
    <div id="dropZone" class="w-full max-w-2xl border-2 border-dashed border-slate-700 hover:border-cyan-500/60 bg-slate-900/40 rounded-2xl p-8 text-center cursor-pointer transition-all flex flex-col items-center justify-center min-h-[220px]">
      <input type="file" id="fileInput" class="hidden" accept="image/*" aria-label="이미지 파일 선택">
      <div class="w-12 h-12 rounded-full bg-slate-800/80 flex items-center justify-center text-cyan-400 mb-3 border border-slate-700">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
      </div>
      <p class="text-sm font-medium text-slate-200">클릭하거나 이미지를 여기로 드래그하세요</p>
      <p class="text-xs text-slate-500 mt-1">PNG, JPG, WEBP 지원 (서버 전송 없음, 완전 무료)</p>
    </div>

    <!-- Preview & Result Area -->
    <div id="resultArea" class="w-full max-w-2xl mt-6 hidden flex-col items-center">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full mb-6">
        <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
          <span class="text-xs text-slate-400 mb-2">원본 이미지</span>
          <div class="w-full h-48 flex items-center justify-center overflow-hidden rounded-lg bg-slate-950">
            <img id="origImg" class="max-h-full max-w-full object-contain" alt="Original">
          </div>
        </div>
        <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
          <span class="text-xs text-cyan-400 mb-2">누끼 제거 결과</span>
          <div class="w-full h-48 flex items-center justify-center overflow-hidden rounded-lg bg-[repeating-conic-gradient(#1e293b_0%_25%,#0f172a_0%_50%)] bg-[length:16px_16px]">
            <img id="resultImg" class="max-h-full max-w-full object-contain" alt="Result">
          </div>
        </div>
      </div>
      <div class="flex gap-3">
        <button id="downloadBtn" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white text-sm font-semibold rounded-xl shadow-lg shadow-cyan-950 transition-all flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          투명 PNG 다운로드
        </button>
        <button id="resetBtn" class="px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium rounded-xl transition-all">
          다른 이미지
        </button>
      </div>
    </div>
  </main>

  <!-- Interactive Loading Overlay -->
  <div id="loadingOverlay" class="hidden fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex flex-col items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-8 max-w-sm w-full text-center shadow-2xl flex flex-col items-center">
      <div class="w-14 h-14 border-4 border-cyan-500/20 border-t-cyan-400 rounded-full animate-spin mb-4"></div>
      <h3 id="loadingStatusText" class="text-base font-semibold text-slate-100 mb-1">AI 모델 메모리 로드 중...</h3>
      <p class="text-xs text-slate-400 mb-4">최초 1회 실행 시 모델 캐싱에 3~7초 소요됩니다.</p>
      <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-3">
        <div class="bg-gradient-to-r from-cyan-500 to-indigo-500 h-full w-2/3 animate-pulse"></div>
      </div>
      <span class="text-[11px] text-slate-500">🔒 100% 브라우저 연산 (서버 전송 없음)</span>
    </div>
  </div>

  <script>
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const resultArea = document.getElementById('resultArea');
    const origImg = document.getElementById('origImg');
    const resultImg = document.getElementById('resultImg');
    const downloadBtn = document.getElementById('downloadBtn');
    const resetBtn = document.getElementById('resetBtn');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const loadingStatusText = document.getElementById('loadingStatusText');

    const msgs = [
      "AI 모델 메모리 로드 중...",
      "이미지 피사체 분석 및 분리 중...",
      "투명 배경 픽셀 다듬는 중...",
      "거의 다 완성되었습니다!"
    ];
    let msgTimer = null;

    function showLoading() {
      loadingOverlay.classList.remove('hidden');
      let idx = 0;
      loadingStatusText.innerText = msgs[0];
      msgTimer = setInterval(() => {
        idx = (idx + 1) % msgs.length;
        loadingStatusText.innerText = msgs[idx];
      }, 2000);
    }

    function hideLoading() {
      loadingOverlay.classList.add('hidden');
      if (msgTimer) clearInterval(msgTimer);
    }

    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', (e) => { e.preventDefault(); dropZone.classList.add('border-cyan-500'); });
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('border-cyan-500'));
    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropZone.classList.remove('border-cyan-500');
      if (e.dataTransfer.files.length) handleImage(e.dataTransfer.files[0]);
    });

    fileInput.addEventListener('change', (e) => {
      if (e.target.files.length) handleImage(e.target.files[0]);
    });

    let currentBlobUrl = null;

    async function handleImage(file) {
      if (!file.type.startsWith('image/')) {
        alert('이미지 파일만 지원합니다.');
        return;
      }

      origImg.src = URL.createObjectURL(file);
      showLoading();

      try {
        const imageBlob = await imglyRemoveBackground(file);
        if (currentBlobUrl) URL.revokeObjectURL(currentBlobUrl);
        currentBlobUrl = URL.createObjectURL(imageBlob);
        resultImg.src = currentBlobUrl;

        dropZone.classList.add('hidden');
        resultArea.classList.remove('hidden');
        resultArea.classList.add('flex');
      } catch (err) {
        console.error(err);
        alert('배경 제거 중 오류가 발생했습니다. (HTTPS 또는 로컬 웹서버 환경인지 확인해주세요)');
      } finally {
        hideLoading();
      }
    }

    downloadBtn.addEventListener('click', () => {
      if (!currentBlobUrl) return;
      const a = document.createElement('a');
      a.href = currentBlobUrl;
      a.download = `starsign16-nobg-${Date.now()}.png`;
      a.click();
    });

    resetBtn.addEventListener('click', () => {
      fileInput.value = '';
      resultArea.classList.add('hidden');
      resultArea.classList.remove('flex');
      dropZone.classList.remove('hidden');
    });
  </script>
</body>
</html>
"""

EN_HTML = KO_HTML.replace("AI 배경 제거 (누끼 따기) - StarSign16 Toolkit", "AI Background Remover - StarSign16 Toolkit") \
                 .replace("100% 온디바이스 고정밀 AI 배경 분리 도구. 서버 업로드 없는 무료 누끼 제거기.", "100% on-device AI background remover. Free client-side image cutout tool.") \
                 .replace("/ko/background-remover", "/background-remover") \
                 .replace("&larr; StarSign16 툴킷 허브", "&larr; StarSign16 Toolkit Hub") \
                 .replace('href="/ko"', 'href="/"') \
                 .replace('href="/background-remover"', 'href="/ko/background-remover"') \
                 .replace('>English<', '>한국어<') \
                 .replace("이미지 & 미디어", "Image & Media") \
                 .replace("AI 배경 제거 (누끼 따기)", "AI Background Remover") \
                 .replace("고정밀 온디바이스 AI 모델 기반 배경 분리. 내 컴퓨터 메모리에서 100% 로컬 연산됩니다.", "Universal high-precision background removal. 100% on-device client processing.") \
                 .replace("클릭하거나 이미지를 여기로 드래그하세요", "Click or drag & drop an image here") \
                 .replace("PNG, JPG, WEBP 지원 (서버 전송 없음, 완전 무료)", "Supports PNG, JPG, WEBP (No server upload, 100% Free)") \
                 .replace("원본 이미지", "Original Image") \
                 .replace("누끼 제거 결과", "Removed Background") \
                 .replace("투명 PNG 다운로드", "Download Transparent PNG") \
                 .replace("다른 이미지", "Upload Another") \
                 .replace("AI 모델 메모리 로드 중...", "Loading AI model into memory...") \
                 .replace("최초 1회 실행 시 모델 캐싱에 3~7초 소요됩니다.", "Initial run caches ~25MB model in browser memory.") \
                 .replace("🔒 100% 브라우저 연산 (서버 전송 없음)", "🔒 100% Client-Side Processing") \
                 .replace("이미지 파일만 지원합니다.", "Please select an image file.") \
                 .replace("배경 제거 중 오류가 발생했습니다. (HTTPS 또는 로컬 웹서버 환경인지 확인해주세요)", "Failed to remove background. Please ensure HTTPS or local server environment.") \
                 .replace('msgs = [\n      "AI 모델 메모리 로드 중...",\n      "이미지 피사체 분석 및 분리 중...",\n      "투명 배경 픽셀 다듬는 중...",\n      "거의 다 완성되었습니다!"\n    ];', 'msgs = [\n      "Loading AI model into memory...",\n      "Analyzing foreground subject...",\n      "Refining alpha transparency edges...",\n      "Almost ready!"\n    ];') \
                 .replace('lang="ko"', 'lang="en"')

def run():
    ko_path = os.path.join(ROOT_DIR, "ko", "background-remover.html")
    en_path = os.path.join(ROOT_DIR, "background-remover.html")

    with open(ko_path, "w", encoding="utf-8") as f:
        f.write(KO_HTML.strip())
    print("✅ Patched: ko/background-remover.html")

    with open(en_path, "w", encoding="utf-8") as f:
        f.write(EN_HTML.strip())
    print("✅ Patched: background-remover.html")

if __name__ == "__main__":
    run()