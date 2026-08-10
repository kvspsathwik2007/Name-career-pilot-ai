import streamlit as st


def show_sidebar():

    #st.sidebar.image("assets/logo.png", width=120)

    st.sidebar.title("CareerPilot AI")

    st.sidebar.caption("AI Career Growth Assistant")

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigation",

        [
            "🏠 Dashboard",
            "👤 LinkedIn Optimizer",
            "📄 Resume Analyzer",
            "💻 GitHub Analyzer",
            "⭐ ATS Checker",
            "📝 Post Generator",
            "🎯 Career Roadmap",
            "⚙ Settings"
        ]

    )

    st.sidebar.divider()

    st.sidebar.info("Version 1.0")

    return page