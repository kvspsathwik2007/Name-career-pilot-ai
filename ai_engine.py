# ============================================================
# CAREERPILOT AI - AI ENGINE
# ============================================================

from config import client, MODEL

from prompts import (
    HEADLINE_PROMPT,
    ABOUT_PROMPT,
    SKILLS_PROMPT,
    EXPERIENCE_PROMPT,
    LINKEDIN_PROFILE_ANALYSIS_PROMPT,
    RESUME_ANALYSIS_PROMPT,
    GITHUB_ANALYSIS_PROMPT,
    GITHUB_ROLE_MATCH_PROMPT,
    GITHUB_PROJECT_ANALYSIS_PROMPT
)


# ============================================================
# LINKEDIN
# ============================================================

def improve_headline(headline):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": HEADLINE_PROMPT
            },
            {
                "role": "user",
                "content": headline
            }
        ]
    )

    return response.choices[0].message.content.strip()


def improve_about(about):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": ABOUT_PROMPT
            },
            {
                "role": "user",
                "content": about
            }
        ]
    )

    return response.choices[0].message.content.strip()


def improve_skills(skills):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SKILLS_PROMPT
            },
            {
                "role": "user",
                "content": skills
            }
        ]
    )

    return response.choices[0].message.content.strip()


def improve_experience(experience):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": EXPERIENCE_PROMPT
            },
            {
                "role": "user",
                "content": experience
            }
        ]
    )

    return response.choices[0].message.content.strip()


def analyze_headline(headline):

    prompt = f"""
You are a LinkedIn recruiter and ATS specialist.

Analyze this headline:

{headline}

Return:

SCORE: <number>/100

STRENGTHS:
- ...
- ...
- ...

MISSING KEYWORDS:
- ...
- ...
- ...

IMPROVEMENT:
...

Do not invent information.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": headline
            }
        ]
    )

    return response.choices[0].message.content.strip()


def analyze_linkedin_profile(profile_data):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": LINKEDIN_PROFILE_ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": profile_data
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# RESUME
# ============================================================

def analyze_resume(resume_text):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": RESUME_ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": resume_text
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# GITHUB
# ============================================================

def analyze_github_profile(github_data):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": GITHUB_ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": github_data
            }
        ]
    )

    return response.choices[0].message.content.strip()


def analyze_github_role_match(
    target_role,
    github_data
):

    prompt = GITHUB_ROLE_MATCH_PROMPT.format(
        target_role=target_role,
        github_data=github_data
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": github_data
            }
        ]
    )

    return response.choices[0].message.content.strip()


def analyze_github_projects(
    project_data
):

    prompt = GITHUB_PROJECT_ANALYSIS_PROMPT

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": project_data
            }
        ]
    )

    return response.choices[0].message.content.strip()
def analyze_consistency(
    consistency_data
):

    from prompts import CONSISTENCY_ANALYSIS_PROMPT

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": CONSISTENCY_ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": consistency_data
            }
        ]
    )

    return response.choices[0].message.content.strip()
# ============================================================
# ATS CHECKER
# ============================================================

def analyze_ats(resume_text, job_description):

    from prompts import ATS_ANALYSIS_PROMPT

    prompt = f"""
RESUME:

{resume_text}


JOB DESCRIPTION:

{job_description}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": ATS_ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# LINKEDIN POST GENERATOR
# ============================================================

def generate_linkedin_post(
    topic,
    details,
    tone,
    audience,
    length
):

    from prompts import LINKEDIN_POST_PROMPT

    prompt = f"""
TOPIC:
{topic}

DETAILS:
{details}

TONE:
{tone}

TARGET AUDIENCE:
{audience}

POST LENGTH:
{length}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": LINKEDIN_POST_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# CAREER ROADMAP
# ============================================================

def generate_career_roadmap(
    target_role,
    skills,
    experience,
    projects,
    education,
    hours_per_week,
    duration
):

    from prompts import CAREER_ROADMAP_PROMPT

    prompt = CAREER_ROADMAP_PROMPT.format(
        target_role=target_role,
        skills=skills,
        experience=experience,
        projects=projects,
        education=education,
        hours_per_week=hours_per_week,
        duration=duration
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": (
                    "Create the personalized career roadmap."
                )
            }
        ]
    )

    return response.choices[0].message.content.strip()