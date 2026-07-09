import streamlit as st
from pathlib import Path

# Streamlit 페이지 기본 설정 (넓은 레이아웃 및 제목 지정)
st.set_page_config(
    page_title="축구 승률 예측 챌린지 ⚽",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 파일 경로 정의 (app.py 기준 상대 경로 설정)
BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "htmls" / "index.html"

def load_html():
    """index.html 파일 존재 유무 확인 및 렌더링"""
    if not HTML_PATH.exists():
        # 파일이 없을 때 사용자 친절 안내 메시지 출력
        st.error("⚠️ HTML 파일을 찾을 수 없습니다.")
        st.info(
            f"**확인 필요한 경로:** `{HTML_PATH}`\n\n"
            "프로젝트 폴더 구조가 다음과 같이 구성되어 있는지 확인해 주세요:\n"
            "```text\n"
            "내-웹앱/\n"
            "├── app.py\n"
            "├── requirements.txt\n"
            "└── htmls/\n"
            "    └── index.html\n"
            "```"
        )
        return

    # HTML 파일 읽기 (UTF-8 인코딩 적용)
    try:
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Streamlit 화면에 HTML 웹앱 렌더링
        st.components.v1.html(html_content, height=900, scrolling=True)

    except Exception as e:
        st.error(f"⚠️ HTML 파일을 읽는 중 오류가 발생했습니다: {e}")

# 메인 실행부
if __name__ == "__main__":
    load_html()
