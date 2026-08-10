# ============================================================
# CAREERPILOT AI - CAREER ROADMAP ULTRA PRO MAX
# ============================================================

import streamlit as st

from ai_engine import generate_career_roadmap


def show_roadmap():

    st.title(
        "🗺️ AI Career Roadmap"
    )

    st.caption(
        "Build a personalized roadmap from your current level "
        "to your target technical role."
    )

    st.divider()

    # ========================================================
    # TARGET ROLE
    # ========================================================

    st.subheader(
        "🎯 Target Role"
    )

    target_role = st.selectbox(
        "Choose your target role",
        [
            "AI/ML Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Python Developer",
            "Software Engineer",
            "Data Analyst",
            "Full Stack Developer",
            "Backend Developer",
            "Cloud Engineer",
            "Other"
        ]
    )

    if target_role == "Other":

        target_role = st.text_input(
            "Enter target role"
        )

    # ========================================================
    # CURRENT PROFILE
    # ========================================================

    st.subheader(
        "🧠 Current Profile"
    )

    skills = st.text_area(
        "Current Skills",
        value=st.session_state.get(
            "profile_skills",
            ""
        ),
        height=180,
        placeholder=(
            "Example: Python, Java, SQL, Git..."
        )
    )

    experience = st.text_area(
        "Current Experience",
        value=st.session_state.get(
            "profile_experience",
            ""
        ),
        height=180,
        placeholder=(
            "Internships, projects or work experience..."
        )
    )

    projects = st.text_area(
        "Current Projects",
        height=180,
        placeholder=(
            "Example:\n"
            "CareerPilot AI\n"
            "Weather App\n"
            "E-commerce website"
        )
    )

    education = st.text_area(
        "Education",
        placeholder=(
            "Example: B.Tech CSE - AIML"
        ),
        height=120
    )

    # ========================================================
    # TIME
    # ========================================================

    st.subheader(
        "⏱️ Your Available Time"
    )

    col1, col2 = st.columns(2)

    with col1:

        hours_per_week = st.slider(
            "Hours per week",
            min_value=3,
            max_value=40,
            value=14
        )

    with col2:

        duration = st.selectbox(
            "Roadmap duration",
            [
                "30 Days",
                "60 Days",
                "90 Days",
                "6 Months",
                "12 Months"
            ]
        )

    # ========================================================
    # GENERATE
    # ========================================================

    st.divider()

    if st.button(
        "🚀 Generate My Ultra Career Roadmap",
        use_container_width=True,
        type="primary"
    ):

        if not target_role:

            st.warning(
                "Please select a target role."
            )

            return

        if not skills.strip():

            st.warning(
                "Please enter your current skills."
            )

            return

        with st.spinner(
            "🧠 AI is designing your personalized roadmap..."
        ):

            try:

                result = generate_career_roadmap(
                    target_role,
                    skills,
                    experience,
                    projects,
                    education,
                    hours_per_week,
                    duration
                )

                st.session_state[
                    "career_roadmap"
                ] = result

            except Exception as e:

                st.error(
                    f"Roadmap generation failed: {e}"
                )

                return

    # ========================================================
    # ROADMAP RESULT
    # ========================================================

    if "career_roadmap" in st.session_state:

        st.divider()

        st.subheader(
            "🧭 Your Career Roadmap"
        )

        st.markdown(
            st.session_state[
                "career_roadmap"
            ]
        )

        st.divider()

        st.success(
            "🎯 Follow the roadmap consistently and "
            "update it as your skills evolve."
        )