import streamlit as st

st.set_page_config(
    page_title="Rishu Gurjar",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CSS
# -----------------------------
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Navbar
# -----------------------------

menu = st.columns(6)

pages = [
    "🏠 Home",
    "👨 About",
    "🛠 Skills",
    "🚀 Projects",
    "📄 Resume",
    "📞 Contact"
]

for col, page in zip(menu, pages):
    with col:
        st.markdown(
            f"<div class='nav-item'>{page}</div>",
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

left, right = st.columns([1.2,1])

with left:

    st.markdown("""
    <div class="hero-title">
        👋 Hello, I'm
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="name">
        Rishu Gurjar
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        Machine Learning Engineer <br>
        Python Developer <br>
        Data Engineer
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2 = st.columns(2)

    with c1:
        st.button("📄 Download Resume", use_container_width=True)

    with c2:
        st.button("💼 Hire Me", use_container_width=True)

with right:

    st.image(
        "assets/profile.png",
        width=350
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# STATS
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='card'>
    <h1>15+</h1>
    <p>Projects</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h1>20+</h1>
    <p>Skills</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div class='card'>
    <h1>250+</h1>
    <p>LeetCode Problems</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
    <h1>Open</h1>
    <p>Internship</p>
    </div>
    """, unsafe_allow_html=True)
