class GitHubProfile:

    def __init__(
        self,
        username="",
        repositories=0,
        followers=0,
        following=0,
        languages=None
    ):

        self.username = username
        self.repositories = repositories
        self.followers = followers
        self.following = following
        self.languages = languages if languages else []

    def to_dict(self):

        return {
            "username": self.username,
            "repositories": self.repositories,
            "followers": self.followers,
            "following": self.following,
            "languages": self.languages
        }