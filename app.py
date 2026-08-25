
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
    "Instagram": "https://www.instagram.com/gurjar_sahab_jii_/",
    "Streamlit": "https://share.streamlit.io/user/rishu6262",
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
        "link": "https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/"
    },
    {
        "name": "Customer Churn Prediction",
        "description": "Deep Learning application for customer churn prediction.",
        "link": "https://churnpredictionp19-evkjk4fzrarzujckjevh9h.streamlit.app/"
    },
    {
        "name": "Car Model Prediction",
        "description": "FastAPI + Machine Learning powered prediction system.",
        "link": "https://fastapicarmodelprediction-5wfyhdredwxwykagdh9ruo.streamlit.app/"
    },
    {
        "name": "Mental Health Prediction",
        "description": "Machine Learning based mental health prediction app.",
        "link": "https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/"
    },
    {
        "name": "Revenue Prediction",
        "description": "Business revenue forecasting using Machine Learning.",
        "link": "https://revenueprediction-jqtcydvcaxpcm3aj5ex2am.streamlit.app/"
    },
    {
        "name": "AI-Powered Resume Analyzer",
        "description": "Advanced ATS Resume Screening System using NLP, Machine Learning, Deep Learning, FastAPI, Streamlit and Render Deployment.",
        "link": "https://ai-poweredresumescheckerp19.streamlit.app/"
    }
]

# ======================
# CSS
# ======================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
}

div[data-testid="stSidebar"]{
    background:#111827;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
}

.hero{
    padding:35px;
    border-radius:25px;
    background:linear-gradient(
    135deg,
    rgba(59,130,246,0.25),
    rgba(168,85,247,0.20)
    );
    border:1px solid rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR
# ======================

with st.sidebar:
    st.title("🚀 Navigation")

    page = st.radio(
        "Select Section",
        [
            "Home",
            "About Me",
            "Projects",
            "Resumes",
            "Social Hub",
            "Contact"
        ]
    )

# ======================
# HOME
# ======================

if page == "Home":

    st.markdown("""
    <div class='hero'>
        <h1>🚀 Rishu Gurjar</h1>
        <h3>Data Engineer | Machine Learning Engineer | Python Developer</h3>
        <p>
        Building AI applications, deploying real-world ML projects,
        solving coding challenges and continuously learning modern technologies.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "🚀 Open to Internships, Part-Time work and Full-Time Opportunities."
    )

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Projects","8+")

    with col2:
        st.metric("Skills","10+")

    with col3:
        st.metric("Profiles","5+")

    with col4:
        st.metric("Status","Active")

# ======================
# ABOUT ME
# ======================

elif page == "About Me":

    st.title("👨‍💻 About Me")

    st.markdown("""
    ### Hello Sir/Ma'am,

->  My name is Rishu Gurjar, and I am currently pursuing a Bachelor's degree in Computer Science. I am passionate about Python Development, Machine Learning, Deep Learning, GenAI and Data Analytics.
    I have worked on several projects such as Placement Prediction, Agriculture Price Prediction, Weather Forecast Prediction, Customer Churn Prediction . Through these projects, I have gained practical experience in Python, SQL, PostgreSQL, Scikit-learn, and Streamlit.
    I am a quick learner, self-motivated, and enjoy solving real-world problems through technology. My goal is to become a skilled Python Developer and Data Scientist while continuously learning and contributing to innovative projects.
    I am excited about this opportunity and look forward to learning, growing, and adding value to your organization.


->  In the next five years, I see myself as a highly skilled Python Developer and Data Scientist with strong expertise in Machine Learning, Artificial Intelligence, and Data Analytics. I want to gain hands-on industry experience by working on real-world projects that solve meaningful business and social problems.
    As I grow professionally, I would like to take on more responsibilities, mentor junior team members, and contribute to the development of innovative AI solutions. I am particularly interested in using AI and data science to create practical applications that can make a positive impact.
    I am also passionate about education and technology. In the long term, I would like to contribute to improving AI awareness and education in India by sharing knowledge, building useful projects, and helping more students understand and adopt emerging technologies.
    Overall, my goal is to continuously learn, grow into a senior technical role, and contribute both to my organization’s success and to the advancement of AI in India.

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
    """)

    st.markdown("---")

    st.subheader("Technical Skills")

    st.write("""
    ✔ Python

    ✔ SQL

    ✔ Machine Learning

    ✔ Deep Learning

    ✔ GenAI

    ✔ NLP

    ✔ TensorFlow

    ✔ Pandas

    ✔ NumPy

    ✔ Seaborn

    ✔ Matplotlib

    ✔ Streamlit

    ✔ FastAPI

    ✔ Git & GitHub

    ✔ Data Analysis
    
    ✔ PowerBI

    ✔ MSexcle

    ✔ PostgreSQL
    """)

# ======================
# PROJECTS
# ======================

elif page == "Projects":

    st.title("🔥 Live Projects")

    cols = st.columns(2)

    for i, project in enumerate(PROJECTS):

        with cols[i % 2]:

            st.markdown(f"""
            <div class='card'>
                <h3>{project['name']}</h3>
                <p>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                f"Open {project['name']}",
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
        <div class='card'>
            <h2>📊 Data Engineer Resume</h2>
            <p>
            Focused on SQL, ETL, Data Pipelines,
            Data Warehousing, Python and Analytics.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "Download Data Engineer Resume",
            DATA_ENGINEER_RESUME
        )

    with col2:

        st.markdown("""
        <div class='card'>
            <h2>🤖 ML Engineer Resume</h2>
            <p>
            Focused on Machine Learning,
            Deep Learning, NLP,
            TensorFlow and Deployment.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "Download ML Engineer Resume",
            ML_ENGINEER_RESUME
        )

# ======================
# SOCIAL HUB
# ======================

elif page == "Social Hub":

    st.title("🌐 Social Profiles")

    col1,col2 = st.columns(2)

    with col1:
        st.link_button("LinkedIn", SOCIAL_LINKS["LinkedIn"])
        st.link_button("GitHub", SOCIAL_LINKS["GitHub"])
        st.link_button("LeetCode", SOCIAL_LINKS["LeetCode"])

    with col2:
        st.link_button("Instagram", SOCIAL_LINKS["Instagram"])
        st.link_button("Streamlit", SOCIAL_LINKS["Streamlit"])

# ======================
# CONTACT
# ======================

elif page == "Contact":

    st.title("📩 Contact Me")

    st.markdown("""
    <div class='card'>
        <h3>Let's Connect</h3>

        Available for:

        ✔ Internship Opportunities

        ✔ Machine Learning Projects

        ✔ Data Engineering Projects

        ✔ Collaboration & Networking
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Connect on LinkedIn",
        SOCIAL_LINKS["LinkedIn"]
    )
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````
