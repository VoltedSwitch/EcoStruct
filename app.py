import screen
import prompt
from constants.command import GO_BACK, CREATE_PROJECT, DONE
from constants.key import NAME, MEMBERS, GOAL, PROGRESS
from organization import Organization

screen.clear()

to_run = prompt.get_organization_details

organization = None

while True:
    if to_run is prompt.get_organization_details:
        result = to_run()
        organization = Organization(result[NAME], result[MEMBERS])
        to_run = prompt.choose_menu_option

    elif to_run is prompt.choose_menu_option:
        result = to_run()

        if result == GO_BACK:
            to_run = prompt.get_organization_details
        elif result == CREATE_PROJECT:
            to_run = prompt.project_details

    elif to_run is prompt.project_details:
        result = to_run(organization.member_names)

        if result == GO_BACK:
            to_run = prompt.choose_menu_option
        else:
            if organization:
                organization.add_project(
                    result[NAME], result[MEMBERS], result[GOAL], result[PROGRESS]
                )

    elif to_run is prompt.project_management:
        result = to_run()
