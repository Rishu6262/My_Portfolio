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

# with right:

#     st.image(
#         "assets/profile.png",
#         width=350
#     )

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# STATS
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='card'>
    <h1>25+</h1>
    <p>ALL_Projects</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h1>10+</h1>
    <p>Skills</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div class='card'>
    <h1>15+</h1>
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
SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/rishu-gurjar-58072a333/",
    "GitHub": "https://github.com/Rishu6262",
    "LeetCode": "https://leetcode.com/u/rishu6262/",
    "Instagram": "https://www.instagram.com/gurjar_sahab_jii_/?hl=en",
    "Streamlit": "https://share.streamlit.io/user/rishu6262",
    "Resume": "https://drive.google.com/file/d/1vPA-ThfKORseUxF6D9aLfHna8nGLVxjL/view?usp=sharing"
}

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🌐 Connect With Me</div>", unsafe_allow_html=True)

cols = st.columns(3)

for i, (name, url) in enumerate(SOCIAL_LINKS.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <a href="{url}" target="_blank" style="text-decoration:none;">
                <div class="social-card">
                    <h3>{name}</h3>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
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

🚀 Open To Internship

</div>
""", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    🚀 Journey
</div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="timeline">

<div class="timeline-card">
<h3>2024</h3>
Started Python Programming
</div>

<div class="timeline-card">
<h3>2025</h3>
Built Multiple Machine Learning Projects
</div>

<div class="timeline-card">
<h3>2026</h3>
Learning Data Engineering & FastAPI
</div>

<div class="timeline-card">
<h3>2027 Goal</h3>
Machine Learning Engineer Internship
</div>

</div>

""", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
🛠 Technical Skills
</div>
""", unsafe_allow_html=True)
