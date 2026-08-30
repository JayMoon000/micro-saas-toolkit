import os
import re

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

# 로딩 오버레이 HTML 컴포넌트
LOADING_OVERLAY_HTML = """
    <!-- Loading Overlay with Interactive Messages -->
    <div id="loadingOverlay" class="hidden fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex flex-col items-center justify-center p-4">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-8 max-w-md w-full text-center shadow-2xl flex flex-col items-center">
        <div class="relative w-16 h-16 mb-4">
          <div class="w-16 h-16 border-4 border-indigo-500/20 border-t-indigo-500 rounded-full animate-spin"></div>
          <div class="absolute inset-0 flex items-center justify-center text-indigo-400">
            <svg class="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          </div>
        </div>
        <h3 id="loadingStatusText" class="text-lg font-semibold text-slate-100 mb-2 transition-all duration-300">AI 모델을 브라우저에 불러오는 중...</h3>
        <p class="text-xs text-slate-400 mb-4">기기 사양에 따라 최초 3~8초 정도 소요될 수 있습니다.</p>
        <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-4">
          <div class="bg-gradient-to-r from-indigo-500 to-cyan-400 h-full w-2/3 animate-pulse"></div>
        </div>
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-800/80 border border-slate-700/50 text-[11px] text-indigo-300">
          <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
          100% 온디바이스 로컬 연산 (서버 전송 없음)
        </div>
      </div>
    </div>
"""

# 로딩 텍스트 제어 JS
LOADING_SCRIPT = """
<script>
  const statusMessagesKo = [
    "AI 모델을 브라우저에 불러오는 중...",
    "이미지 윤곽선을 정밀하게 분리하고 있어요...",
    "배경을 투명화 처리하고 있습니다. 거의 다 됐어요!",
    "마무리 픽셀 다듬는 중..."
  ];
  let msgIdx = 0;
  let msgInterval = null;

  function showProcessingLoading() {
    const overlay = document.getElementById('loadingOverlay');
    const textEl = document.getElementById('loadingStatusText');
    if (!overlay || !textEl) return;
    
    overlay.classList.remove('hidden');
    msgIdx = 0;
    textEl.innerText = statusMessagesKo[0];
    
    msgInterval = setInterval(() => {
      msgIdx = (msgIdx + 1) % statusMessagesKo.length;
      textEl.innerText = statusMessagesKo[msgIdx];
    }, 2200);
  }

  function hideProcessingLoading() {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) overlay.classList.add('hidden');
    if (msgInterval) clearInterval(msgInterval);
  }
</script>
"""

def patch_bg_remover(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미 로딩 오버레이가 들어간 경우 패스
    if 'id="loadingOverlay"' in content:
        print(f"⏩ Already patched: {os.path.basename(file_path)}")
        return

    # body 종료 직전에 오버레이 및 제어 스크립트 주입
    if "</body>" in content:
        content = content.replace("</body>", f"{LOADING_OVERLAY_HTML}\n{LOADING_SCRIPT}\n</body>")

    # 변환 시작/종료 함수 호출부 연동 보강
    # (일반적인 처리 시작 이벤트 시점 연결)
    content = re.sub(r'(\.removeBackground\(.*?\))', r'showProcessingLoading(); \1', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✨ Enhanced UX: {os.path.basename(file_path)}")

def run():
    target_files = [
        os.path.join(ROOT_DIR, "background-remover.html"),
        os.path.join(ROOT_DIR, "ko", "background-remover.html")
    ]
    for file_path in target_files:
        if os.path.exists(file_path):
            patch_bg_remover(file_path)

if __name__ == "__main__":
    run()