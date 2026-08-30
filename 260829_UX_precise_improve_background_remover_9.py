import os

ROOT_DIR = r"D:\Gemini_Files\Micro_SaaS_Toolkit"

KO_HTML_PATH = os.path.join(ROOT_DIR, "ko", "background-remover.html")
EN_HTML_PATH = os.path.join(ROOT_DIR, "background-remover.html")

TOAST_HTML = """
  <!-- Download Complete Toast Notification -->
  <div id="downloadToast" class="hidden fixed bottom-8 left-1/2 -translate-x-1/2 bg-emerald-500/95 text-slate-950 font-bold px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-2.5 z-50 transition-all transform duration-300">
    <svg class="w-5 h-5 text-slate-950" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
    <span id="toastMsg" class="text-sm">투명 PNG 다운로드가 완료되었습니다! (7.3MB)</span>
  </div>
"""

def patch_file(path, is_ko=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    msg = "투명 PNG 다운로드가 완료되었습니다!" if is_ko else "Transparent PNG downloaded successfully!"

    if 'id="downloadToast"' not in content:
        content = content.replace("</main>", f"</main>\n{TOAST_HTML}")

    # downloadBtn 이벤트 로직에 토스트 띄우기 삽입
    old_download_logic = """    downloadBtn.addEventListener('click', () => {
      if (!currentBlobUrl) return;
      const a = document.createElement('a');
      a.href = currentBlobUrl;
      a.download = `starsign16-nobg-${Date.now()}.png`;
      a.click();
    });"""

    new_download_logic = f"""    downloadBtn.addEventListener('click', () => {{
      if (!currentBlobUrl) return;
      const a = document.createElement('a');
      a.href = currentBlobUrl;
      a.download = `starsign16-nobg-${{Date.now()}}.png`;
      a.click();

      // OBS 녹화용 다운로드 완료 토스트 노출
      const toast = document.getElementById('downloadToast');
      const toastMsg = document.getElementById('toastMsg');
      if (toast) {{
        toastMsg.innerText = "{msg}";
        toast.classList.remove('hidden');
        setTimeout(() => {{
          toast.classList.add('hidden');
        }}, 3500);
      }}
    }});"""

    content = content.replace(old_download_logic, new_download_logic)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def run():
    patch_file(KO_HTML_PATH, is_ko=True)
    patch_file(EN_HTML_PATH, is_ko=False)
    print("✅ Successfully added Download Toast Notification for OBS recording!")

if __name__ == "__main__":
    run()