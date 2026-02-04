class Member:
    def __init__(self, name):
        self.name = name
        self.roles = []

    def format_data_for_saving(self):
        return {"member_name": self.name, "roles": self.roles}
