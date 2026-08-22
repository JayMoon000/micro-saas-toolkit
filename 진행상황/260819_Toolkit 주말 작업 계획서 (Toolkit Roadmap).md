# StarSign16 Toolkit 주말 작업 계획서 (Toolkit Roadmap)

## 📌 목표 요약
1. **글로벌 타겟팅을 위한 영문화 및 폴더 구조 개편** (영문 기본 루트 + 한글 `/ko/`)
2. **PC/모바일 가독성 최적화를 위한 다크/라이트 모드 토글 기능 추가**
3. **구글 글로벌 SEO 태그 및 상단 네비게이션(언어/테마) 연동**

---

## 1. 도메인 및 디렉토리 구조 개편 (SEO 최적화)


글로벌 트래픽(달러 수익)을 기본값으로 설정하고, 국내 유입을 서브 폴더로 분리합니다.

```text
[[tool.starsign16.com/](https://tool.starsign16.com/)] (Root)
│
├── index.html              <-- 영문 메인 (Default)
├── flowchart.html          <-- 영문 개별 툴 (영문 UI)
├── ... (기타 툴 영문 버전)
│
└── ko/                     <-- 한국어 버전 폴더
    ├── index.html          <-- 한글 메인
    ├── flowchart.html      <-- 한글 개별 툴
    └── ... (기타 툴 한글 버전)
	
	

SEO 헤더 필수 태그: 영문용/한글용


## 2. 상단 네비게이션 UI (언어 전환 + 테마 토글)

html
<header class="toolkit-header">
  <!-- 로고/타이틀 영역 -->
  <div class="logo">StarSign16 Toolkit</div>

  <!-- 컨트롤 영역 -->
  <div class="header-controls">
    <!-- 언어 전환 링크 (현재 영문 페이지 기준) -->
    <a href="/ko/index.html" class="lang-switch">한국어</a>
    
    <!-- 다크/라이트 모드 토글 버튼 -->
    <button id="themeToggle" class="theme-btn" aria-label="Toggle Theme">
      <span class="icon">☀️</span>
    </button>
  </div>
</header>

## 3. 다크/라이트 모드 구현 가이드 (Pure CSS & JS)

① CSS 변수 설정

CSS

/* 기본 테마: 다크 모드 (미드나잇 블루) */
:root {
  --bg-primary: #0b0f19;
  --bg-card: #151c2e;
  --text-main: #f3f4f6;
  --text-muted: #9ca3af;
  --border-color: #232d45;
  --accent-color: #6366f1;
}

/* 라이트 모드 오버라이드 */
[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-card: #ffffff;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --accent-color: #4f46e5;
}

/* 적용 예시 */
body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  transition: background-color 0.2s ease, color 0.2s ease;
}

.card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
}



② 초간단 자바스크립트 (로컬스토리지 저장 지원)

JavaScript

const themeToggleBtn = document.getElementById('themeToggle');
const currentTheme = localStorage.getItem('theme') || 'dark';

// 초기 테마 적용
if (currentTheme === 'light') {
  document.documentElement.setAttribute('data-theme', 'light');
  themeToggleBtn.querySelector('.icon').textContent = '🌙';
}

// 클릭 이벤트
themeToggleBtn.addEventListener('click', () => {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  if (isLight) {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'dark');
    themeToggleBtn.querySelector('.icon').textContent = '☀️';
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    themeToggleBtn.querySelector('.icon').textContent = '🌙';
  }
});


## 4. 주말 실행 순서 (Action Checklist)

[ ] 1단계: 폴더 분리

기존 HTML 파일들을 ko/ 폴더를 생성해 이동.

루트 경로에 복사본을 두고 메인 텍스트 및 UI 영문화(English Translation).

[ ] 2단계: 테마 시스템 적용

CSS에 변수(var(--bg-primary) 등) 정의 및 라이트 모드 속성 추가.

JS 테마 토글 스크립트 삽입.

[ ] 3단계: 헤더 네비게이션 연결

영문 ↔ 한글 상호 링크(<a>) 연결.

<head> SEO hreflang 메타태그 삽입.

[ ] 4단계: 테스트 및 배포

PC / 모바일 환경에서 테마 전환 및 링크 동작 검증.