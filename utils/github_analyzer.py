# ============================================================
# CAREERPILOT AI - GITHUB ANALYZER V2
# ============================================================

from collections import Counter
from datetime import datetime, timezone


def analyze_languages(repositories):

    languages = []

    for repo in repositories:

        language = repo.get("language")

        if language:
            languages.append(language)

    return Counter(languages)


def calculate_star_score(repositories):

    total_stars = sum(
        repo.get("stargazers_count", 0)
        for repo in repositories
    )

    if total_stars >= 50:
        return 100

    if total_stars >= 20:
        return 85

    if total_stars >= 10:
        return 70

    if total_stars >= 1:
        return 55

    return 40


def calculate_repository_quality(repo):

    score = 0

    if repo.get("description"):
        score += 15

    if repo.get("language"):
        score += 15

    if repo.get("topics"):
        score += 15

    if repo.get("html_url"):
        score += 10

    if not repo.get("fork", False):
        score += 10

    if repo.get("stargazers_count", 0) > 0:
        score += 10

    if repo.get("forks_count", 0) > 0:
        score += 5

    if repo.get("size", 0) > 0:
        score += 10

    if repo.get("default_branch"):
        score += 10

    return min(score, 100)


def analyze_repositories(repositories):

    results = []

    for repo in repositories:

        quality_score = calculate_repository_quality(
            repo
        )

        results.append(
            {
                "name": repo.get(
                    "name",
                    "Unknown"
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
                ),

                "url": repo.get(
                    "html_url"
                ),

                "updated_at": repo.get(
                    "updated_at"
                ),

                "quality_score": quality_score
            }
        )

    results.sort(
        key=lambda repo: repo["quality_score"],
        reverse=True
    )

    return results


def calculate_repository_score(repositories):

    if not repositories:
        return 0

    analyzed = analyze_repositories(
        repositories
    )

    scores = [
        repo["quality_score"]
        for repo in analyzed
    ]

    return round(
        sum(scores) / len(scores)
    )


def calculate_activity_score(repositories):

    if not repositories:
        return 0

    now = datetime.now(
        timezone.utc
    )

    recent_count = 0

    for repo in repositories:

        updated_at = repo.get(
            "updated_at"
        )

        if not updated_at:
            continue

        try:

            updated = datetime.fromisoformat(
                updated_at.replace(
                    "Z",
                    "+00:00"
                )
            )

            days_old = (
                now - updated
            ).days

            if days_old <= 90:
                recent_count += 1

        except ValueError:

            continue

    return round(
        (recent_count / len(repositories))
        * 100
    )


def calculate_documentation_score(
    repositories
):

    if not repositories:
        return 0

    documented = 0

    for repo in repositories:

        has_description = bool(
            repo.get("description")
        )

        has_topics = bool(
            repo.get("topics")
        )

        if has_description:
            documented += 1

        elif has_topics:
            documented += 0.5

    return round(
        (documented / len(repositories))
        * 100
    )


def calculate_profile_score(profile):

    score = 0

    if profile.get("name"):
        score += 15

    if profile.get("bio"):
        score += 20

    if profile.get("company"):
        score += 10

    if profile.get("location"):
        score += 10

    if profile.get("blog"):
        score += 10

    if profile.get(
        "twitter_username"
    ):
        score += 5

    if profile.get(
        "public_repos",
        0
    ) >= 3:

        score += 15

    if profile.get(
        "followers",
        0
    ) > 0:

        score += 15

    return score


def calculate_github_score(
    profile_score,
    repository_score,
    activity_score,
    documentation_score,
    star_score
):

    score = (
        profile_score * 0.20
        + repository_score * 0.30
        + activity_score * 0.15
        + documentation_score * 0.20
        + star_score * 0.15
    )

    return round(score)


def analyze_github(
    github_data
):

    profile = github_data[
        "profile"
    ]

    repositories = github_data[
        "repositories"
    ]

    languages = analyze_languages(
        repositories
    )

    repository_details = analyze_repositories(
        repositories
    )

    profile_score = calculate_profile_score(
        profile
    )

    repository_score = calculate_repository_score(
        repositories
    )

    activity_score = calculate_activity_score(
        repositories
    )

    documentation_score = calculate_documentation_score(
        repositories
    )

    star_score = calculate_star_score(
        repositories
    )

    github_score = calculate_github_score(
        profile_score,
        repository_score,
        activity_score,
        documentation_score,
        star_score
    )

    return {
        "github_score": github_score,

        "profile_score": profile_score,

        "repository_score": repository_score,

        "activity_score": activity_score,

        "documentation_score": documentation_score,

        "star_score": star_score,

        "languages": languages,

        "repository_details": repository_details,

        "repository_count": len(
            repositories
        ),

        "total_stars": sum(
            repo.get(
                "stargazers_count",
                0
            )
            for repo in repositories
        ),

        "total_forks": sum(
            repo.get(
                "forks_count",
                0
            )
            for repo in repositories
        )
    }