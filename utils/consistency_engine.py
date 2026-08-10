# ============================================================
# CAREERPILOT AI - CONSISTENCY ENGINE
# ============================================================

import re


# ============================================================
# COMMON TECHNOLOGY / SKILL DATABASE
# ============================================================

COMMON_SKILLS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "html",
    "css",
    "react",
    "node.js",
    "express",
    "flask",
    "django",
    "streamlit",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "opencv",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "android",
    "kotlin",
    "firebase",
    "rest api",
    "api",
]


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):

    if not text:
        return ""

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# EXTRACT SKILLS
# ============================================================

def extract_skills(text):

    text = normalize_text(text)

    found = []

    for skill in COMMON_SKILLS:

        if skill in text:

            found.append(skill)

    return sorted(
        set(found)
    )


# ============================================================
# EXTRACT PROJECT-LIKE NAMES
# ============================================================

def extract_project_candidates(text):

    if not text:
        return []

    lines = text.splitlines()

    projects = []

    project_section = False

    project_headers = [
        "projects",
        "project",
        "academic projects",
        "personal projects",
        "projects:"
    ]

    for line in lines:

        clean = line.strip()

        lower = clean.lower()

        if lower in project_headers:

            project_section = True
            continue

        if project_section:

            if not clean:

                continue

            if lower in [
                "experience",
                "education",
                "skills",
                "certifications",
                "achievements",
                "summary",
                "objective"
            ]:

                project_section = False
                continue

            if len(clean) > 3:

                projects.append(
                    clean
                )

    return projects[:20]


# ============================================================
# SKILL COMPARISON
# ============================================================

def compare_skills(
    linkedin_text,
    resume_text,
    github_text
):

    linkedin_skills = set(
        extract_skills(
            linkedin_text
        )
    )

    resume_skills = set(
        extract_skills(
            resume_text
        )
    )

    github_skills = set(
        extract_skills(
            github_text
        )
    )

    all_skills = (
        linkedin_skills
        | resume_skills
        | github_skills
    )

    common_skills = (
        linkedin_skills
        & resume_skills
        & github_skills
    )

    linkedin_resume = (
        linkedin_skills
        & resume_skills
    )

    resume_github = (
        resume_skills
        & github_skills
    )

    linkedin_github = (
        linkedin_skills
        & github_skills
    )

    return {

        "linkedin": sorted(
            linkedin_skills
        ),

        "resume": sorted(
            resume_skills
        ),

        "github": sorted(
            github_skills
        ),

        "all": sorted(
            all_skills
        ),

        "common_all": sorted(
            common_skills
        ),

        "linkedin_resume": sorted(
            linkedin_resume
        ),

        "resume_github": sorted(
            resume_github
        ),

        "linkedin_github": sorted(
            linkedin_github
        )
    }


# ============================================================
# CALCULATE MATCH %
# ============================================================

def calculate_match(
    first_set,
    second_set
):

    first = set(
        first_set
    )

    second = set(
        second_set
    )

    combined = (
        first | second
    )

    if not combined:

        return 100

    intersection = (
        first & second
    )

    return round(
        len(intersection)
        / len(combined)
        * 100
    )


# ============================================================
# PLATFORM PAIR SCORES
# ============================================================

def calculate_platform_scores(
    skill_data
):

    linkedin = skill_data[
        "linkedin"
    ]

    resume = skill_data[
        "resume"
    ]

    github = skill_data[
        "github"
    ]

    return {

        "linkedin_resume": calculate_match(
            linkedin,
            resume
        ),

        "resume_github": calculate_match(
            resume,
            github
        ),

        "linkedin_github": calculate_match(
            linkedin,
            github
        )
    }


# ============================================================
# OVERALL CONSISTENCY SCORE
# ============================================================

def calculate_overall_score(
    platform_scores
):

    score = (
        platform_scores[
            "linkedin_resume"
        ] * 0.35

        + platform_scores[
            "resume_github"
        ] * 0.35

        + platform_scores[
            "linkedin_github"
        ] * 0.30
    )

    return round(
        score
    )


# ============================================================
# MISSING SKILLS
# ============================================================

def find_missing_skills(
    linkedin_skills,
    resume_skills,
    github_skills
):

    linkedin = set(
        linkedin_skills
    )

    resume = set(
        resume_skills
    )

    github = set(
        github_skills
    )

    return {

        "resume_missing_from_linkedin":
            sorted(
                resume - linkedin
            ),

        "github_missing_from_linkedin":
            sorted(
                github - linkedin
            ),

        "github_missing_from_resume":
            sorted(
                github - resume
            ),

        "linkedin_missing_from_resume":
            sorted(
                linkedin - resume
            )
    }


# ============================================================
# COMPLETE ANALYSIS
# ============================================================

def analyze_consistency(
    linkedin_text,
    resume_text,
    github_text
):

    skill_data = compare_skills(
        linkedin_text,
        resume_text,
        github_text
    )

    platform_scores = calculate_platform_scores(
        skill_data
    )

    overall_score = calculate_overall_score(
        platform_scores
    )

    missing_skills = find_missing_skills(
        skill_data["linkedin"],
        skill_data["resume"],
        skill_data["github"]
    )

    linkedin_projects = (
        extract_project_candidates(
            linkedin_text
        )
    )

    resume_projects = (
        extract_project_candidates(
            resume_text
        )
    )

    github_projects = (
        extract_project_candidates(
            github_text
        )
    )

    return {

        "overall_score": overall_score,

        "platform_scores":
            platform_scores,

        "skills":
            skill_data,

        "missing_skills":
            missing_skills,

        "linkedin_projects":
            linkedin_projects,

        "resume_projects":
            resume_projects,

        "github_projects":
            github_projects
    }
def extract_github_projects(github_text):

    projects = []

    blocks = github_text.split(
        "-----------------------------"
    )

    for block in blocks:

        lines = block.strip().splitlines()

        repo_name = ""

        for line in lines:

            if line.startswith("Repository:"):

                repo_name = line.replace(
                    "Repository:",
                    ""
                ).strip()

                break

        if repo_name:

            projects.append(
                repo_name
            )

    return projects