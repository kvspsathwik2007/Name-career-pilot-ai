import streamlit as st

from styles import load_css
from components.ai_loader import show_sidebar

from pages.dashboard import show_dashboard
from pages.linkedin import show_linkedin
from pages.resume import show_resume
from pages.github import show_github
from pages.ats import show_ats
from pages.post_generator import show_posts
from pages.roadmap import show_roadmap
from pages.settings import show_settings

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.navigation([])
load_css()

page = show_sidebar()

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "👤 LinkedIn Optimizer":
    show_linkedin()

elif page == "📄 Resume Analyzer":
    show_resume()

elif page == "💻 GitHub Analyzer":
    show_github()

elif page == "⭐ ATS Checker":
    show_ats()

elif page == "📝 Post Generator":
    show_posts()

elif page == "🎯 Career Roadmap":
    show_roadmap()

elif page == "⚙ Settings":
    show_settings()