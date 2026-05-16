# import streamlit as st

# st.set_page_config(
#     page_title='Rishu Portfolio Hub',
#     page_icon='🚀',
#     layout='wide',
#     initial_sidebar_state='expanded'
# )

# SOCIAL_LINKS = {
#     'LinkedIn': 'https://www.linkedin.com/in/rishu-gurjar-58072a333/',
#     'GitHub': 'https://github.com/Rishu6262',
#     'LeetCode': 'https://leetcode.com/u/rishu6262/',
#     'Instagram': 'https://www.instagram.com/gurjar_sahab_jii_/?hl=en',
#     'Streamlit': 'https://share.streamlit.io/user/rishu6262',
#     'Resume': 'https://drive.google.com/file/d/1vPA-ThfKORseUxF6D9aLfHna8nGLVxjL/view?usp=sharing'
# }

# PROJECTS = [
#     {
#         'name': 'Project 1',
#         'description': 'Live deployed Streamlit ML application.',
#         'link': 'https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/'
#     },
#     {
#         'name': 'Project 2',
#         'description': 'Machine Learning deployment project.',
#         'link': 'https://mlprojectp19-hdbfn8anguoftpumgrzbrl.streamlit.app/'
#     }
# ]

# st.markdown('''
# <style>
# .stApp {
#     background: linear-gradient(135deg, #0f172a, #1e293b);
#     color: white;
# }
# div[data-testid="stSidebar"] {
#     background: #111827;
# }
# .block-container {
#     padding-top: 2rem;
# }
# .card {
#     background: rgba(255,255,255,0.08);
#     padding: 20px;
#     border-radius: 18px;
#     backdrop-filter: blur(12px);
#     margin-bottom: 20px;
#     border: 1px solid rgba(255,255,255,0.15);
# }
# </style>
# ''', unsafe_allow_html=True)

# with st.sidebar:
#     st.title('🚀 Navigation')
#     page = st.radio('Select Section', ['Home', 'Projects', 'Social Hub', 'Contact'])

# if page == 'Home':
#     st.title('Rishu Gurjar')
#     st.subheader('Data Science | ML Engineer | Python Developer')
#     st.markdown('''
#     <div class='card'>
#     Welcome to my personal portfolio hub. Explore my social profiles, live projects, resume, and professional journey.
#     </div>
#     ''', unsafe_allow_html=True)

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric('Projects', '2+')
#     with col2:
#         st.metric('Platforms', '5+')
#     with col3:
#         st.metric('Status', 'Active')

# if page == 'Projects':
#     st.title('🔥 Live Projects')
#     for project in PROJECTS:
#         st.markdown(f"""
#         <div class='card'>
#         <h3>{project['name']}</h3>
#         <p>{project['description']}</p>
#         </div>
#         """, unsafe_allow_html=True)
#         st.link_button(f"Open {project['name']}", project['link'])

# if page == 'Social Hub':
#     st.title('🌐 Social Hub')
#     cols = st.columns(2)
#     items = list(SOCIAL_LINKS.items())
#     for i, (name, link) in enumerate(items):
#         with cols[i % 2]:
#             st.link_button(name, link)

# if page == 'Contact':
#     st.title('📩 Contact')
#     st.markdown('''
#     <div class='card'>
#     Let's connect for collaborations, internships, projects, and opportunities.
#     </div>
#     ''', unsafe_allow_html=True)
#     st.link_button('Connect on LinkedIn', SOCIAL_LINKS['LinkedIn'])

import streamlit as st

st.set_page_config(
    page_title='Rishu Portfolio Hub',
    page_icon='🚀',
    layout='wide',
    initial_sidebar_state='expanded'
)

SOCIAL_LINKS = {
    'LinkedIn': 'https://www.linkedin.com/in/rishu-gurjar-58072a333/',
    'GitHub': 'https://github.com/Rishu6262',
    'LeetCode': 'https://leetcode.com/u/rishu6262/',
    'Instagram': 'https://www.instagram.com/gurjar_sahab_jii_/?hl=en',
    'Streamlit': 'https://share.streamlit.io/user/rishu6262',
    'Resume': 'https://drive.google.com/file/d/1vPA-ThfKORseUxF6D9aLfHna8nGLVxjL/view?usp=sharing'
}

PROJECTS = [
    {
        'name': 'Project 1',
        'description': 'Live deployed Streamlit ML application.',
        'link': 'https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/'
    },
    {
        'name': 'Project 2',
        'description': 'Machine Learning deployment project.',
        'link': 'https://mlprojectp19-hdbfn8anguoftpumgrzbrl.streamlit.app/'
    },
    {
        'name': 'Car Model Prediction App',
        'description': 'FastAPI + ML powered car model prediction project.',
        'link': 'https://fastapicarmodelprediction-5wfyhdredwxwykagdh9ruo.streamlit.app/'
    },
    {
        'name': 'Mental Health Prediction App',
        'description': 'ML application focused on mental health prediction.',
        'link': 'https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/'
    },
    {
        'name': 'Revenue Prediction App',
        'description': 'Business revenue forecasting machine learning application.',
        'link': 'https://revenueprediction-jqtcydvcaxpcm3aj5ex2am.streamlit.app/'
    }
]

st.markdown('''
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
div[data-testid="stSidebar"] {
    background: #111827;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.15);
}
</style>
''', unsafe_allow_html=True)

with st.sidebar:
    st.title('🚀 Navigation')
    page = st.radio('Select Section', ['Home', 'Projects', 'Social Hub', 'Contact'])

if page == 'Home':
    st.markdown("""
    <div style='padding:30px; border-radius:24px; background: linear-gradient(135deg, rgba(59,130,246,0.25), rgba(168,85,247,0.20)); border:1px solid rgba(255,255,255,0.15); backdrop-filter: blur(14px);'>
        <h1 style='font-size:52px; margin-bottom:10px;'>🚀 Rishu Gurjar</h1>
        <h3 style='color:#cbd5e1;'>Data Science • ML Engineer • Python Developer</h3>
        <p style='font-size:18px; color:#e2e8f0;'>Building AI projects, deploying real apps, solving coding challenges, and growing as an engineer every day.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write('')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('🔥 Live Projects', '5+')
    with col2:
        st.metric('💻 Coding Profiles', '5+')
    with col3:
        st.metric('🚀 Deployment', 'Active')
    with col4:
        st.metric('📈 Learning', 'Daily')

    st.write('')
    left, right = st.columns([2,1])

    with left:
        st.markdown("""
        <div class='card'>
        <h2>About Me</h2>
        <p>I am passionate about Data Science, Machine Learning, deployment, and building practical Python applications. This portfolio is my digital hub where you can explore my projects, coding profiles, and professional journey.</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class='card'>
        <h3>Tech Stack</h3>
        <p>Python<br>Machine Learning<br>Data Science<br>FastAPI<br>Streamlit<br>Git & GitHub</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader('⚡ Quick Access')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button('GitHub', SOCIAL_LINKS['GitHub'])
        st.link_button('LeetCode', SOCIAL_LINKS['LeetCode'])
    with c2:
        st.link_button('LinkedIn', SOCIAL_LINKS['LinkedIn'])
        st.link_button('Instagram', SOCIAL_LINKS['Instagram'])
    with c3:
        st.link_button('Resume', SOCIAL_LINKS['Resume'])
        st.link_button('Streamlit Apps', SOCIAL_LINKS['Streamlit'])

if page == 'Projects':
    st.title('🔥 Live Projects')
    cols = st.columns(2)
    for i, project in enumerate(PROJECTS):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='card' style='min-height:220px;'>
                <h3>🚀 {project['name']}</h3>
                <p style='font-size:16px; color:#d1d5db;'>{project['description']}</p>
                <p style='color:#93c5fd;'>Ready to explore the live demo.</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Open {project['name']}", project['link'])

if page == 'Social Hub':
    st.title('🌐 Social Hub')
    cols = st.columns(2)
    items = list(SOCIAL_LINKS.items())
    for i, (name, link) in enumerate(items):
        with cols[i % 2]:
            st.link_button(name, link)

if page == 'Contact':
    st.title('📩 Contact')
    st.markdown('''
    <div class='card'>
    Let's connect for collaborations, internships, projects, and opportunities.
    </div>
    ''', unsafe_allow_html=True)
    st.link_button('Connect on LinkedIn', SOCIAL_LINKS['LinkedIn'])
