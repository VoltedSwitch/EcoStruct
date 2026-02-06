class Project:
    def __init__(self, name, members, goal, progress):
        self.name = name
        self.members = members
        self.goal = goal
        self.progress = progress
        self.status = "Planned"
