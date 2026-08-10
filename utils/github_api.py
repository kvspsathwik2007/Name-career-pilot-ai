# ============================================================
# CAREERPILOT AI - GITHUB API ENGINE
# ============================================================

import requests


GITHUB_API = "https://api.github.com"


def extract_username(github_input):

    github_input = github_input.strip()

    if "github.com/" in github_input:

        username = github_input.split(
            "github.com/"
        )[1]

        username = username.split("/")[0]

        username = username.split("?")[0]

        return username.strip()

    return github_input.strip().lstrip("@").strip()


def get_headers():

    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def get_profile(username):

    url = f"{GITHUB_API}/users/{username}"

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=15
    )

    if response.status_code == 404:

        raise ValueError(
            "GitHub user not found."
        )

    response.raise_for_status()

    return response.json()


def get_repositories(username):

    repositories = []

    page = 1

    while page <= 3:

        url = f"{GITHUB_API}/users/{username}/repos"

        params = {
            "per_page": 100,
            "page": page,
            "sort": "updated"
        }

        response = requests.get(
            url,
            headers=get_headers(),
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data:

            break

        repositories.extend(data)

        if len(data) < 100:

            break

        page += 1

    return repositories


def get_repository_readme(
    owner,
    repo
):

    url = (
        f"{GITHUB_API}/repos/"
        f"{owner}/{repo}/readme"
    )

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=15
    )

    if response.status_code == 404:

        return ""

    if response.status_code != 200:

        return ""

    data = response.json()

    return data.get(
        "content",
        ""
    )


def get_github_data(username):

    profile = get_profile(
        username
    )

    repositories = get_repositories(
        username
    )

    return {
        "profile": profile,
        "repositories": repositories
    }# ============================================================
# CAREERPILOT AI - GITHUB API ENGINE
# ============================================================

import requests


GITHUB_API = "https://api.github.com"


def extract_username(github_input):

    github_input = github_input.strip()

    if "github.com/" in github_input:

        username = github_input.split(
            "github.com/"
        )[1]

        username = username.split("/")[0]

        username = username.split("?")[0]

        return username.strip()

    return github_input.strip().lstrip("@").strip()


def get_headers():

    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def get_profile(username):

    url = f"{GITHUB_API}/users/{username}"

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=15
    )

    if response.status_code == 404:

        raise ValueError(
            "GitHub user not found."
        )

    response.raise_for_status()

    return response.json()


def get_repositories(username):

    repositories = []

    page = 1

    while page <= 3:

        url = f"{GITHUB_API}/users/{username}/repos"

        params = {
            "per_page": 100,
            "page": page,
            "sort": "updated"
        }

        response = requests.get(
            url,
            headers=get_headers(),
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data:

            break

        repositories.extend(data)

        if len(data) < 100:

            break

        page += 1

    return repositories


def get_repository_readme(
    owner,
    repo
):

    url = (
        f"{GITHUB_API}/repos/"
        f"{owner}/{repo}/readme"
    )

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=15
    )

    if response.status_code == 404:

        return ""

    if response.status_code != 200:

        return ""

    data = response.json()

    return data.get(
        "content",
        ""
    )


def get_github_data(username):

    profile = get_profile(
        username
    )

    repositories = get_repositories(
        username
    )

    return {
        "profile": profile,
        "repositories": repositories
    }