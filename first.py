import streamlit as st
import time

# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="박민희 | About Me",
    page_icon="✨",
    layout="centered"
)

# =========================================================
# 상태 저장
# =========================================================

if "card" not in st.session_state:
    st.session_state.card = 0

if "timer_minutes" not in st.session_state:
    st.session_state.timer_minutes = 25


# =========================================================
# 디자인 CSS
# =========================================================

st.markdown("""
<style>

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 5rem;
}

/* ---------- 상단 ---------- */

.small-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #8B7CF6;
    margin-bottom: 12px;
}

/* ---------- 카드뉴스 ---------- */

.news-card {
    min-height: 340px;
    padding: 42px;
    border-radius: 28px;

    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(139,124,246,0.25),
            transparent 35%
        ),
        linear-gradient(
            145deg,
            #F8F6FF,
            #EEEAFE
        );

    border: 1px solid #DED7FF;

    box-shadow:
        0px 20px 50px
        rgba(71,54,140,0.12);

    color: #171717;
}

.card-number {
    color: #7967E8;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

.card-title {
    color: #171717;
    font-size: 40px;
    font-weight: 850;
    line-height: 1.25;
    letter-spacing: -1.5px;

    margin-top: 35px;
    margin-bottom: 20px;
}

.highlight {
    color: #7662E8;
}

.card-desc {
    color: #4D4D55;
    font-size: 16px;
    line-height: 1.8;
}

.tag {
    display: inline-block;

    margin-top: 30px;
    margin-right: 5px;

    padding: 7px 13px;

    background: #FFFFFF;

    border:
        1px solid #DCD5FF;

    border-radius: 100px;

    color: #6858D4;

    font-size: 11px;
    font-weight: 700;
}

.page-dot {
    text-align: center;

    color: #8B7CF6;

    letter-spacing: 6px;

    margin-top: 15px;
    margin-bottom: 5px;
}


/* ---------- 타이머 ---------- */

.timer-section {
    margin-top: 65px;
}

.timer-heading {
    font-size: 30px;
    font-weight: 850;
    margin-bottom: 5px;
}

.timer-sub {
    font-size: 14px;
    color: #888895;
    margin-bottom: 25px;
}


/* 원형 타이머 */

.timer-circle {

    width: 260px;
    height: 260px;

    margin:
        30px auto
        30px auto;

    border-radius: 50%;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            circle,
            #111118 61%,
            transparent 62%
        ),
        conic-gradient(
            #8B7CF6 0deg,
            #B5AAFF 285deg,
            #34343F 285deg
        );

    box-shadow:
        0px 15px 50px
        rgba(118,98,232,0.25);
}

.timer-emoji {
    font-size: 28px;
    margin-bottom: 5px;
}

.timer-time {

    color: #FFFFFF;

    font-size: 50px;
    font-weight: 850;

    line-height: 1.1;

    letter-spacing: -2px;
}

.timer-status {

    color: #A8A8B4;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 2px;

    margin-top: 8px;
}


/* ---------- 버튼 ---------- */

.stButton > button {

    min-height: 48px;

    border-radius: 14px;

    font-weight: 700;

    transition: all 0.2s ease;
}

.stButton > button:hover {

    transform:
        translateY(-2px);
}


/* 숫자 input 숨김 등의 기본 여백 정리 */

div[data-testid="stVerticalBlock"] {
    gap: 0.7rem;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 카드뉴스 데이터
# =========================================================

cards = [

"""<div class="news-card">
<div class="card-number">01 / HELLO</div>
<div class="card-title">안녕하세요.<br><span class="highlight">박민희</span>입니다. 👋</div>
<div class="card-desc">디자인하고, 가르치고,<br>새로운 아이디어를 직접 실험하는 사람입니다.</div>
<span class="tag">DESIGNER</span>
<span class="tag">EDUCATOR</span>
<span class="tag">LOCAL CREATOR</span>
</div>""",

"""<div class="news-card">
<div class="card-number">02 / ABOUT ME</div>
<div class="card-title">저는 <span class="highlight">관찰하고</span><br>만드는 사람입니다.</div>
<div class="card-desc">사람과 공간을 관찰하고,<br>그 안에서 발견한 이야기를<br>디자인과 콘텐츠로 만드는 것을 좋아합니다.</div>
<span class="tag"># 디자인</span>
<span class="tag"># 콘텐츠</span>
<span class="tag"># 교육</span>
<span class="tag"># 로컬</span>
</div>""",

"""<div class="news-card">
<div class="card-number">03 / NOW</div>
<div class="card-title">요즘은 동네를<br><span class="highlight">PLAY</span>하는 방법을<br>고민합니다. 🎮</div>
<div class="card-desc"><b>LOCAL QUEST</b><br><br>동네의 상점·골목·시장·문화공간을<br>게임처럼 탐험할 수 있는 QUEST로 바꾸는<br>로컬 프로젝트 플랫폼을 기획하고 있습니다.</div>
<span class="tag">LOCAL QUEST</span>
<span class="tag">PLAY THE CITY</span>
</div>"""

]


# =========================================================
# 자기소개 카드뉴스
# =========================================================

st.markdown(
    '<div class="small-label">ABOUT ME ✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    cards[st.session_state.card],
    unsafe_allow_html=True
)


# 페이지 표시 점

dots = ""

for i in range(len(cards)):

    if i == st.session_state.card:
        dots += "● "
    else:
        dots += "○ "


st.markdown(
    f'<div class="page-dot">{dots}</div>',
    unsafe_allow_html=True
)


# 이전 / 다음 버튼

left, space, right = st.columns(
    [1, 2.2, 1]
)

with left:

    if st.button(
        "← 이전",
        use_container_width=True
    ):

        st.session_state.card = (
            st.session_state.card - 1
        ) % len(cards)

        st.rerun()


with right:

    if st.button(
        "다음 →",
        use_container_width=True
    ):

        st.session_state.card = (
            st.session_state.card + 1
        ) % len(cards)

        st.rerun()


# =========================================================
# 집중 타이머 제목
# =========================================================

st.markdown(
    '<div class="timer-section">'
    '<div class="small-label">FOCUS MODE ✦</div>'
    '<div class="timer-heading">집중 타이머</div>'
    '<div class="timer-sub">지금 필요한 집중 시간을 선택하세요.</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 시간 선택
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "☕ 5분 · QUICK",
        use_container_width=True
    ):

        st.session_state.timer_minutes = 5
        st.rerun()


with col2:

    if st.button(
        "⚡ 25분 · FOCUS",
        use_container_width=True
    ):

        st.session_state.timer_minutes = 25
        st.rerun()


with col3:

    if st.button(
        "🔥 50분 · DEEP",
        use_container_width=True
    ):

        st.session_state.timer_minutes = 50
        st.rerun()


# =========================================================
# 타이머 표시
# =========================================================

timer_area = st.empty()


def draw_timer(minutes, seconds, status):

    timer_html = (
        '<div class="timer-circle">'
        '<div class="timer-emoji">⚡</div>'
        f'<div class="timer-time">{minutes:02d}:{seconds:02d}</div>'
        f'<div class="timer-status">{status}</div>'
        '</div>'
    )

    timer_area.markdown(
        timer_html,
        unsafe_allow_html=True
    )


draw_timer(
    st.session_state.timer_minutes,
    0,
    "READY TO FOCUS"
)


# =========================================================
# 시작 버튼
# =========================================================

if st.button(
    "▶  FOCUS START",
    use_container_width=True,
    type="primary"
):

    total_seconds = (
        st.session_state.timer_minutes * 60
    )

    for remaining in range(
        total_seconds,
        -1,
        -1
    ):

        mins = remaining // 60
        secs = remaining % 60

        draw_timer(
            mins,
            secs,
            "FOCUSING"
        )

        if remaining > 0:
            time.sleep(1)

    st.balloons()

    st.success(
        "집중 완료! ☕ 잠깐 쉬어가세요."
    )