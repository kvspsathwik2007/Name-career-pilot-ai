# ============================================================
# CAREERPILOT AI - ATS CHECKER ULTRA PRO MAX
# ============================================================

import streamlit as st

from ai_engine import analyze_ats


def show_ats():

    st.title(
        "🎯 ATS Resume Checker"
    )

    st.caption(
        "Compare your resume against a real job description "
        "and discover your recruiter-readiness."
    )

    st.divider()

    # ========================================================
    # RESUME
    # ========================================================

    st.subheader(
        "📄 Resume"
    )

    existing_resume = st.session_state.get(
        "resume_text",
        ""
    )

    resume_text = st.text_area(
        "Resume Text",
        value=existing_resume,
        height=350,
        placeholder=(
            "Paste your resume text here..."
        ),
        key="ats_resume_text"
    )

    # ========================================================
    # JOB DESCRIPTION
    # ========================================================

    st.subheader(
        "💼 Job Description"
    )

    job_description = st.text_area(
        "Job Description",
        height=350,
        placeholder=(
            "Paste the complete job description here..."
        ),
        key="ats_job_description"
    )

    # ========================================================
    # ANALYZE
    # ========================================================

    st.divider()

    if st.button(
        "🚀 Run Ultra ATS Analysis",
        use_container_width=True,
        type="primary"
    ):

        if not resume_text.strip():

            st.warning(
                "Please provide your resume."
            )

            return

        if not job_description.strip():

            st.warning(
                "Please provide the job description."
            )

            return

        with st.spinner(
            "🤖 AI is analyzing your resume against the job..."
        ):

            try:

                result = analyze_ats(
                    resume_text,
                    job_description
                )

                st.session_state[
                    "ats_result"
                ] = result

            except Exception as e:

                st.error(
                    f"ATS analysis failed: {e}"
                )

                return

    # ========================================================
    # RESULT
    # ========================================================

    if "ats_result" not in st.session_state:

        st.info(
            "Run an ATS analysis to see your job-match report."
        )

        return

    result = st.session_state[
        "ats_result"
    ]

    st.divider()

    st.subheader(
        "📊 ATS Intelligence Report"
    )

    st.markdown(
        result
    )

    # ========================================================
    # SAVE SCORE IF DETECTABLE
    # ========================================================

    import re

    match = re.search(
        r"ATS SCORE:\s*(\d+)",
        result,
        re.IGNORECASE
    )

    if match:

        score = int(
            match.group(1)
        )

        st.session_state[
            "ats_score"
        ] = score

        st.divider()

        st.metric(
            "🎯 ATS Score",
            f"{score}/100"
        )

        st.progress(
            score / 100
        )

        if score >= 85:

            st.success(
                "🟢 Strong ATS compatibility"
            )

        elif score >= 70:

            st.info(
                "🔵 Good compatibility with room for improvement"
            )

        elif score >= 50:

            st.warning(
                "🟡 Several improvements are recommended"
            )

        else:

            st.error(
                "🔴 Major resume improvements are needed"
            )