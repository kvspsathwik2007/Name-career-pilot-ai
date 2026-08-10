# ============================================================
# CAREERPILOT AI
# MAIN APPLICATION
# ============================================================

import streamlit as st

from styles import load_css

from pages.dashboard import show_dashboard
from pages.linkedin import show_linkedin
from pages.resume import show_resume
from pages.github import show_github
from pages.consistency import show_consistency
from pages.ats import show_ats
from pages.post_generator import show_posts
from pages.roadmap import show_roadmap
from pages.career_coach import show_career_coach
from pages.career_intelligence import show_career_intelligence


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# LOAD GLOBAL CSS
# ============================================================

load_css()


# ============================================================
# SIDEBAR BRANDING
# ============================================================

st.sidebar.markdown(
    "## 🚀 CareerPilot AI"
)

st.sidebar.caption(
    "AI Career Intelligence Platform"
)

st.sidebar.divider()


# ============================================================
# CREATE PAGE OBJECTS
# ============================================================

dashboard_page = st.Page(
    show_dashboard,
    title="Dashboard",
    icon="🏠",
    default=True,
)

linkedin_page = st.Page(
    show_linkedin,
    title="LinkedIn Optimizer",
    icon="👤",
)

resume_page = st.Page(
    show_resume,
    title="Resume Analyzer",
    icon="📄",
)

github_page = st.Page(
    show_github,
    title="GitHub Optimizer",
    icon="💻",
)

consistency_page = st.Page(
    show_consistency,
    title="Career Consistency",
    icon="🔗",
)

ats_page = st.Page(
    show_ats,
    title="ATS Checker",
    icon="🎯",
)

post_page = st.Page(
    show_posts,
    title="Post Generator",
    icon="✍️",
)

roadmap_page = st.Page(
    show_roadmap,
    title="Career Roadmap",
    icon="🗺️",
)

coach_page = st.Page(
    show_career_coach,
    title="AI Career Coach",
    icon="🤖",
)

intelligence_page = st.Page(
    show_career_intelligence,
    title="Career Intelligence",
    icon="🧠",
)


# ============================================================
# PAGE COLLECTION
# ============================================================

pages = [

    dashboard_page,

    linkedin_page,

    resume_page,

    github_page,

    consistency_page,

    ats_page,

    post_page,

    roadmap_page,

    coach_page,

    intelligence_page,

]


# ============================================================
# SHARE PAGE OBJECTS WITH DASHBOARD
# ============================================================

st.session_state["careerpilot_pages"] = {

    "dashboard": dashboard_page,

    "linkedin": linkedin_page,

    "resume": resume_page,

    "github": github_page,

    "consistency": consistency_page,

    "ats": ats_page,

    "posts": post_page,

    "roadmap": roadmap_page,

    "coach": coach_page,

    "intelligence": intelligence_page,

}


# ============================================================
# CREATE NAVIGATION
# ============================================================

pg = st.navigation(
    pages
)


# ============================================================
# RUN SELECTED PAGE
# ============================================================

pg.run()