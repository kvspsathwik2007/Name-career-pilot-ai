# ============================================================
# CAREERPILOT AI - RESUME ANALYZER V2
# ============================================================

import streamlit as st

from utils.pdf_parser import extract_text
from utils.ats_engine import analyze_resume_ats

from ai_engine import analyze_resume


def show_resume():

    st.title("📄 Resume Analyzer")

    st.caption(
        "Analyze your resume using ATS rules and AI-powered feedback."
    )

    st.divider()

    # ========================================================
    # UPLOAD
    # ========================================================

    uploaded_file = st.file_uploader(
        "Upload your Resume",
        type=["pdf"],
        help="Upload a PDF resume."
    )

    if not uploaded_file:

        st.info(
            "👆 Upload a PDF resume to begin."
        )

        return

    st.success(
        f"✅ {uploaded_file.name} uploaded successfully!"
    )

    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    ):

        # ----------------------------------------------------
        # Extract Text
        # ----------------------------------------------------

        with st.spinner(
            "📖 Extracting resume text..."
        ):

            try:

                resume_text = extract_text(
                    uploaded_file
                )

                if not resume_text:

                    st.error(
                        "❌ Could not extract text from this PDF."
                    )

                    st.warning(
                        "This may be an image-based PDF. "
                        "OCR support can be added later."
                    )

                    return

                st.session_state[
                    "resume_text"
                ] = resume_text

            except Exception as e:

                st.error(
                    f"PDF extraction failed: {e}"
                )

                return

        # ----------------------------------------------------
        # Real ATS Analysis
        # ----------------------------------------------------

        with st.spinner(
            "🔍 Running ATS checks..."
        ):

            try:

                ats_result = analyze_resume_ats(
                    resume_text
                )

                st.session_state[
                    "ats_result"
                ] = ats_result

            except Exception as e:

                st.error(
                    f"ATS analysis failed: {e}"
                )

                return

        # ----------------------------------------------------
        # AI Analysis
        # ----------------------------------------------------

        with st.spinner(
            "🤖 AI is reviewing your resume..."
        ):

            try:

                ai_result = analyze_resume(
                    resume_text
                )

                st.session_state[
                    "resume_ai_result"
                ] = ai_result

            except Exception as e:

                st.error(
                    f"AI analysis failed: {e}"
                )

                return

    # ========================================================
    # RESULTS
    # ========================================================

    if "ats_result" not in st.session_state:

        return

    ats = st.session_state[
        "ats_result"
    ]

    # ========================================================
    # SCORE DASHBOARD
    # ========================================================

    st.divider()

    st.subheader(
        "📊 Resume Health Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "ATS Score",
            f"{ats['ats_score']}/100"
        )

    with col2:

        st.metric(
            "Sections",
            f"{ats['section_score']}%"
        )

    with col3:

        st.metric(
            "Contact",
            f"{ats['contact_score']}%"
        )

    with col4:

        st.metric(
            "Skills",
            f"{ats['skill_score']}%"
        )

    # ========================================================
    # SCORE MESSAGE
    # ========================================================

    if ats["ats_score"] >= 80:

        st.success(
            "🟢 Strong ATS readiness"
        )

    elif ats["ats_score"] >= 60:

        st.warning(
            "🟡 Your resume has room for improvement"
        )

    else:

        st.error(
            "🔴 Your resume needs significant improvement"
        )

    # ========================================================
    # SECTION CHECK
    # ========================================================

    st.divider()

    st.subheader(
        "📑 Resume Sections"
    )

    for section, found in ats[
        "sections"
    ].items():

        if found:

            st.success(
                f"✅ {section}"
            )

        else:

            st.warning(
                f"⚠️ {section} not detected"
            )

    # ========================================================
    # CONTACT CHECK
    # ========================================================

    st.divider()

    st.subheader(
        "📞 Contact Information"
    )

    for item, found in ats[
        "contact"
    ].items():

        if found:

            st.success(
                f"✅ {item}"
            )

        else:

            st.warning(
                f"⚠️ {item} not detected"
            )

    # ========================================================
    # RESUME LENGTH
    # ========================================================

    st.divider()

    st.subheader(
        "📏 Resume Length"
    )

    st.write(
        f"Word Count: **{ats['length']['word_count']}**"
    )

    if ats["length"]["status"] == "Good":

        st.success(
            "✅ Resume length looks reasonable."
        )

    elif ats["length"]["status"] == "Too Short":

        st.warning(
            "⚠️ Resume may contain too little information."
        )

    else:

        st.warning(
            "⚠️ Resume may be longer than necessary."
        )

    # ========================================================
    # SKILLS
    # ========================================================

    st.divider()

    st.subheader(
        "🛠 Detected Technical Skills"
    )

    if ats["skills"]:

        cols = st.columns(3)

        for index, skill in enumerate(
            ats["skills"]
        ):

            with cols[
                index % 3
            ]:

                st.info(
                    skill.title()
                )

    else:

        st.warning(
            "No common technical skills were detected."
        )

    # ========================================================
    # AI ANALYSIS
    # ========================================================

    if "resume_ai_result" in st.session_state:

        st.divider()

        st.subheader(
            "🤖 AI Resume Analysis"
        )

        st.markdown(
            st.session_state[
                "resume_ai_result"
            ]
        )

    # ========================================================
    # EXTRACTED TEXT
    # ========================================================

    st.divider()

    with st.expander(
        "📋 View Extracted Resume Text"
    ):

        st.text_area(
            "Resume Content",
            value=st.session_state[
                "resume_text"
            ],
            height=400
        )

        st.caption(
            f"Characters extracted: "
            f"{len(st.session_state['resume_text'])}"
        )