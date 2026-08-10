class Profile:

    def __init__(
        self,
        name="",
        headline="",
        about="",
        skills=None,
        experience=""
    ):

        self.name = name
        self.headline = headline
        self.about = about
        self.skills = skills if skills else []
        self.experience = experience

    def to_dict(self):

        return {
            "name": self.name,
            "headline": self.headline,
            "about": self.about,
            "skills": self.skills,
            "experience": self.experience
        }