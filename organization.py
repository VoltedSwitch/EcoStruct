from random import randint

from member import Member
from project import Project
from data_manager import DataManager


class Organization(DataManager):
    def __init__(self, name, member_names):
        self.name = name
        self.members = self.create_members(member_names)
        self.projects = []

    def create_members(self, member_names):
        members = {}

        for member_name in member_names:
            member = Member(member_name)
            id_number = self.generate_id(members.keys())

            members.update({id_number: member})

        return members

    def add_project(self, members, project_title, goal):
        project = Project(project_title, members, goal)
        self.projects.append(project)

    def remove_project(self, project_number):
        index = project_number - 1
        self.projects.pop(index)

    def generate_id(self, id_numbers):
        while True:
            id_number = randint(10000, 99999)

            if id_number not in id_numbers:
                return id_number

    def format_data_for_saving(self):
        return {
            "organization_name": self.name,
            "members": {
                id_number: member.format_data_for_saving()
                for id_number, member in self.members.items()
            },
            "projects": self.projects,
        }
