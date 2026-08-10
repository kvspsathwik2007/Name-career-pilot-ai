# ============================================================
# CAREERPILOT AI - ULTRA PRO MAX GITHUB OPTIMIZER
# ============================================================

import streamlit as st

from utils.github_api import (
    extract_username,
    get_github_data
)

from utils.github_analyzer import (
    analyze_github
)

from ai_engine import (
    analyze_github_profile,
    analyze_github_role_match,
    analyze_github_projects
)


def show_github():

    st.title("💻 GitHub Profile Optimizer")

    st.caption(
        "Analyze your GitHub portfolio, projects, "
        "technology stack, recruiter readiness, and career fit."
    )

    st.divider()

    # ========================================================
    # TARGET ROLE
    # ========================================================

    st.subheader("🎯 Career Target")

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
            "Other"
        ],
        key="github_target_role"
    )

    if target_role == "Other":

        target_role = st.text_input(
            "Enter your target role",
            key="github_custom_role"
        )

    st.divider()

    # ========================================================
    # GITHUB INPUT
    # ========================================================

    st.subheader("🔗 GitHub Profile")

    github_input = st.text_input(
        "GitHub Username or Profile URL",
        placeholder=(
            "Example: octocat or "
            "https://github.com/octocat"
        ),
        key="github_input"
    )

    if st.button(
        "🚀 Analyze GitHub Profile",
        use_container_width=True
    ):

        if not github_input.strip():

            st.warning(
                "Please enter a GitHub username or URL."
            )

        else:

            try:

                username = extract_username(
                    github_input
                )

                with st.spinner(
                    "🔍 Fetching GitHub profile..."
                ):

                    github_data = get_github_data(
                        username
                    )

                with st.spinner(
                    "📊 Calculating GitHub metrics..."
                ):

                    metrics = analyze_github(
                        github_data
                    )

                st.session_state[
                    "github_data"
                ] = github_data

                st.session_state[
                    "github_metrics"
                ] = metrics

                st.session_state.pop(
                    "github_ai_analysis",
                    None
                )

                st.session_state.pop(
                    "github_role_analysis",
                    None
                )

                st.success(
                    "✅ GitHub profile analyzed successfully!"
                )

            except ValueError as e:

                st.error(str(e))

            except Exception as e:

                st.error(
                    f"GitHub analysis failed: {e}"
                )

    # ========================================================
    # CHECK DATA
    # ========================================================

    if "github_data" not in st.session_state:

        st.info(
            "👆 Enter a GitHub username to begin."
        )

        return

    github_data = st.session_state[
        "github_data"
    ]

    metrics = st.session_state[
        "github_metrics"
    ]

    profile = github_data[
        "profile"
    ]

    repositories = github_data[
        "repositories"
    ]

    # ========================================================
    # PROFILE
    # ========================================================

    st.divider()

    st.subheader(
        "👤 GitHub Profile"
    )

    col1, col2 = st.columns(
        [1, 3]
    )

    with col1:

        avatar = profile.get(
            "avatar_url"
        )

        if avatar:

            st.image(
                avatar,
                width=150
            )

    with col2:

        st.markdown(
            f"### {profile.get('name') or profile.get('login')}"
        )

        st.write(
            f"**Username:** @{profile.get('login')}"
        )

        if profile.get("bio"):

            st.write(
                profile["bio"]
            )

        if profile.get("location"):

            st.caption(
                f"📍 {profile['location']}"
            )

        st.caption(
            f"👥 {profile.get('followers', 0)} followers "
            f"· Following {profile.get('following', 0)}"
        )

        st.caption(
            f"📦 {profile.get('public_repos', 0)} public repositories"
        )

    # ========================================================
    # SCORE DASHBOARD
    # ========================================================

    st.divider()

    st.subheader(
        "📊 GitHub Health Dashboard"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(
            "GitHub Score",
            f"{metrics['github_score']}/100"
        )

    with col2:

        st.metric(
            "Profile",
            f"{metrics['profile_score']}/100"
        )

    with col3:

        st.metric(
            "Projects",
            f"{metrics['repository_score']}/100"
        )

    with col4:

        st.metric(
            "Documentation",
            f"{metrics['documentation_score']}/100"
        )

    with col5:

        st.metric(
            "Activity",
            f"{metrics['activity_score']}/100"
        )

    score = metrics[
        "github_score"
    ]

    if score >= 80:

        st.success(
            "🟢 Strong GitHub profile"
        )

    elif score >= 60:

        st.warning(
            "🟡 Good foundation with room for improvement."
        )

    else:

        st.error(
            "🔴 Your GitHub profile needs improvement."
        )

    # ========================================================
    # STATISTICS
    # ========================================================

    st.divider()

    st.subheader(
        "📈 GitHub Statistics"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Repositories",
            metrics["repository_count"]
        )

    with col2:

        st.metric(
            "Stars",
            metrics["total_stars"]
        )

    with col3:

        st.metric(
            "Forks",
            metrics["total_forks"]
        )

    with col4:

        st.metric(
            "Languages",
            len(metrics["languages"])
        )

    # ========================================================
    # TECHNOLOGY STACK
    # ========================================================

    st.divider()

    st.subheader(
        "🧠 Technology Stack"
    )

    if metrics["languages"]:

        for language, count in metrics[
            "languages"
        ].most_common():

            st.write(
                f"**{language}** — "
                f"{count} repositories"
            )

    else:

        st.info(
            "No programming languages detected."
        )

    # ========================================================
    # TARGET ROLE MATCHER
    # ========================================================

    st.divider()

    st.subheader(
        "🎯 GitHub → Job Role Matcher"
    )

    st.write(
        f"Evaluate your GitHub portfolio for the role: "
        f"**{target_role}**"
    )

    if st.button(
        "🎯 Analyze Role Fit",
        key="github_role_match",
        use_container_width=True
    ):

        if not target_role:

            st.warning(
                "Please select a target role."
            )

        else:

            repo_summary = []

            for repo in repositories[:20]:

                repo_summary.append(
                    {
                        "name": repo.get(
                            "name"
                        ),
                        "description": repo.get(
                            "description"
                        ),
                        "language": repo.get(
                            "language"
                        ),
                        "stars": repo.get(
                            "stargazers_count",
                            0
                        ),
                        "forks": repo.get(
                            "forks_count",
                            0
                        ),
                        "topics": repo.get(
                            "topics",
                            []
                        )
                    }
                )

            role_data = f"""
TARGET ROLE:
{target_role}

GITHUB USERNAME:
{profile.get('login')}

BIO:
{profile.get('bio')}

LANGUAGES:
{dict(metrics['languages'])}

GITHUB SCORE:
{metrics['github_score']}

PROFILE SCORE:
{metrics['profile_score']}

REPOSITORY SCORE:
{metrics['repository_score']}

DOCUMENTATION SCORE:
{metrics['documentation_score']}

REPOSITORIES:
{repo_summary}
"""

            with st.spinner(
                "🤖 AI is comparing your GitHub profile with the target role..."
            ):

                try:

                    result = analyze_github_role_match(
                        target_role,
                        role_data
                    )

                    st.session_state[
                        "github_role_analysis"
                    ] = result

                except Exception as e:

                    st.error(
                        f"Role analysis failed: {e}"
                    )

    if "github_role_analysis" in st.session_state:

        st.success(
            "🎯 Role-fit analysis completed!"
        )

        st.markdown(
            st.session_state[
                "github_role_analysis"
            ]
        )

    # ========================================================
    # REPOSITORIES
    # ========================================================

    st.divider()

    st.subheader(
        "📦 Repository Portfolio"
    )

    if not repositories:

        st.warning(
            "No public repositories found."
        )

    else:

        repository_details = metrics[
            "repository_details"
        ]

        for repo in repository_details[:20]:

            repo_name = repo[
                "name"
            ]

            quality = repo[
                "quality_score"
            ]

            with st.expander(
                f"📁 {repo_name} — {quality}/100"
            ):

                st.write(
                    repo["description"]
                    or "No description provided."
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.write(
                        f"💻 {repo['language'] or 'Not specified'}"
                    )

                with col2:

                    st.write(
                        f"⭐ {repo['stars']}"
                    )

                with col3:

                    st.write(
                        f"🍴 {repo['forks']}"
                    )

                if repo["topics"]:

                    st.write(
                        "🏷️ "
                        + ", ".join(
                            repo["topics"]
                        )
                    )

                if repo["url"]:

                    st.link_button(
                        "🔗 Open Repository",
                        repo["url"]
                    )

    # ========================================================
    # PROJECT ANALYSIS
    # ========================================================

    st.divider()

    st.subheader(
        "🚀 AI Project Portfolio Review"
    )

    if st.button(
        "🔍 Analyze My Projects",
        key="analyze_github_projects",
        use_container_width=True
    ):

        project_data = []

        for repo in repositories[:15]:

            project_data.append(
                {
                    "name": repo.get(
                        "name"
                    ),
                    "description": repo.get(
                        "description"
                    ),
                    "language": repo.get(
                        "language"
                    ),
                    "topics": repo.get(
                        "topics",
                        []
                    ),
                    "stars": repo.get(
                        "stargazers_count",
                        0
                    ),
                    "forks": repo.get(
                        "forks_count",
                        0
                    )
                }
            )

        with st.spinner(
            "🤖 AI is reviewing your projects..."
        ):

            try:

                result = analyze_github_projects(
                    str(project_data)
                )

                st.session_state[
                    "github_project_analysis"
                ] = result

            except Exception as e:

                st.error(
                    f"Project analysis failed: {e}"
                )

    if "github_project_analysis" in st.session_state:

        st.markdown(
            st.session_state[
                "github_project_analysis"
            ]
        )

    # ========================================================
    # COMPLETE AI ANALYSIS
    # ========================================================

    st.divider()

    st.subheader(
        "🧠 Complete GitHub Intelligence"
    )

    if st.button(
        "🚀 Generate Complete GitHub Report",
        key="github_complete_analysis",
        use_container_width=True
    ):

        repo_data = []

        for repo in repositories[:20]:

            repo_data.append(
                {
                    "name": repo.get("name"),
                    "description": repo.get(
                        "description"
                    ),
                    "language": repo.get(
                        "language"
                    ),
                    "stars": repo.get(
                        "stargazers_count",
                        0
                    ),
                    "forks": repo.get(
                        "forks_count",
                        0
                    ),
                    "topics": repo.get(
                        "topics",
                        []
                    )
                }
            )

        ai_input = f"""
GITHUB PROFILE:

Username:
{profile.get('login')}

Name:
{profile.get('name')}

Bio:
{profile.get('bio')}

Public Repositories:
{profile.get('public_repos')}

Followers:
{profile.get('followers')}

Following:
{profile.get('following')}

LANGUAGES:
{dict(metrics['languages'])}

CALCULATED METRICS:

GitHub Score:
{metrics['github_score']}

Profile Score:
{metrics['profile_score']}

Repository Score:
{metrics['repository_score']}

Activity Score:
{metrics['activity_score']}

Documentation Score:
{metrics['documentation_score']}

Star Score:
{metrics['star_score']}

REPOSITORIES:
{repo_data}
"""

        with st.spinner(
            "🧠 AI is preparing your complete GitHub report..."
        ):

            try:

                result = analyze_github_profile(
                    ai_input
                )

                st.session_state[
                    "github_ai_analysis"
                ] = result

            except Exception as e:

                st.error(
                    f"AI analysis failed: {e}"
                )

    if "github_ai_analysis" in st.session_state:

        st.markdown(
            st.session_state[
                "github_ai_analysis"
            ]
        )