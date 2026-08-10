# ============================================================
# CAREERPILOT AI
# DASHBOARD / COMMAND CENTER
# ============================================================

import streamlit as st


# ============================================================
# PAGE ACCESS
# ============================================================

def get_pages():

    return st.session_state.get(
        "careerpilot_pages",
        {}
    )


# ============================================================
# SCORE HELPERS
# ============================================================

def get_score(key):

    value = st.session_state.get(
        key,
        0
    )

    try:

        value = int(value)

    except (
        TypeError,
        ValueError
    ):

        value = 0

    return max(
        0,
        min(100, value)
    )


def get_career_score():

    scores = [

        get_score(
            "linkedin_profile_score"
        ),

        get_score(
            "resume_score"
        ),

        get_score(
            "github_score"
        ),

        get_score(
            "ats_score"
        ),

        get_score(
            "consistency_score"
        ),

    ]

    active_scores = [
        score
        for score in scores
        if score > 0
    ]

    if not active_scores:

        return 0

    return round(
        sum(active_scores)
        / len(active_scores)
    )


def get_status(score):

    if score >= 85:

        return "🟢 EXCELLENT"

    if score >= 70:

        return "🔵 STRONG"

    if score >= 50:

        return "🟡 DEVELOPING"

    if score > 0:

        return "🔴 NEEDS ATTENTION"

    return "⚪ NOT ANALYZED"


# ============================================================
# MAIN DASHBOARD
# ============================================================

def show_dashboard():

    pages = get_pages()


    # ========================================================
    # HERO
    # ========================================================

    st.title(
        "🚀 CareerPilot AI"
    )

    st.caption(
        "AI CAREER INTELLIGENCE COMMAND CENTER"
    )

    hero_left, hero_right = st.columns(
        [3, 1]
    )

    with hero_left:

        st.write(
            "Analyze • Optimize • Execute • Accelerate"
        )

    with hero_right:

        st.success(
            "🟢 AI CORE ONLINE"
        )

    st.divider()


    # ========================================================
    # CAREER INTELLIGENCE CORE
    # ========================================================

    score = get_career_score()

    st.subheader(
        "🧠 Career Intelligence Core"
    )

    score_col, information_col = st.columns(
        [1, 2],
        gap="large"
    )

    with score_col:

        st.metric(
            "CAREERPILOT SCORE",
            f"{score}/100"
        )

        st.progress(
            score / 100
        )

        st.caption(
            get_status(score)
        )

    with information_col:

        st.info(
            "CareerPilot combines your LinkedIn, Resume, "
            "GitHub, ATS and consistency signals into "
            "one career intelligence score."
        )

        metric_one, metric_two = st.columns(2)

        with metric_one:

            st.metric(
                "AI SYSTEMS",
                "10"
            )

        with metric_two:

            st.metric(
                "SYSTEM STATUS",
                "ONLINE"
            )

    st.divider()


    # ========================================================
    # LIVE TELEMETRY
    # ========================================================

    st.subheader(
        "📡 Live Career Telemetry"
    )

    telemetry = [

        (
            "👤 LinkedIn",
            "linkedin_profile_score"
        ),

        (
            "📄 Resume",
            "resume_score"
        ),

        (
            "💻 GitHub",
            "github_score"
        ),

        (
            "🎯 ATS",
            "ats_score"
        ),

        (
            "🔗 Consistency",
            "consistency_score"
        ),

    ]

    telemetry_columns = st.columns(
        5,
        gap="small"
    )

    for column, item in zip(
        telemetry_columns,
        telemetry
    ):

        label, key = item

        value = get_score(
            key
        )

        with column:

            st.metric(
                label,
                f"{value}%"
            )

            st.progress(
                value / 100
            )

    st.divider()


    # ========================================================
    # MODULE COMMAND DECK
    # ========================================================

    st.subheader(
        "⚡ Module Command Deck"
    )

    st.caption(
        "Select an intelligence system."
    )


    # ========================================================
    # ROW 1
    # ========================================================

    col1, col2, col3 = st.columns(
        3,
        gap="medium"
    )


    # --------------------------------------------------------
    # LINKEDIN
    # --------------------------------------------------------

    with col1:

        st.subheader(
            "👤 LinkedIn Optimizer"
        )

        st.write(
            "Optimize your headline, About section, "
            "skills and professional positioning."
        )

        if "linkedin" in pages:

            st.page_link(
                pages["linkedin"],
                label="🚀 Launch LinkedIn Optimizer",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # RESUME
    # --------------------------------------------------------

    with col2:

        st.subheader(
            "📄 Resume Analyzer"
        )

        st.write(
            "Analyze resume quality, keywords, "
            "ATS compatibility and missing skills."
        )

        if "resume" in pages:

            st.page_link(
                pages["resume"],
                label="🚀 Launch Resume Analyzer",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # GITHUB
    # --------------------------------------------------------

    with col3:

        st.subheader(
            "💻 GitHub Optimizer"
        )

        st.write(
            "Analyze repositories, projects, "
            "coding activity and developer branding."
        )

        if "github" in pages:

            st.page_link(
                pages["github"],
                label="🚀 Launch GitHub Optimizer",
                use_container_width=True,
            )


    # ========================================================
    # ROW 2
    # ========================================================

    col1, col2, col3 = st.columns(
        3,
        gap="medium"
    )


    # --------------------------------------------------------
    # CONSISTENCY
    # --------------------------------------------------------

    with col1:

        st.subheader(
            "🔗 Career Consistency"
        )

        st.write(
            "Check whether your Resume, LinkedIn "
            "and GitHub tell the same professional story."
        )

        if "consistency" in pages:

            st.page_link(
                pages["consistency"],
                label="🚀 Launch Career Consistency",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # ATS
    # --------------------------------------------------------

    with col2:

        st.subheader(
            "🎯 ATS Checker"
        )

        st.write(
            "Compare your resume against a target "
            "role and discover skill gaps."
        )

        if "ats" in pages:

            st.page_link(
                pages["ats"],
                label="🚀 Launch ATS Checker",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # POST GENERATOR
    # --------------------------------------------------------

    with col3:

        st.subheader(
            "✍️ Post Generator"
        )

        st.write(
            "Generate professional LinkedIn posts "
            "with AI-powered content suggestions."
        )

        if "posts" in pages:

            st.page_link(
                pages["posts"],
                label="🚀 Launch Post Generator",
                use_container_width=True,
            )


    # ========================================================
    # ROW 3
    # ========================================================

    col1, col2, col3 = st.columns(
        3,
        gap="medium"
    )


    # --------------------------------------------------------
    # ROADMAP
    # --------------------------------------------------------

    with col1:

        st.subheader(
            "🗺️ Career Roadmap"
        )

        st.write(
            "Build a structured roadmap from your "
            "current skills to your target career."
        )

        if "roadmap" in pages:

            st.page_link(
                pages["roadmap"],
                label="🚀 Launch Career Roadmap",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # AI CAREER COACH
    # --------------------------------------------------------

    with col2:

        st.subheader(
            "🤖 AI Career Coach"
        )

        st.write(
            "Ask career questions and receive "
            "personalized AI guidance."
        )

        if "coach" in pages:

            st.page_link(
                pages["coach"],
                label="🚀 Launch AI Career Coach",
                use_container_width=True,
            )


    # --------------------------------------------------------
    # CAREER INTELLIGENCE
    # --------------------------------------------------------

    with col3:

        st.subheader(
            "🧠 Career Intelligence"
        )

        st.write(
            "Combine your professional signals "
            "into one career readiness view."
        )

        if "intelligence" in pages:

            st.page_link(
                pages["intelligence"],
                label="🚀 Launch Career Intelligence",
                use_container_width=True,
            )


    st.divider()


    # ========================================================
    # ASK CAREERPILOT AI
    # ========================================================

    st.subheader(
        "🤖 Ask CareerPilot AI"
    )

    st.caption(
        "Have a career doubt? Ask your AI career assistant."
    )


    if "dashboard_ai_messages" not in st.session_state:

        st.session_state.dashboard_ai_messages = []


    # ========================================================
    # CHAT HISTORY
    # ========================================================

    for message in st.session_state.dashboard_ai_messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )


    # ========================================================
    # CHAT INPUT
    # ========================================================

    question = st.chat_input(
        "Ask about Python, Java, DSA, AI/ML, projects, resume, jobs..."
    )


    if question:

        st.session_state.dashboard_ai_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message(
            "user"
        ):

            st.write(
                question
            )


        # ====================================================
        # AI RESPONSE
        # ====================================================

        try:

            from config import client, MODEL

            system_prompt = """
You are CareerPilot AI.

You are an intelligent career assistant for
students, freshers and aspiring software engineers.

Help users with:

Programming
Python
Java
DSA
AI/ML
Data Science
Resume building
LinkedIn optimization
GitHub
ATS
Projects
Internships
Job preparation
Interview preparation
Career roadmaps
Learning plans

Rules:

1. Give practical advice.
2. Explain difficult concepts simply.
3. Give step-by-step instructions when useful.
4. Avoid unnecessary motivational speeches.
5. If the user is confused, start from the basics.
6. Give realistic learning plans.
7. Personalize the answer to the user's question.
8. Keep responses structured and easy to follow.
"""

            with st.chat_message(
                "assistant"
            ):

                with st.spinner(
                    "🧠 CareerPilot AI is thinking..."
                ):

                    response = client.chat.completions.create(

                        model=MODEL,

                        messages=[

                            {
                                "role": "system",
                                "content": system_prompt,
                            },

                            {
                                "role": "user",
                                "content": question,
                            },

                        ],
                    )

                    answer = (
                        response
                        .choices[0]
                        .message
                        .content
                    )

                st.write(
                    answer
                )


            st.session_state.dashboard_ai_messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )


        except Exception as error:

            with st.chat_message(
                "assistant"
            ):

                st.error(
                    "⚠️ CareerPilot AI could not connect "
                    "to the AI engine."
                )

                st.caption(
                    str(error)
                )


    st.divider()


    # ========================================================
    # AI ACTION CENTER
    # ========================================================

    st.subheader(
        "⚡ AI Action Center"
    )

    actions = []


    linkedin_score = get_score(
        "linkedin_profile_score"
    )

    resume_score = get_score(
        "resume_score"
    )

    github_score = get_score(
        "github_score"
    )

    ats_score = get_score(
        "ats_score"
    )

    consistency_score = get_score(
        "consistency_score"
    )


    if linkedin_score == 0:

        actions.append(
            "Complete your LinkedIn profile analysis."
        )

    elif linkedin_score < 70:

        actions.append(
            "Improve your LinkedIn profile."
        )


    if resume_score == 0:

        actions.append(
            "Upload and analyze your resume."
        )

    elif resume_score < 70:

        actions.append(
            "Improve your resume ATS compatibility."
        )


    if github_score == 0:

        actions.append(
            "Analyze your GitHub profile."
        )

    elif github_score < 70:

        actions.append(
            "Improve your GitHub project quality."
        )


    if ats_score > 0 and ats_score < 70:

        actions.append(
            "Close your biggest ATS skill gaps."
        )


    if consistency_score > 0 and consistency_score < 70:

        actions.append(
            "Improve consistency between your career profiles."
        )


    if not actions:

        actions.append(
            "Your major career intelligence signals "
            "are performing strongly."
        )


    for number, action in enumerate(
        actions,
        1
    ):

        if number == 1:

            st.warning(
                f"⚡ PRIORITY {number:02d} • {action}"
            )

        else:

            st.info(
                f"◉ ACTION {number:02d} • {action}"
            )


    st.divider()


    # ========================================================
    # CAREER READINESS
    # ========================================================

    st.subheader(
        "🎯 Career Readiness"
    )


    if score >= 85:

        st.success(
            "🚀 Elite readiness. Focus on advanced "
            "projects, interview preparation and measurable impact."
        )

    elif score >= 70:

        st.info(
            "🛰️ Strong foundation. Improve your weakest "
            "career signal next."
        )

    elif score >= 50:

        st.warning(
            "⚠️ Several career signals need optimization."
        )

    else:

        st.info(
            "🌌 Start analyzing your profiles to initialize "
            "CareerPilot intelligence."
        )


    # ========================================================
    # FOOTER
    # ========================================================

    st.divider()

    st.caption(
        "🚀 CareerPilot AI • AI Career Intelligence Platform • "
        "Command Center"
    )