
# import streamlit as st

# st.set_page_config(
#     page_title="Rishu Portfolio Hub",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ======================
# # SOCIAL LINKS
# # ======================

# SOCIAL_LINKS = {
#     "LinkedIn": "https://www.linkedin.com/in/rishu-gurjar-58072a333/",
#     "GitHub": "https://github.com/Rishu6262",
#     "LeetCode": "https://leetcode.com/u/rishu6262/",
#     "Instagram": "https://www.instagram.com/rishu_gurjar_010/?hl=en",
#     "Streamlit": "https://share.streamlit.io/user/rishu6262",
# }

# # ======================
# # RESUME LINKS
# # ======================

# DATA_ENGINEER_RESUME = "https://drive.google.com/file/d/1HgS0VpbZAfTpZfOcVhtnbNXS-0bxpj-q/view?usp=sharing"
# ML_ENGINEER_RESUME = "https://drive.google.com/file/d/1kPAN0uwjscDoALTXYP2Et731G1Ff70MU/view?usp=sharing"

# # ======================
# # PROJECTS
# # ======================

# PROJECTS = [
#     {
#         "name": "Email Spam Classifier",
#         "description": "Deep Learning and NLP based email spam detection system.",
#         "link": "https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/"
#     },
#     {
#         "name": "Customer Churn Prediction",
#         "description": "Deep Learning application for customer churn prediction.",
#         "link": "https://churnpredictionp19-evkjk4fzrarzujckjevh9h.streamlit.app/"
#     },
#     {
#         "name": "Car Model Prediction",
#         "description": "FastAPI + Machine Learning powered prediction system.",
#         "link": "https://fastapicarmodelprediction-5wfyhdredwxwykagdh9ruo.streamlit.app/"
#     },
#     {
#         "name": "Mental Health Prediction",
#         "description": "Machine Learning based mental health prediction app.",
#         "link": "https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/"
#     },
#     {
#         "name": "Revenue Prediction",
#         "description": "Business revenue forecasting using Machine Learning.",
#         "link": "https://revenueprediction-jqtcydvcaxpcm3aj5ex2am.streamlit.app/"
#     },
#     {
#         "name": "AI-Powered Resume Analyzer",
#         "description": "Advanced ATS Resume Screening System using NLP, Machine Learning, Deep Learning, FastAPI, Streamlit and Render Deployment.",
#         "link": "https://ai-poweredresumescheckerp19.streamlit.app/"
#     }
# ]

# # ======================
# # CSS
# # ======================

# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(135deg,#0f172a,#1e293b);
#     color:white;
# }

# div[data-testid="stSidebar"]{
#     background:#111827;
# }

# .card{
#     background:rgba(255,255,255,0.08);
#     padding:20px;
#     border-radius:20px;
#     margin-bottom:20px;
#     border:1px solid rgba(255,255,255,0.15);
#     backdrop-filter: blur(12px);
# }

# .hero{
#     padding:35px;
#     border-radius:25px;
#     background:linear-gradient(
#     135deg,
#     rgba(59,130,246,0.25),
#     rgba(168,85,247,0.20)
#     );
#     border:1px solid rgba(255,255,255,0.15);
# }

# </style>
# """, unsafe_allow_html=True)

# # ======================
# # SIDEBAR
# # ======================

# with st.sidebar:
#     st.title("🚀 Navigation")

#     page = st.radio(
#         "Select Section",
#         [
#             "Home",
#             "About Me",
#             "Projects",
#             "Resumes",
#             "Social Hub",
#             "Contact"
#         ]
#     )

# # ======================
# # HOME
# # ======================

# if page == "Home":

#     st.markdown("""
#     <div class='hero'>
#         <h1>🚀 Rishu Gurjar</h1>
#         <h3>Data Engineer | Machine Learning Engineer | Python Developer</h3>
#         <p>
#         Building AI applications, deploying real-world ML projects,
#         solving coding challenges and continuously learning modern technologies.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.info(
#         "🚀 Open to Internships, Part-Time work and Full-Time Opportunities."
#     )

#     col1,col2,col3,col4 = st.columns(4)

#     with col1:
#         st.metric("Projects","8+")

#     with col2:
#         st.metric("Skills","10+")

#     with col3:
#         st.metric("Profiles","5+")

#     with col4:
#         st.metric("Status","Active")

# # ======================
# # ABOUT ME
# # ======================

# elif page == "About Me":

#     st.title("👨‍💻 About Me")

#     st.markdown("""
#     ### Hello Sir/Ma'am,

# ->  My name is Rishu Gurjar, and I am currently pursuing a Bachelor's degree in Computer Science. I am passionate about Python Development, Machine Learning, Deep Learning, GenAI and Data Analytics.
#     I have worked on several projects such as Placement Prediction, Agriculture Price Prediction, Weather Forecast Prediction, Customer Churn Prediction . Through these projects, I have gained practical experience in Python, SQL, PostgreSQL, Scikit-learn, and Streamlit.
#     I am a quick learner, self-motivated, and enjoy solving real-world problems through technology. My goal is to become a skilled Python Developer and Data Scientist while continuously learning and contributing to innovative projects.
#     I am excited about this opportunity and look forward to learning, growing, and adding value to your organization.


# ->  In the next five years, I see myself as a highly skilled Python Developer and Data Scientist with strong expertise in Machine Learning, Artificial Intelligence, and Data Analytics. I want to gain hands-on industry experience by working on real-world projects that solve meaningful business and social problems.
#     As I grow professionally, I would like to take on more responsibilities, mentor junior team members, and contribute to the development of innovative AI solutions. I am particularly interested in using AI and data science to create practical applications that can make a positive impact.
#     I am also passionate about education and technology. In the long term, I would like to contribute to improving AI awareness and education in India by sharing knowledge, building useful projects, and helping more students understand and adopt emerging technologies.
#     Overall, my goal is to continuously learn, grow into a senior technical role, and contribute both to my organization’s success and to the advancement of AI in India.

# ->  One of my weaknesses is that sometimes I spend extra time on a task because I want the result to be as accurate and high-quality as possible. While this helps me maintain good quality, I realized that it can sometimes affect my speed.
#     To improve this, I have started focusing more on time management and task prioritization. I set clear deadlines for myself and break larger tasks into smaller milestones. This helps me balance both quality and efficiency.
#     I believe continuous improvement is important, and I am actively working on this area.

# ->  My biggest strength is my problem-solving ability. I enjoy analyzing problems and finding effective solutions. While working on my machine learning projects, I often faced challenges related to data cleaning, feature selection, and model accuracy. Instead of giving up, I researched different approaches, experimented with multiple models, and improved the overall performance of the projects.
#     Another strength is that I am a quick learner. Technology is constantly evolving, and I enjoy learning new tools and concepts. For example, while building my projects, I learned Python libraries such as Pandas, NumPy, Scikit-learn, and also explored PostgreSQL and Streamlit on my own.
#     I am also a dedicated and disciplined person. Once I commit to a task, I make sure to complete it on time and with quality. Additionally, I work well in teams, communicate effectively, and am always open to feedback because 
#     I believe continuous improvement is important for professional growth."
    
#     I have built multiple real-world projects including:

#     - Email Spam Classifier
#     - Salary Prediction System
#     - Customer Churn Prediction
#     - Revenue Prediction
#     - Mental Health Prediction
#     - AI resume Cheacker 
#     - More Project like this

#     I enjoy solving real-world problems through data-driven solutions and
#     continuously improving my skills in AI, Data Engineering and Software Development.
#     """)

#     st.markdown("---")

#     st.subheader("Technical Skills")

#     st.write("""
#     ✔ Python

#     ✔ SQL

#     ✔ Machine Learning

#     ✔ Deep Learning

#     ✔ GenAI

#     ✔ NLP

#     ✔ TensorFlow

#     ✔ Pandas

#     ✔ NumPy

#     ✔ Seaborn

#     ✔ Matplotlib

#     ✔ Streamlit

#     ✔ FastAPI

#     ✔ Git & GitHub

#     ✔ Data Analysis
    
#     ✔ PowerBI

#     ✔ MSexcle

#     ✔ PostgreSQL
#     """)

# # ======================
# # PROJECTS
# # ======================

# elif page == "Projects":

#     st.title("🔥 Live Projects")

#     cols = st.columns(2)

#     for i, project in enumerate(PROJECTS):

#         with cols[i % 2]:

#             st.markdown(f"""
#             <div class='card'>
#                 <h3>{project['name']}</h3>
#                 <p>{project['description']}</p>
#             </div>
#             """, unsafe_allow_html=True)

#             st.link_button(
#                 f"Open {project['name']}",
#                 project["link"]
#             )

# # ======================
# # RESUMES
# # ======================

# elif page == "Resumes":

#     st.title("📄 My Resumes")

#     col1,col2 = st.columns(2)

#     with col1:

#         st.markdown("""
#         <div class='card'>
#             <h2>📊 Data Engineer Resume</h2>
#             <p>
#             Focused on SQL, ETL, Data Pipelines,
#             Data Warehousing, Python and Analytics.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.link_button(
#             "Download Data Engineer Resume",
#             DATA_ENGINEER_RESUME
#         )

#     with col2:

#         st.markdown("""
#         <div class='card'>
#             <h2>🤖 ML Engineer Resume</h2>
#             <p>
#             Focused on Machine Learning,
#             Deep Learning, NLP,
#             TensorFlow and Deployment.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.link_button(
#             "Download ML Engineer Resume",
#             ML_ENGINEER_RESUME
#         )

# # ======================
# # SOCIAL HUB
# # ======================

# elif page == "Social Hub":

#     st.title("🌐 Social Profiles")

#     col1,col2 = st.columns(2)

#     with col1:
#         st.link_button("LinkedIn", SOCIAL_LINKS["LinkedIn"])
#         st.link_button("GitHub", SOCIAL_LINKS["GitHub"])
#         st.link_button("LeetCode", SOCIAL_LINKS["LeetCode"])

#     with col2:
#         st.link_button("Instagram", SOCIAL_LINKS["Instagram"])
#         st.link_button("Streamlit", SOCIAL_LINKS["Streamlit"])

# # ======================
# # CONTACT
# # ======================

# elif page == "Contact":

#     st.title("📩 Contact Me")

#     st.markdown("""
#     <div class='card'>
#         <h3>Let's Connect</h3>

#         Available for:

#         ✔ Internship Opportunities

#         ✔ Machine Learning Projects

#         ✔ Data Engineering Projects

#         ✔ Collaboration & Networking
#     </div>
#     """, unsafe_allow_html=True)

#     st.link_button(
#         "Connect on LinkedIn",
#         SOCIAL_LINKS["LinkedIn"]
#     )
# # ``````````````````````````````````````````````````````````````````````````````````````````````````````````

import streamlit as st

st.set_page_config(
    page_title="Rishu Portfolio Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# SOCIAL LINKS
# ======================

SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/rishu-gurjar-58072a333/",
    "GitHub": "https://github.com/Rishu6262",
    "LeetCode": "https://leetcode.com/u/rishu6262/",
    "Instagram": "https://www.instagram.com/rishu_gurjar_010/?hl=en",
    "Streamlit": "https://share.streamlit.io/user/rishu6262",
}

SOCIAL_ICONS = {
    "LinkedIn": "💼",
    "GitHub": "🐙",
    "LeetCode": "🧩",
    "Instagram": "📸",
    "Streamlit": "🎈",
}

# ======================
# RESUME LINKS
# ======================

DATA_ENGINEER_RESUME = "https://drive.google.com/file/d/1HgS0VpbZAfTpZfOcVhtnbNXS-0bxpj-q/view?usp=sharing"
ML_ENGINEER_RESUME = "https://drive.google.com/file/d/1kPAN0uwjscDoALTXYP2Et731G1Ff70MU/view?usp=sharing"

# ======================
# PROJECTS
# ======================

PROJECTS = [
    {
        "name": "Email Spam Classifier",
        "description": "Deep Learning and NLP based email spam detection system.",
        "link": "https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/",
        "icon": "📧",
        "color": "#6366F1"
    },
    {
        "name": "Customer Churn Prediction",
        "description": "Deep Learning application for customer churn prediction.",
        "link": "https://churnpredictionp19-evkjk4fzrarzujckjevh9h.streamlit.app/",
        "icon": "📉",
        "color": "#14B8A6"
    },
    {
        "name": "Car Model Prediction",
        "description": "FastAPI + Machine Learning powered prediction system.",
        "link": "https://fastapicarmodelprediction-5wfyhdredwxwykagdh9ruo.streamlit.app/",
        "icon": "🚗",
        "color": "#F59E0B"
    },
    {
        "name": "Mental Health Prediction",
        "description": "Machine Learning based mental health prediction app.",
        "link": "https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/",
        "icon": "🧠",
        "color": "#EC4899"
    },
    {
        "name": "Revenue Prediction",
        "description": "Business revenue forecasting using Machine Learning.",
        "link": "https://revenueprediction-jqtcydvcaxpcm3aj5ex2am.streamlit.app/",
        "icon": "💰",
        "color": "#22C55E"
    },
    {
        "name": "AI-Powered Resume Analyzer",
        "description": "Advanced ATS Resume Screening System using NLP, Machine Learning, Deep Learning, FastAPI, Streamlit and Render Deployment.",
        "link": "https://ai-poweredresumescheckerp19.streamlit.app/",
        "icon": "📄",
        "color": "#8B5CF6"
    }
]

# ======================
# CSS  —  Light "data-aurora" theme
# Palette: #F7F9FC bg · #FFFFFF cards · #4F46E5 indigo ·
#          #14B8A6 teal · #F59E0B amber · #0F172A ink text
# ======================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 12%, rgba(99,102,241,0.14), transparent 40%),
        radial-gradient(circle at 92% 18%, rgba(20,184,166,0.14), transparent 40%),
        radial-gradient(circle at 50% 100%, rgba(245,158,11,0.10), transparent 45%),
        #F7F9FC;
    color: #0F172A;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
}

/* ---------- Sidebar ---------- */
div[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #4F46E5 0%, #6D28D9 55%, #0F766E 100%);
}
div[data-testid="stSidebar"] * {
    color: #F8FAFC !important;
}
div[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.08);
    padding: 10px 14px;
    border-radius: 14px;
    margin-bottom: 8px;
    display: block;
    transition: all 0.2s ease-in-out;
    border: 1px solid rgba(255,255,255,0.12);
}
div[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.20);
    transform: translateX(4px);
}

/* ---------- Cards ---------- */
.card{
    background: #FFFFFF;
    padding: 22px 24px;
    border-radius: 20px;
    margin-bottom: 20px;
    border: 1px solid #E7EBF3;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover{
    transform: translateY(-4px);
    box-shadow: 0 16px 32px rgba(79, 70, 229, 0.15);
}

/* ---------- Hero ---------- */
.hero{
    padding: 42px;
    border-radius: 28px;
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #14B8A6 100%);
    color: #FFFFFF;
    box-shadow: 0 20px 40px rgba(79,70,229,0.25);
}
.hero h1, .hero h3, .hero p{
    color: #FFFFFF !important;
}

/* ---------- Skill Pills ---------- */
.pill{
    display: inline-block;
    padding: 8px 16px;
    margin: 5px;
    border-radius: 999px;
    background: linear-gradient(135deg, #EEF2FF, #E0F2FE);
    border: 1px solid #C7D2FE;
    color: #3730A3;
    font-weight: 600;
    font-size: 14px;
}

/* ---------- Metric tiles ---------- */
div[data-testid="stMetric"]{
    background: #FFFFFF;
    border-radius: 18px;
    padding: 14px 10px;
    border: 1px solid #E7EBF3;
    box-shadow: 0 6px 18px rgba(15,23,42,0.05);
}

/* ---------- Buttons / link buttons ---------- */
.stLinkButton a{
    border-radius: 12px !important;
    font-weight: 600 !important;
    border: none !important;
    background: linear-gradient(135deg, #4F46E5, #14B8A6) !important;
    color: #FFFFFF !important;
    box-shadow: 0 6px 16px rgba(79,70,229,0.25);
}
.stLinkButton a:hover{
    filter: brightness(1.08);
}

/* ---------- Section divider ---------- */
hr{
    border: none;
    border-top: 2px dashed #C7D2FE;
    margin: 24px 0;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR
# ======================

with st.sidebar:
    st.markdown("## 🚀 Navigation")
    st.caption("Explore my portfolio ✨")

    page = st.radio(
        "Select Section",
        [
            "Home",
            "About Me",
            "Projects",
            "Resumes",
            "Social Hub",
            "Contact"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    for name, url in SOCIAL_LINKS.items():
        st.markdown(f"{SOCIAL_ICONS[name]} [{name}]({url})")

# ======================
# HOME
# ======================

if page == "Home":

    st.markdown("""
    <div class='hero'>
        <h1>🚀 Rishu Gurjar</h1>
        <h3>📊 Data Engineer | 🤖 Machine Learning Engineer | 🐍 Python Developer</h3>
        <p>
        Building AI applications, deploying real-world ML projects,
        solving coding challenges and continuously learning modern technologies.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.info(
        "🚀 Open to Internships, Part-Time work and Full-Time Opportunities."
    )

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("📁 Projects","8+")

    with col2:
        st.metric("🛠️ Skills","10+")

    with col3:
        st.metric("🌐 Profiles","5+")

    with col4:
        st.metric("⚡ Status","Active")

# ======================
# ABOUT ME
# ======================

elif page == "About Me":

    st.title("👨‍💻 About Me")

    st.markdown("""
    <div class='card'>

    ### Hello Sir/Ma'am,

->  My name is Rishu Gurjar, and I am currently pursuing a Bachelor's degree in Computer Science. I am passionate about Python Development, Machine Learning, Deep Learning, GenAI and Data Analytics.
    I have worked on several projects such as Placement Prediction, Agriculture Price Prediction, Weather Forecast Prediction, Customer Churn Prediction . Through these projects, I have gained practical experience in Python, SQL, PostgreSQL, Scikit-learn, and Streamlit.
    I am a quick learner, self-motivated, and enjoy solving real-world problems through technology. My goal is to become a skilled Python Developer and Data Scientist while continuously learning and contributing to innovative projects.
    I am excited about this opportunity and look forward to learning, growing, and adding value to your organization.


->  In the next five years, I see myself as a highly skilled Python Developer and Data Scientist with strong expertise in Machine Learning, Artificial Intelligence, and Data Analytics. I want to gain hands-on industry experience by working on real-world projects that solve meaningful business and social problems.
    As I grow professionally, I would like to take on more responsibilities, mentor junior team members, and contribute to the development of innovative AI solutions. I am particularly interested in using AI and data science to create practical applications that can make a positive impact.
    I am also passionate about education and technology. In the long term, I would like to contribute to improving AI awareness and education in India by sharing knowledge, building useful projects, and helping more students understand and adopt emerging technologies.
    Overall, my goal is to continuously learn, grow into a senior technical role, and contribute both to my organization's success and to the advancement of AI in India.

->  One of my weaknesses is that sometimes I spend extra time on a task because I want the result to be as accurate and high-quality as possible. While this helps me maintain good quality, I realized that it can sometimes affect my speed.
    To improve this, I have started focusing more on time management and task prioritization. I set clear deadlines for myself and break larger tasks into smaller milestones. This helps me balance both quality and efficiency.
    I believe continuous improvement is important, and I am actively working on this area.

->  My biggest strength is my problem-solving ability. I enjoy analyzing problems and finding effective solutions. While working on my machine learning projects, I often faced challenges related to data cleaning, feature selection, and model accuracy. Instead of giving up, I researched different approaches, experimented with multiple models, and improved the overall performance of the projects.
    Another strength is that I am a quick learner. Technology is constantly evolving, and I enjoy learning new tools and concepts. For example, while building my projects, I learned Python libraries such as Pandas, NumPy, Scikit-learn, and also explored PostgreSQL and Streamlit on my own.
    I am also a dedicated and disciplined person. Once I commit to a task, I make sure to complete it on time and with quality. Additionally, I work well in teams, communicate effectively, and am always open to feedback because 
    I believe continuous improvement is important for professional growth."
    
    I have built multiple real-world projects including:

    - Email Spam Classifier
    - Salary Prediction System
    - Customer Churn Prediction
    - Revenue Prediction
    - Mental Health Prediction
    - AI resume Cheacker 
    - More Project like this

    I enjoy solving real-world problems through data-driven solutions and
    continuously improving my skills in AI, Data Engineering and Software Development.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🛠️ Technical Skills")

    skills = [
        "🐍 Python", "🗄️ SQL", "🤖 Machine Learning", "🧠 Deep Learning",
        "✨ GenAI", "💬 NLP", "🔶 TensorFlow", "🐼 Pandas", "🔢 NumPy",
        "📈 Seaborn", "📊 Matplotlib", "🎈 Streamlit", "⚡ FastAPI",
        "🔧 Git & GitHub", "📉 Data Analysis", "📘 PowerBI", "📗 MSexcle",
        "🐘 PostgreSQL"
    ]

    st.markdown(
        "".join(f"<span class='pill'>{s}</span>" for s in skills),
        unsafe_allow_html=True
    )

# ======================
# PROJECTS
# ======================

elif page == "Projects":

    st.title("🔥 Live Projects")

    cols = st.columns(2)

    for i, project in enumerate(PROJECTS):

        with cols[i % 2]:

            st.markdown(f"""
            <div class='card' style='border-left: 6px solid {project["color"]};'>
                <h3>{project['icon']} {project['name']}</h3>
                <p>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                f"🔗 Open {project['name']}",
                project["link"]
            )

# ======================
# RESUMES
# ======================

elif page == "Resumes":

    st.title("📄 My Resumes")

    col1,col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class='card' style='border-left: 6px solid #4F46E5;'>
            <h2>📊 Data Engineer Resume</h2>
            <p>
            Focused on SQL, ETL, Data Pipelines,
            Data Warehousing, Python and Analytics.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "⬇️ Download Data Engineer Resume",
            DATA_ENGINEER_RESUME
        )

    with col2:

        st.markdown("""
        <div class='card' style='border-left: 6px solid #14B8A6;'>
            <h2>🤖 ML Engineer Resume</h2>
            <p>
            Focused on Machine Learning,
            Deep Learning, NLP,
            TensorFlow and Deployment.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "⬇️ Download ML Engineer Resume",
            ML_ENGINEER_RESUME
        )

# ======================
# SOCIAL HUB
# ======================

elif page == "Social Hub":

    st.title("🌐 Social Profiles")

    col1,col2 = st.columns(2)

    with col1:
        st.link_button(f"{SOCIAL_ICONS['LinkedIn']} LinkedIn", SOCIAL_LINKS["LinkedIn"])
        st.link_button(f"{SOCIAL_ICONS['GitHub']} GitHub", SOCIAL_LINKS["GitHub"])
        st.link_button(f"{SOCIAL_ICONS['LeetCode']} LeetCode", SOCIAL_LINKS["LeetCode"])

    with col2:
        st.link_button(f"{SOCIAL_ICONS['Instagram']} Instagram", SOCIAL_LINKS["Instagram"])
        st.link_button(f"{SOCIAL_ICONS['Streamlit']} Streamlit", SOCIAL_LINKS["Streamlit"])

# ======================
# CONTACT
# ======================

elif page == "Contact":

    st.title("📩 Contact Me")

    st.markdown("""
    <div class='card'>
        <h3>🤝 Let's Connect</h3>

        Available for:

        ✔ Internship Opportunities

        ✔ Machine Learning Projects

        ✔ Data Engineering Projects

        ✔ Collaboration & Networking
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "💼 Connect on LinkedIn",
        SOCIAL_LINKS["LinkedIn"]
    )
