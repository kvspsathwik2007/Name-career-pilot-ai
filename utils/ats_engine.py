# ============================================================
# CAREERPILOT AI - ATS ENGINE V2
# ============================================================

import re


# ------------------------------------------------------------
# Expected Resume Sections
# ------------------------------------------------------------

SECTION_KEYWORDS = {
    "Contact Information": [
        "email",
        "phone",
        "mobile",
        "linkedin",
        "github"
    ],

    "Summary": [
        "summary",
        "objective",
        "profile"
    ],

    "Education": [
        "education",
        "academic",
        "qualification"
    ],

    "Experience": [
        "experience",
        "work experience",
        "internship",
        "employment"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "technologies"
    ],

    "Projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],

    "Certifications": [
        "certifications",
        "certificates",
        "courses"
    ],

    "Achievements": [
        "achievements",
        "awards",
        "honors"
    ]
}


# ------------------------------------------------------------
# Detect Sections
# ------------------------------------------------------------

def detect_sections(resume_text):

    text = resume_text.lower()

    detected = {}

    for section, keywords in SECTION_KEYWORDS.items():

        found = False

        for keyword in keywords:

            if keyword in text:
                found = True
                break

        detected[section] = found

    return detected


# ------------------------------------------------------------
# Contact Information Check
# ------------------------------------------------------------

def check_contact_information(resume_text):

    text = resume_text.lower()

    checks = {
        "Email": bool(
            re.search(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                resume_text
            )
        ),

        "Phone": bool(
            re.search(
                r"(\+?\d[\d\s\-]{8,}\d)",
                resume_text
            )
        ),

        "LinkedIn": "linkedin.com" in text,

        "GitHub": "github.com" in text
    }

    return checks


# ------------------------------------------------------------
# Resume Length Check
# ------------------------------------------------------------

def check_resume_length(resume_text):

    words = len(
        resume_text.split()
    )

    if words < 150:

        status = "Too Short"

    elif words <= 800:

        status = "Good"

    else:

        status = "Possibly Too Long"

    return {
        "word_count": words,
        "status": status
    }


# ------------------------------------------------------------
# Skill Detection
# ------------------------------------------------------------

def detect_skills(resume_text):

    common_skills = [

        "python",
        "java",
        "javascript",
        "typescript",
        "c",
        "c++",

        "html",
        "css",
        "react",
        "node.js",

        "sql",
        "mysql",
        "mongodb",

        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",

        "tensorflow",
        "pytorch",
        "scikit-learn",

        "pandas",
        "numpy",

        "streamlit",
        "flask",
        "django",

        "git",
        "github",

        "docker",
        "aws",
        "azure"
    ]

    text = resume_text.lower()

    found_skills = []

    for skill in common_skills:

        if skill in text:

            found_skills.append(skill)

    return found_skills


# ------------------------------------------------------------
# Calculate Section Score
# ------------------------------------------------------------

def calculate_section_score(sections):

    total_sections = len(sections)

    completed_sections = sum(
        sections.values()
    )

    if total_sections == 0:

        return 0

    return round(
        (completed_sections / total_sections) * 100
    )


# ------------------------------------------------------------
# Calculate Contact Score
# ------------------------------------------------------------

def calculate_contact_score(contact):

    total = len(contact)

    completed = sum(
        contact.values()
    )

    if total == 0:

        return 0

    return round(
        (completed / total) * 100
    )


# ------------------------------------------------------------
# Calculate Final ATS Score
# ------------------------------------------------------------

def calculate_ats_score(
    section_score,
    contact_score,
    length_score,
    skill_score
):

    score = (

        section_score * 0.40
        + contact_score * 0.20
        + length_score * 0.15
        + skill_score * 0.25

    )

    return round(score)


# ------------------------------------------------------------
# Complete ATS Analysis
# ------------------------------------------------------------

def analyze_resume_ats(resume_text):

    sections = detect_sections(
        resume_text
    )

    contact = check_contact_information(
        resume_text
    )

    length = check_resume_length(
        resume_text
    )

    skills = detect_skills(
        resume_text
    )

    section_score = calculate_section_score(
        sections
    )

    contact_score = calculate_contact_score(
        contact
    )

    # Length score

    if length["status"] == "Good":

        length_score = 100

    elif length["status"] == "Too Short":

        length_score = 60

    else:

        length_score = 70

    # Skill score

    if len(skills) >= 8:

        skill_score = 100

    elif len(skills) >= 5:

        skill_score = 80

    elif len(skills) >= 3:

        skill_score = 60

    else:

        skill_score = 40

    final_score = calculate_ats_score(
        section_score,
        contact_score,
        length_score,
        skill_score
    )

    return {

        "ats_score": final_score,

        "sections": sections,

        "contact": contact,

        "length": length,

        "skills": skills,

        "section_score": section_score,

        "contact_score": contact_score,

        "length_score": length_score,

        "skill_score": skill_score

    }