class Project:
    def __init__(self, name, members, goal):
        self.name = name
        self.members = members
        self.goal = goal
        self.progress = 0
        self.status = "Planned"
