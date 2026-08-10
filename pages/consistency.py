# ============================================================
# CAREERPILOT AI - AUTO CAREER CONSISTENCY ENGINE V2
# ============================================================

import streamlit as st

from utils.consistency_engine import (
    analyze_consistency
)

from ai_engine import (
    analyze_consistency as ai_consistency_analysis
)


# ============================================================
# BUILD LINKEDIN DATA
# ============================================================

def get_linkedin_data():

    return f"""
NAME:
{st.session_state.get("profile_name", "")}

TARGET ROLE:
{st.session_state.get("target_role", "")}

HEADLINE:
{st.session_state.get("profile_headline", "")}

ABOUT:
{st.session_state.get("profile_about", "")}

SKILLS:
{st.session_state.get("profile_skills", "")}

EXPERIENCE:
{st.session_state.get("profile_experience", "")}

OPTIMIZED HEADLINE:
{st.session_state.get("linkedin_headline_result", "")}

OPTIMIZED ABOUT:
{st.session_state.get("linkedin_about_result", "")}

OPTIMIZED SKILLS:
{st.session_state.get("linkedin_skills_result", "")}

OPTIMIZED EXPERIENCE:
{st.session_state.get("linkedin_experience_result", "")}
"""


# ============================================================
# BUILD GITHUB DATA
# ============================================================

def get_github_data_text():

    github_data = st.session_state.get(
        "github_data"
    )

    github_metrics = st.session_state.get(
        "github_metrics"
    )

    if not github_data:

        return ""

    profile = github_data.get(
        "profile",
        {}
    )

    repositories = github_data.get(
        "repositories",
        []
    )

    text = f"""
GITHUB USERNAME:
{profile.get("login", "")}

NAME:
{profile.get("name", "")}

BIO:
{profile.get("bio", "")}

LOCATION:
{profile.get("location", "")}

PUBLIC REPOSITORIES:
{profile.get("public_repos", 0)}

FOLLOWERS:
{profile.get("followers", 0)}

FOLLOWING:
{profile.get("following", 0)}

LANGUAGES:
"""

    if github_metrics:

        languages = github_metrics.get(
            "languages",
            {}
        )

        text += str(
            dict(languages)
        )

    text += "\n\nREPOSITORIES:\n"

    for repo in repositories[:30]:

        text += f"""
Repository:
{repo.get("name", "")}

Description:
{repo.get("description", "")}

Language:
{repo.get("language", "")}

Stars:
{repo.get("stargazers_count", 0)}

Forks:
{repo.get("forks_count", 0)}

Topics:
{", ".join(repo.get("topics", []))}

URL:
{repo.get("html_url", "")}

-----------------------------
"""

    return text


# ============================================================
# MAIN PAGE
# ============================================================

def show_consistency():

    st.title(
        "🔗 Career Consistency Engine"
    )

    st.caption(
        "Automatically compare your LinkedIn, Resume, "
        "and GitHub career identity."
    )

    st.divider()

    # ========================================================
    # DATA AVAILABILITY
    # ========================================================

    linkedin_available = any(
        [
            st.session_state.get(
                "profile_headline",
                ""
            ).strip(),

            st.session_state.get(
                "profile_about",
                ""
            ).strip(),

            st.session_state.get(
                "profile_skills",
                ""
            ).strip(),

            st.session_state.get(
                "profile_experience",
                ""
            ).strip()
        ]
    )

    resume_available = bool(
        st.session_state.get(
            "resume_text",
            ""
        ).strip()
    )

    github_available = bool(
        st.session_state.get(
            "github_data"
        )
    )

    # ========================================================
    # DATA STATUS
    # ========================================================

    st.subheader(
        "📡 Connected Career Data"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        if linkedin_available:

            st.success(
                "✅ LinkedIn data available"
            )

        else:

            st.warning(
                "⚠️ LinkedIn data not available"
            )

    with col2:

        if resume_available:

            st.success(
                "✅ Resume data available"
            )

        else:

            st.warning(
                "⚠️ Resume data not available"
            )

    with col3:

        if github_available:

            st.success(
                "✅ GitHub data available"
            )

        else:

            st.warning(
                "⚠️ GitHub data not available"
            )

    st.divider()

    # ========================================================
    # TARGET ROLE
    # ========================================================

    st.subheader(
        "🎯 Career Target"
    )

    target_role = st.selectbox(
        "Target role",
        [
            "AI/ML Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Python Developer",
            "Software Engineer",
            "Data Analyst",
            "Full Stack Developer",
            "Backend Developer",
            "Other"
        ],
        key="consistency_target_role"
    )

    if target_role == "Other":

        target_role = st.text_input(
            "Enter your target role",
            key="consistency_custom_role"
        )

    # ========================================================
    # AUTOMATIC DATA
    # ========================================================

    linkedin_text = get_linkedin_data()

    resume_text = st.session_state.get(
        "resume_text",
        ""
    )

    github_text = get_github_data_text()

    # ========================================================
    # AUTO ANALYZE
    # ========================================================

    st.divider()

    st.subheader(
        "🚀 Automatic Career Analysis"
    )

    st.write(
        "CareerPilot will automatically use the information "
        "already analyzed in this session."
    )

    if st.button(
        "🚀 Analyze My Complete Career Profile",
        use_container_width=True,
        type="primary"
    ):

        if not linkedin_available:

            st.error(
                "LinkedIn data is missing. "
                "Open LinkedIn Optimizer and enter your profile information first."
            )

        elif not resume_available:

            st.error(
                "Resume data is missing. "
                "Open Resume Analyzer and analyze a resume first."
            )

        elif not github_available:

            st.error(
                "GitHub data is missing. "
                "Open GitHub Optimizer and analyze your GitHub profile first."
            )

        else:

            # ------------------------------------------------
            # PYTHON ANALYSIS
            # ------------------------------------------------

            with st.spinner(
                "🔍 Comparing LinkedIn, Resume and GitHub..."
            ):

                try:

                    result = analyze_consistency(
                        linkedin_text,
                        resume_text,
                        github_text
                    )

                    st.session_state[
                        "auto_consistency_result"
                    ] = result

                except Exception as e:

                    st.error(
                        f"Consistency engine failed: {e}"
                    )

                    return

            # ------------------------------------------------
            # AI ANALYSIS
            # ------------------------------------------------

            ai_data = f"""
TARGET ROLE:
{target_role}

================ LINKEDIN ================

{linkedin_text}

================ RESUME ===================

{resume_text}

================ GITHUB ===================

{github_text}

================ PYTHON ANALYSIS ==========

{result}
"""

            with st.spinner(
                "🤖 AI is building your career intelligence report..."
            ):

                try:

                    ai_result = ai_consistency_analysis(
                        ai_data
                    )

                    st.session_state[
                        "auto_consistency_ai_result"
                    ] = ai_result

                except Exception as e:

                    st.error(
                        f"AI analysis failed: {e}"
                    )

    # ========================================================
    # RESULTS
    # ========================================================

    if "auto_consistency_result" not in st.session_state:

        st.info(
            "Analyze your complete career profile to see results."
        )

        return

    result = st.session_state[
        "auto_consistency_result"
    ]

    # ========================================================
    # OVERALL SCORE
    # ========================================================

    st.divider()

    st.subheader(
        "🎯 Career Consistency Score"
    )

    overall = result[
        "overall_score"
    ]

    scores = result[
        "platform_scores"
    ]

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Overall",
            f"{overall}/100"
        )

    with col2:

        st.metric(
            "LinkedIn ↔ Resume",
            f"{scores['linkedin_resume']}%"
        )

    with col3:

        st.metric(
            "Resume ↔ GitHub",
            f"{scores['resume_github']}%"
        )

    with col4:

        st.metric(
            "LinkedIn ↔ GitHub",
            f"{scores['linkedin_github']}%"
        )

    if overall >= 85:

        st.success(
            "🟢 Excellent career consistency"
        )

    elif overall >= 70:

        st.success(
            "🟢 Good career consistency"
        )

    elif overall >= 50:

        st.warning(
            "🟡 Some alignment improvements are needed"
        )

    else:

        st.error(
            "🔴 Your platforms need stronger alignment"
        )

    # ========================================================
    # SKILLS
    # ========================================================

    st.divider()

    st.subheader(
        "🛠 Skill Intelligence"
    )

    skills = result[
        "skills"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            "### 💼 LinkedIn"
        )

        if skills["linkedin"]:

            for skill in skills[
                "linkedin"
            ]:

                st.write(
                    f"• {skill.title()}"
                )

        else:

            st.caption(
                "No detected skills"
            )

    with col2:

        st.markdown(
            "### 📄 Resume"
        )

        if skills["resume"]:

            for skill in skills[
                "resume"
            ]:

                st.write(
                    f"• {skill.title()}"
                )

        else:

            st.caption(
                "No detected skills"
            )

    with col3:

        st.markdown(
            "### 💻 GitHub"
        )

        if skills["github"]:

            for skill in skills[
                "github"
            ]:

                st.write(
                    f"• {skill.title()}"
                )

        else:

            st.caption(
                "No detected skills"
            )

    # ========================================================
    # COMMON SKILLS
    # ========================================================

    st.divider()

    st.subheader(
        "✅ Skills Consistent Across All Platforms"
    )

    common = skills[
        "common_all"
    ]

    if common:

        for skill in common:

            st.success(
                f"✓ {skill.title()}"
            )

    else:

        st.info(
            "No skills were detected across all three platforms."
        )

    # ========================================================
    # SKILL GAPS
    # ========================================================

    st.divider()

    st.subheader(
        "⚠️ Detected Skill Visibility Gaps"
    )

    missing = result[
        "missing_skills"
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            "### 📄 Resume → LinkedIn"
        )

        values = missing[
            "resume_missing_from_linkedin"
        ]

        if values:

            for skill in values:

                st.warning(
                    f"Missing from LinkedIn: {skill.title()}"
                )

        else:

            st.success(
                "No detected gap."
            )

    with col2:

        st.markdown(
            "### 💻 GitHub → LinkedIn"
        )

        values = missing[
            "github_missing_from_linkedin"
        ]

        if values:

            for skill in values:

                st.warning(
                    f"Missing from LinkedIn: {skill.title()}"
                )

        else:

            st.success(
                "No detected gap."
            )

    # ========================================================
    # PROJECT VISIBILITY
    # ========================================================

    st.divider()

    st.subheader(
        "🚀 Project Visibility"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            "### 💼 LinkedIn"
        )

        projects = result[
            "linkedin_projects"
        ]

        if projects:

            for project in projects:

                st.write(
                    f"• {project}"
                )

        else:

            st.info(
                "No project section detected."
            )

    with col2:

        st.markdown(
            "### 📄 Resume"
        )

        projects = result[
            "resume_projects"
        ]

        if projects:

            for project in projects:

                st.write(
                    f"• {project}"
                )

        else:

            st.info(
                "No project section detected."
            )

    with col3:

        st.markdown(
            "### 💻 GitHub"
        )

        projects = result[
            "github_projects"
        ]

        if projects:

            for project in projects:

                st.write(
                    f"• {project}"
                )

        else:

            st.info(
                "GitHub repository information is available "
                "through the GitHub Optimizer."
            )

    # ========================================================
    # AI REPORT
    # ========================================================

    if "auto_consistency_ai_result" in st.session_state:

        st.divider()

        st.subheader(
            "🤖 AI Career Intelligence Report"
        )

        st.markdown(
            st.session_state[
                "auto_consistency_ai_result"
            ]
        )

        st.caption(
            "Important: a skill missing from one platform "
            "does not mean you don't possess it. It only "
            "means it was not detected there."
        )