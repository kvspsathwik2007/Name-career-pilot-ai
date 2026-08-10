# ============================================================
# CAREERPILOT AI
# LINKEDIN OPTIMIZER V2
# PROFILE INTELLIGENCE ENGINE
# ============================================================

import re
import json
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

# Do not use st.set_page_config() here.
# app.py already handles the page configuration.


# ============================================================
# SESSION STATE
# ============================================================

def initialize_state():

    defaults = {

        "linkedin_profile_score": 0,

        "linkedin_analysis": None,

        "linkedin_optimized_headline": "",

        "linkedin_optimized_about": "",

        "linkedin_url": "",

        "linkedin_analyzed": False,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ============================================================
# URL VALIDATION
# ============================================================

def validate_linkedin_url(url):

    if not url:

        return False

    url = url.strip()

    pattern = (
        r"^(https?://)?"
        r"(www\.)?"
        r"linkedin\.com/in/"
        r"[A-Za-z0-9\-_%.]+"
        r"/?$"
    )

    return bool(
        re.match(
            pattern,
            url,
            re.IGNORECASE
        )
    )


# ============================================================
# CLEAN URL
# ============================================================

def clean_linkedin_url(url):

    url = url.strip()

    if not url.startswith("http://") and not url.startswith("https://"):

        url = "https://" + url

    return url.rstrip("/")


# ============================================================
# SCORE NORMALIZATION
# ============================================================

def normalize_score(value):

    try:

        value = int(
            float(value)
        )

    except (
        TypeError,
        ValueError
    ):

        value = 0

    return max(
        0,
        min(100, value)
    )


# ============================================================
# SAFE JSON EXTRACTION
# ============================================================

def extract_json(text):

    if not text:

        return None

    text = text.strip()

    # Remove markdown code fences

    text = re.sub(
        r"```json",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"```",
        "",
        text
    )

    text = text.strip()

    # Try direct JSON

    try:

        return json.loads(
            text
        )

    except Exception:

        pass

    # Try extracting JSON object

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if match:

        try:

            return json.loads(
                match.group(0)
            )

        except Exception:

            return None

    return None


# ============================================================
# SCORE STATUS
# ============================================================

def score_status(score):

    if score >= 90:

        return (
            "🟢 Elite",
            "Your profile is highly optimized."
        )

    if score >= 80:

        return (
            "🟢 Strong",
            "Your profile has a strong professional foundation."
        )

    if score >= 70:

        return (
            "🔵 Good",
            "Your profile is good but has optimization opportunities."
        )

    if score >= 60:

        return (
            "🟡 Developing",
            "Several areas can be improved."
        )

    if score > 0:

        return (
            "🔴 Needs Attention",
            "Your profile needs significant optimization."
        )

    return (
        "⚪ Not Analyzed",
        "Analyze your profile to generate a score."
    )


# ============================================================
# AI ANALYSIS
# ============================================================

def analyze_with_ai(
    linkedin_url,
    headline,
    about,
    experience,
    skills,
    target_role,
):

    from config import client, MODEL

    prompt = f"""
You are CareerPilot AI LinkedIn Intelligence Engine.

Analyze the user's LinkedIn profile content for
professional branding, recruiter appeal, ATS/search
visibility, technical positioning and target-role alignment.

IMPORTANT:
Do NOT invent information that is not provided.

LINKEDIN URL:
{linkedin_url}

TARGET ROLE:
{target_role}

HEADLINE:
{headline}

ABOUT:
{about}

EXPERIENCE:
{experience}

SKILLS:
{skills}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "overall_score": 0,
    "headline_score": 0,
    "about_score": 0,
    "experience_score": 0,
    "skills_score": 0,
    "keyword_score": 0,
    "recruiter_appeal_score": 0,
    "professional_brand_score": 0,

    "profile_status": "",

    "strengths": [
        "",
        "",
        ""
    ],

    "critical_gaps": [
        "",
        "",
        ""
    ],

    "recommendations": [
        "",
        "",
        "",
        "",
        ""
    ],

    "missing_keywords": [
        "",
        "",
        "",
        ""
    ],

    "optimized_headline": "",

    "optimized_about": "",

    "experience_improvements": [
        "",
        "",
        ""
    ],

    "skills_recommendations": [
        "",
        "",
        ""
    ],

    "recruiter_summary": ""
}}

Scoring rules:

90-100 = Elite
80-89 = Strong
70-79 = Good
60-69 = Developing
0-59 = Needs Attention

Headline should be concise and recruiter-friendly.

Optimized headline should:
- clearly communicate target role
- include relevant technical keywords
- avoid keyword stuffing
- show professional positioning

Optimized About should:
- sound human
- communicate expertise
- communicate career direction
- include relevant keywords naturally
- avoid fake claims
- avoid exaggerated achievements

Recommendations must be actionable.

Missing keywords must only include keywords
that are genuinely relevant to the target role.

Do not fabricate:
- companies
- projects
- certifications
- experience
- achievements
- job titles
- technologies
"""

    response = client.chat.completions.create(

        model=MODEL,

        messages=[

            {
                "role": "system",
                "content": (
                    "You are a professional LinkedIn "
                    "profile optimization engine."
                ),
            },

            {
                "role": "user",
                "content": prompt,
            },

        ],

    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    return extract_json(
        content
    )


# ============================================================
# SCORE CARD
# ============================================================

def show_score_card(
    title,
    score,
):

    score = normalize_score(
        score
    )

    st.metric(
        title,
        f"{score}%"
    )

    st.progress(
        score / 100
    )


# ============================================================
# MAIN PAGE
# ============================================================

def show_linkedin():

    initialize_state()


    # ========================================================
    # HEADER
    # ========================================================

    st.title(
        "👤 LinkedIn Profile Optimizer"
    )

    st.caption(
        "AI-powered LinkedIn profile intelligence "
        "for students, freshers and aspiring professionals."
    )

    st.success(
        "🟢 LINKEDIN INTELLIGENCE ENGINE ONLINE"
    )

    st.divider()


    # ========================================================
    # PROFILE URL
    # ========================================================

    st.subheader(
        "🔗 LinkedIn Profile"
    )

    linkedin_url = st.text_input(

        "LinkedIn Profile URL",

        value=st.session_state.get(
            "linkedin_url",
            ""
        ),

        placeholder=(
            "https://www.linkedin.com/in/your-profile/"
        ),

        help=(
            "Paste your public LinkedIn profile URL."
        ),

    )


    if linkedin_url:

        if validate_linkedin_url(
            linkedin_url
        ):

            st.success(
                "✓ Valid LinkedIn profile URL"
            )

        else:

            st.error(
                "Please enter a valid LinkedIn profile URL."
            )


    # ========================================================
    # TARGET ROLE
    # ========================================================

    target_role = st.text_input(

        "🎯 Target Role",

        placeholder=(
            "Example: AI Engineer, Software Engineer, "
            "ML Engineer, Data Scientist"
        ),

    )


    # ========================================================
    # PROFILE CONTENT
    # ========================================================

    st.divider()

    st.subheader(
        "📋 Profile Intelligence Input"
    )

    st.info(
        "For accurate analysis, paste your actual LinkedIn "
        "profile sections below. CareerPilot will analyze "
        "the content rather than inventing profile data."
    )


    headline = st.text_input(

        "Headline",

        placeholder=(
            "Example: B.Tech AIML Student | Python | Java | AI/ML"
        ),

    )


    about = st.text_area(

        "About",

        placeholder=(
            "Paste your LinkedIn About section here..."
        ),

        height=180,

    )


    experience = st.text_area(

        "Experience",

        placeholder=(
            "Paste your internships, projects, "
            "work experience and descriptions..."
        ),

        height=180,

    )


    skills = st.text_area(

        "Skills",

        placeholder=(
            "Example: Python, Java, SQL, Machine Learning, "
            "Git, GitHub, HTML, CSS..."
        ),

        height=120,

    )


    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    st.divider()

    analyze_button = st.button(

        "🔍 ANALYZE LINKEDIN PROFILE",

        type="primary",

        use_container_width=True,

    )


    if analyze_button:

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not validate_linkedin_url(
            linkedin_url
        ):

            st.error(
                "Please enter a valid LinkedIn profile URL."
            )

            return


        if not headline.strip():

            st.error(
                "Please enter your LinkedIn headline."
            )

            return


        if not about.strip():

            st.error(
                "Please enter your LinkedIn About section."
            )

            return


        if not target_role.strip():

            st.error(
                "Please enter your target role."
            )

            return


        # ----------------------------------------------------
        # SAVE URL
        # ----------------------------------------------------

        linkedin_url = clean_linkedin_url(
            linkedin_url
        )

        st.session_state.linkedin_url = (
            linkedin_url
        )


        # ----------------------------------------------------
        # AI ANALYSIS
        # ----------------------------------------------------

        try:

            with st.spinner(
                "🧠 CareerPilot is analyzing your LinkedIn profile..."
            ):

                result = analyze_with_ai(

                    linkedin_url=linkedin_url,

                    headline=headline,

                    about=about,

                    experience=experience,

                    skills=skills,

                    target_role=target_role,

                )


            if not result:

                st.error(
                    "AI returned an invalid analysis. "
                    "Please try again."
                )

                return


            # ------------------------------------------------
            # NORMALIZE SCORES
            # ------------------------------------------------

            overall_score = normalize_score(
                result.get(
                    "overall_score",
                    0
                )
            )

            headline_score = normalize_score(
                result.get(
                    "headline_score",
                    0
                )
            )

            about_score = normalize_score(
                result.get(
                    "about_score",
                    0
                )
            )

            experience_score = normalize_score(
                result.get(
                    "experience_score",
                    0
                )
            )

            skills_score = normalize_score(
                result.get(
                    "skills_score",
                    0
                )
            )

            keyword_score = normalize_score(
                result.get(
                    "keyword_score",
                    0
                )
            )


            # ------------------------------------------------
            # SAVE RESULTS
            # ------------------------------------------------

            st.session_state.linkedin_profile_score = (
                overall_score
            )

            st.session_state.linkedin_analysis = (
                result
            )

            st.session_state.linkedin_optimized_headline = (
                result.get(
                    "optimized_headline",
                    ""
                )
            )

            st.session_state.linkedin_optimized_about = (
                result.get(
                    "optimized_about",
                    ""
                )
            )

            st.session_state.linkedin_analyzed = True


            st.success(
                "✅ LinkedIn profile analysis completed."
            )

        except Exception as error:

            st.error(
                "❌ LinkedIn analysis failed."
            )

            st.exception(
                error
            )

            return


    # ========================================================
    # RESULTS
    # ========================================================

    result = st.session_state.get(
        "linkedin_analysis"
    )


    if not result:

        st.info(
            "👆 Enter your LinkedIn profile details "
            "and click **Analyze LinkedIn Profile**."
        )

        return


    # ========================================================
    # PROFILE SCORE
    # ========================================================

    st.divider()

    st.subheader(
        "📊 LinkedIn Intelligence Score"
    )

    overall_score = normalize_score(
        result.get(
            "overall_score",
            0
        )
    )

    status, status_description = score_status(
        overall_score
    )


    score_col, status_col = st.columns(
        [1, 2],
        gap="large"
    )


    with score_col:

        st.metric(
            "PROFILE SCORE",
            f"{overall_score}/100"
        )

        st.progress(
            overall_score / 100
        )


    with status_col:

        st.subheader(
            status
        )

        st.write(
            status_description
        )

        st.caption(
            f"Target Role: {target_role}"
        )


    # ========================================================
    # SCORE MATRIX
    # ========================================================

    st.subheader(
        "📡 Profile Signal Matrix"
    )

    matrix = [

        (
            "Headline",
            result.get(
                "headline_score",
                0
            )
        ),

        (
            "About",
            result.get(
                "about_score",
                0
            )
        ),

        (
            "Experience",
            result.get(
                "experience_score",
                0
            )
        ),

        (
            "Skills",
            result.get(
                "skills_score",
                0
            )
        ),

        (
            "Keywords",
            result.get(
                "keyword_score",
                0
            )
        ),

    ]


    score_columns = st.columns(
        5
    )


    for column, (
        label,
        value
    ) in zip(
        score_columns,
        matrix
    ):

        with column:

            show_score_card(
                label,
                value
            )


    # ========================================================
    # RECRUITER METRICS
    # ========================================================

    st.divider()

    recruiter_col, branding_col = st.columns(
        2
    )


    with recruiter_col:

        recruiter_score = normalize_score(
            result.get(
                "recruiter_appeal_score",
                0
            )
        )

        st.metric(
            "🎯 Recruiter Appeal",
            f"{recruiter_score}%"
        )

        st.progress(
            recruiter_score / 100
        )


    with branding_col:

        branding_score = normalize_score(
            result.get(
                "professional_brand_score",
                0
            )
        )

        st.metric(
            "💎 Professional Brand",
            f"{branding_score}%"
        )

        st.progress(
            branding_score / 100
        )


    # ========================================================
    # STRENGTHS
    # ========================================================

    st.divider()

    st.subheader(
        "💎 Profile Strengths"
    )

    strengths = result.get(
        "strengths",
        []
    )


    if strengths:

        for strength in strengths:

            st.success(
                f"✓ {strength}"
            )

    else:

        st.info(
            "No strengths were returned."
        )


    # ========================================================
    # CRITICAL GAPS
    # ========================================================

    st.subheader(
        "⚠️ Critical Gaps"
    )

    gaps = result.get(
        "critical_gaps",
        []
    )


    if gaps:

        for gap in gaps:

            st.warning(
                f"• {gap}"
            )

    else:

        st.success(
            "No major critical gaps detected."
        )


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    st.subheader(
        "⚡ AI Recommendations"
    )

    recommendations = result.get(
        "recommendations",
        []
    )


    if recommendations:

        for index, recommendation in enumerate(
            recommendations,
            1
        ):

            st.info(
                f"**Priority {index}:** {recommendation}"
            )


    # ========================================================
    # MISSING KEYWORDS
    # ========================================================

    st.subheader(
        "🔑 Missing / Recommended Keywords"
    )

    keywords = result.get(
        "missing_keywords",
        []
    )


    if keywords:

        keyword_text = " • ".join(
            str(keyword)
            for keyword in keywords
        )

        st.write(
            keyword_text
        )

    else:

        st.success(
            "No major missing keywords detected."
        )


    # ========================================================
    # OPTIMIZED HEADLINE
    # ========================================================

    st.divider()

    st.subheader(
        "✨ AI-Optimized Headline"
    )

    optimized_headline = result.get(
        "optimized_headline",
        ""
    )


    if optimized_headline:

        st.text_area(
            "Optimized headline",
            value=optimized_headline,
            height=100,
            key="optimized_headline_display"
        )

        st.code(
            optimized_headline,
            language=None
        )

    else:

        st.info(
            "No optimized headline was generated."
        )


    # ========================================================
    # OPTIMIZED ABOUT
    # ========================================================

    st.subheader(
        "✨ AI-Optimized About Section"
    )

    optimized_about = result.get(
        "optimized_about",
        ""
    )


    if optimized_about:

        st.text_area(
            "Optimized About",
            value=optimized_about,
            height=280,
            key="optimized_about_display"
        )

    else:

        st.info(
            "No optimized About section was generated."
        )


    # ========================================================
    # EXPERIENCE IMPROVEMENTS
    # ========================================================

    st.subheader(
        "💼 Experience Improvements"
    )

    experience_improvements = result.get(
        "experience_improvements",
        []
    )


    if experience_improvements:

        for item in experience_improvements:

            st.write(
                f"• {item}"
            )

    else:

        st.info(
            "No experience recommendations available."
        )


    # ========================================================
    # SKILLS RECOMMENDATIONS
    # ========================================================

    st.subheader(
        "🧠 Skills Recommendations"
    )

    skills_recommendations = result.get(
        "skills_recommendations",
        []
    )


    if skills_recommendations:

        for item in skills_recommendations:

            st.write(
                f"• {item}"
            )

    else:

        st.info(
            "No additional skills recommendations."
        )


    # ========================================================
    # RECRUITER SUMMARY
    # ========================================================

    st.divider()

    st.subheader(
        "🎯 Recruiter Perspective"
    )

    recruiter_summary = result.get(
        "recruiter_summary",
        ""
    )


    if recruiter_summary:

        st.info(
            recruiter_summary
        )


    # ========================================================
    # EXPORT REPORT
    # ========================================================

    report = f"""
CAREERPILOT AI
LINKEDIN PROFILE INTELLIGENCE REPORT
=====================================

LinkedIn:
{linkedin_url}

Target Role:
{target_role}

Overall Score:
{overall_score}/100

Headline:
{headline_score}/100

About:
{about_score}/100

Experience:
{experience_score}/100

Skills:
{skills_score}/100

Keywords:
{keyword_score}/100

Recruiter Appeal:
{result.get("recruiter_appeal_score", 0)}/100

Professional Brand:
{result.get("professional_brand_score", 0)}/100


STRENGTHS
---------
{chr(10).join("- " + str(x) for x in strengths)}


CRITICAL GAPS
-------------
{chr(10).join("- " + str(x) for x in gaps)}


RECOMMENDATIONS
---------------
{chr(10).join("- " + str(x) for x in recommendations)}


MISSING KEYWORDS
----------------
{chr(10).join("- " + str(x) for x in keywords)}


OPTIMIZED HEADLINE
------------------
{optimized_headline}


OPTIMIZED ABOUT
---------------
{optimized_about}


EXPERIENCE IMPROVEMENTS
-----------------------
{chr(10).join("- " + str(x) for x in experience_improvements)}


SKILLS RECOMMENDATIONS
----------------------
{chr(10).join("- " + str(x) for x in skills_recommendations)}


RECRUITER SUMMARY
-----------------
{recruiter_summary}
"""


    st.download_button(

        "⬇️ Download LinkedIn Intelligence Report",

        data=report,

        file_name=(
            "careerpilot_linkedin_report.txt"
        ),

        mime="text/plain",

        use_container_width=True,

    )


    # ========================================================
    # DASHBOARD SYNC
    # ========================================================

    st.divider()

    st.success(
        f"🔄 CareerPilot Dashboard synchronized. "
        f"LinkedIn Score: {overall_score}/100"
    )