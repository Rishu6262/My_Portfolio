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
# ==========================================
# ABOUT ME
# ==========================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    👨 About Me
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.2, 1])

with left:

    st.markdown("""
<div class="glass">

### Hi, I'm **Rishu Gurjar** 👋

I'm a passionate **Python Developer**, **Machine Learning Engineer**, and **Data Engineering Enthusiast**.

I enjoy building AI-powered applications, solving real-world business problems, and continuously learning modern technologies.

Currently pursuing **B.Tech in Computer Science**, I'm actively looking for Internship opportunities where I can contribute while learning from experienced engineers.

🚀 My Goal is to become an AI Engineer capable of building production-ready intelligent systems.

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="glass">

## 🎯 Quick Info

🎓 B.Tech (Computer Science)

📍 Bhopal, India

💻 Python Developer

🤖 Machine Learning

📊 Data Analytics

🗄 PostgreSQL

☁ FastAPI

st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    Technical Skills
</div>
""", unsafe_allow_html=True)
