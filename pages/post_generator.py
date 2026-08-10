# ============================================================
# CAREERPILOT AI - LINKEDIN POST GENERATOR
# ============================================================

import streamlit as st

from ai_engine import generate_linkedin_post


# ============================================================
# MAIN POST GENERATOR
# ============================================================

def show_post_generator():

    st.title(
        "✍️ LinkedIn Post Generator"
    )

    st.caption(
        "Create authentic, professional and recruiter-friendly "
        "LinkedIn content with AI."
    )

    st.divider()

    # ========================================================
    # POST TYPE
    # ========================================================

    st.subheader(
        "📝 Post Details"
    )

    post_type = st.selectbox(
        "What are you posting about?",
        [
            "Project",
            "Internship",
            "Certification",
            "Course Completion",
            "Hackathon",
            "Achievement",
            "Learning Journey",
            "College Event",
            "Open Source Contribution",
            "Other"
        ],
        key="post_type"
    )

    # ========================================================
    # TOPIC
    # ========================================================

    topic = st.text_input(
        "Post Topic",
        placeholder=(
            "Example: Completed my AI/ML project"
        ),
        key="post_topic"
    )

    # ========================================================
    # DETAILS
    # ========================================================

    details = st.text_area(
        "Tell CareerPilot what happened",
        height=280,
        placeholder=(
            "What did you build?\n"
            "What did you learn?\n"
            "What technologies did you use?\n"
            "Who helped you?\n"
            "What was challenging?\n"
            "What is your next step?"
        ),
        key="post_details"
    )

    # ========================================================
    # SETTINGS
    # ========================================================

    st.subheader(
        "🎨 Post Style"
    )

    col1, col2 = st.columns(2)

    with col1:

        tone = st.selectbox(
            "Tone",
            [
                "Professional",
                "Confident",
                "Friendly",
                "Technical",
                "Storytelling",
                "Student-Friendly"
            ],
            key="post_tone"
        )

    with col2:

        audience = st.selectbox(
            "Target Audience",
            [
                "Recruiters",
                "Developers",
                "AI/ML Professionals",
                "Students",
                "General LinkedIn Audience"
            ],
            key="post_audience"
        )

    length = st.select_slider(
        "Post Length",
        options=[
            "Short",
            "Medium",
            "Long"
        ],
        value="Medium",
        key="post_length"
    )

    # ========================================================
    # GENERATE
    # ========================================================

    st.divider()

    if st.button(
        "🚀 Generate LinkedIn Post",
        use_container_width=True,
        type="primary",
        key="generate_linkedin_post"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a post topic."
            )

            return

        if not details.strip():

            st.warning(
                "⚠️ Please describe what you want to post about."
            )

            return

        with st.spinner(
            "🤖 CareerPilot AI is creating your post..."
        ):

            try:

                result = generate_linkedin_post(
                    topic,
                    details,
                    tone,
                    audience,
                    length
                )

                st.session_state[
                    "linkedin_post_result"
                ] = result

            except Exception as e:

                st.error(
                    f"Post generation failed: {e}"
                )

                return

    # ========================================================
    # RESULT
    # ========================================================

    if (
        "linkedin_post_result"
        in st.session_state
    ):

        st.divider()

        st.subheader(
            "✨ Generated LinkedIn Content"
        )

        result = st.session_state[
            "linkedin_post_result"
        ]

        st.markdown(
            result
        )

        # ====================================================
        # COPY VERSION
        # ====================================================

        st.divider()

        st.subheader(
            "📋 Copy-Ready Version"
        )

        st.text_area(
            "Your generated post",
            value=result,
            height=450,
            key="linkedin_post_copy"
        )

        # ====================================================
        # REGENERATE
        # ====================================================

        st.caption(
            "💡 You can change the tone, audience or length "
            "and generate another version."
        )


# ============================================================
# BACKWARD COMPATIBILITY
# ============================================================
#
# Your current app.py is importing:
#
# from pages.post_generator import show_posts
#
# So we expose show_posts as an alias.
# ============================================================

show_posts = show_post_generator