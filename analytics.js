/**
 * StarSign16 Toolkit - Zero-Cost Analytics Tracker
 * GA4 & Cloudflare Web Analytics 자동 이벤트 바인딩
 */

// Google Analytics 4 (GA4) 연동
const GA_MEASUREMENT_ID = 'G-6LFL2P1WRN';

// Google tag (gtag.js) 스크립트 로드
const gaScript = document.createElement('script');
gaScript.async = true;
gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
document.head.appendChild(gaScript);

// dataLayer 초기화 및 설정
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', GA_MEASUREMENT_ID);

// 2. 커스텀 액션 이벤트 로깅 함수
function trackToolEvent(toolName, actionName) {
    if (typeof gtag === 'function' && GA_MEASUREMENT_ID !== 'G-XXXXXXXXXX') {
        gtag('event', 'tool_action', {
            'tool_name': toolName,
            'action_type': actionName
        });
    }
    console.log(`[Analytics] Tool: ${toolName} | Action: ${actionName}`);
}

// 3. 페이지 내 주요 다운로드/변환 버튼 자동 추적
document.addEventListener('DOMContentLoaded', () => {
    // 다운로드 및 등록 버튼 추적
    const trackTargets = [
        { selector: 'button[onclick*="downloadPNG"]', tool: 'flowchart_maker', action: 'download_png' },
        { selector: 'button[onclick*="downloadSVG"]', tool: 'flowchart_maker', action: 'download_svg' },
        { selector: 'button[onclick*="generateEPUB"]', tool: 'epub_maker', action: 'download_epub' },
        { selector: 'button[onclick*="openGoogleCalendar"]', tool: 'fast_calendar', action: 'add_to_calendar' },
        { selector: 'button[onclick*="downloadChartPNG"]', tool: 'visualizer', action: 'download_chart' },
        { selector: '#copy-btn', tool: 'text_utility', action: 'copy_result' }
    ];

    trackTargets.forEach(({ selector, tool, action }) => {
        const el = document.querySelector(selector);
        if (el) {
            el.addEventListener('click', () => trackToolEvent(tool, action));
        }
    });
});