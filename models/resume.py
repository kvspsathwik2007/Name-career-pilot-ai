class Resume:

    def __init__(
        self,
        name="",
        education="",
        skills=None,
        projects=None,
        experience=""
    ):

        self.name = name
        self.education = education
        self.skills = skills if skills else []
        self.projects = projects if projects else []
        self.experience = experience

    def to_dict(self):

        return {
            "name": self.name,
            "education": self.education,
            "skills": self.skills,
            "projects": self.projects,
            "experience": self.experience
        }