import streamlit as st


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


def calculate_intelligence():

    scores = {

        "LinkedIn":
            get_score(
                "linkedin_profile_score"
            ),

        "Resume":
            get_score(
                "resume_score"
            ),

        "GitHub":
            get_score(
                "github_score"
            ),

        "ATS":
            get_score(
                "ats_score"
            ),

        "Consistency":
            get_score(
                "consistency_score"
            ),

    }

    active = [
        value
        for value in scores.values()
        if value > 0
    ]

    if not active:

        return 0, scores

    overall = round(
        sum(active) /
        len(active)
    )

    return overall, scores


def intelligence_status(score):

    if score >= 85:

        return (
            "🟢 Elite Readiness",
            "Your career profile is highly competitive."
        )

    if score >= 70:

        return (
            "🔵 Strong Readiness",
            "Your profile has a strong foundation."
        )

    if score >= 50:

        return (
            "🟡 Developing",
            "Several areas need optimization."
        )

    if score > 0:

        return (
            "🔴 Needs Attention",
            "Important career signals require improvement."
        )

    return (
        "⚪ Awaiting Analysis",
        "Run the career modules to generate intelligence."
    )


def show_career_intelligence():

    st.title(
        "🧠 Career Intelligence"
    )

    st.caption(
        "Unified AI analysis of your professional identity"
    )

    st.success(
        "🟢 CAREER INTELLIGENCE CORE ONLINE"
    )

    st.divider()

    # ========================================================
    # OVERALL SCORE
    # ========================================================

    overall, scores = calculate_intelligence()

    status, description = intelligence_status(
        overall
    )

    col1, col2 = st.columns(
        [1, 2],
        gap="large"
    )

    with col1:

        st.metric(
            "Career Intelligence Score",
            f"{overall}/100"
        )

        st.progress(
            overall / 100
        )

    with col2:

        st.subheader(
            status
        )

        st.write(
            description
        )

        st.info(
            "CareerPilot combines five major signals: "
            "LinkedIn, Resume, GitHub, ATS and Consistency."
        )

    st.divider()

    # ========================================================
    # SIGNAL MATRIX
    # ========================================================

    st.subheader(
        "📡 Career Signal Matrix"
    )

    cols = st.columns(
        5
    )

    for column, (
        name,
        value
    ) in zip(
        cols,
        scores.items()
    ):

        with column:

            st.metric(
                name,
                f"{value}%"
            )

            st.progress(
                value / 100
            )

    st.divider()

    # ========================================================
    # STRENGTHS & GAPS
    # ========================================================

    st.subheader(
        "🎯 Intelligence Analysis"
    )

    strengths = [
        name
        for name, value in scores.items()
        if value >= 75
    ]

    gaps = [
        name
        for name, value in scores.items()
        if 0 < value < 70
    ]

    not_analyzed = [
        name
        for name, value in scores.items()
        if value == 0
    ]

    col1, col2, col3 = st.columns(
        3
    )

    with col1:

        st.success(
            "💎 Strengths"
        )

        if strengths:

            for item in strengths:

                st.write(
                    f"✓ {item}"
                )

        else:

            st.write(
                "No strong signals yet."
            )

    with col2:

        st.warning(
            "⚠️ Skill / Profile Gaps"
        )

        if gaps:

            for item in gaps:

                st.write(
                    f"• {item}"
                )

        else:

            st.write(
                "No major gaps detected."
            )

    with col3:

        st.info(
            "🔍 Not Analyzed"
        )

        if not_analyzed:

            for item in not_analyzed:

                st.write(
                    f"○ {item}"
                )

        else:

            st.write(
                "All signals analyzed."
            )

    st.divider()

    # ========================================================
    # PRIORITY ENGINE
    # ========================================================

    st.subheader(
        "⚡ AI Priority Engine"
    )

    analyzed_scores = {
        name: value
        for name, value in scores.items()
        if value > 0
    }

    if analyzed_scores:

        weakest = min(
            analyzed_scores,
            key=analyzed_scores.get
        )

        weakest_score = analyzed_scores[
            weakest
        ]

        st.warning(
            f"Highest priority: **{weakest}** "
            f"currently has a score of "
            f"**{weakest_score}%**."
        )

        st.write(
            "Improving your weakest signal will "
            "usually provide the biggest improvement "
            "to your overall career intelligence."
        )

    else:

        st.info(
            "Run LinkedIn, Resume, GitHub or ATS analysis "
            "to activate the priority engine."
        )

    st.divider()

    # ========================================================
    # CAREER INTELLIGENCE REPORT
    # ========================================================

    st.subheader(
        "📊 Intelligence Report"
    )

    report = f"""
CareerPilot AI Career Intelligence Report

Overall Score:
{overall}/100

LinkedIn:
{scores["LinkedIn"]}%

Resume:
{scores["Resume"]}%

GitHub:
{scores["GitHub"]}%

ATS:
{scores["ATS"]}%

Consistency:
{scores["Consistency"]}%

Status:
{status}
"""

    st.text_area(
        "Generated Report",
        value=report,
        height=250
    )

    st.download_button(
        "⬇️ Download Intelligence Report",
        data=report,
        file_name="careerpilot_intelligence_report.txt",
        mime="text/plain",
        use_container_width=True
    )