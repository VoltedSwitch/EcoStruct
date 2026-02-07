import input
import screen
import version

from constants.default import MEMBER_COUNTER
from constants.key import PARSED, PROMPT, UNPARSED, NAME, MEMBERS, GOAL, PROGRESS
from constants.command import GO_BACK, CREATE_PROJECT, DONE

from validators import valid_list_digit, valid_range_digit
from colors import Colors


def get_input_status(input_info):
    return input_info[PROMPT] + input_info[UNPARSED]


def collect_member_names(before_prompt_messages=None):
    OPTIONS = ("1", "2")
    counter = MEMBER_COUNTER

    input_taken_states = []
    members = []

    required_field_message = {
        "message1": "You cannot submit blank",
        "message2": "Please input organization member's names before hitting done!",
        "message3": "Please input a valid member name or option!",
        "display": "",
    }

    while True:
        print(version.display)

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            print()
            print()
            required_field_message["display"] = ""

        if before_prompt_messages:
            for message in before_prompt_messages:
                print(message)
                if message != before_prompt_messages[-1]:
                    print()

        for state in input_taken_states:
            print(state)

        name = input.parse(f"Enter name of member #{counter} OR (1) Back, (2) Done: ")
        screen.clear()

        if not name[PARSED]:
            required_field_message["display"] = "message1"
            continue
        elif name[PARSED] in OPTIONS:
            if name[PARSED] == "1":
                return GO_BACK
            elif name[PARSED] == "2" and members:
                return members
            else:
                required_field_message["display"] = "message2"
        elif "".join(name[PARSED].split()).isalpha():
            input_taken_states.append(get_input_status(name))
            members.append(name[PARSED])
            counter += 1
        else:
            required_field_message["display"] = "message3"


def select_member_names(member_names, before_prompt_messages=None):
    required_field_message = {
        "message1": "This field is required!",
        "message2": "Please input a valid member digit or option!",
        "message3": "You must check at least one participating member from your organization before hitting done!",
        "display": "",
    }
    OPTIONS = ("b", "d")
    members_state = {member: False for member in member_names}

    while True:
        print(version.display)

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            required_field_message["display"] = ""
            print()

        if before_prompt_messages:
            for message in before_prompt_messages:
                print(message)
                if message != before_prompt_messages[-1]:
                    print()

        for counter, member in enumerate(member_names, start=1):
            print(f"({counter}) {member} {"✔️" if members_state[member] else ""}")
        print()

        selected_member = input.parse(
            "Enter a member number to include that member or (b) to back and (d) done: "
        )
        screen.clear()

        if not selected_member[PARSED]:
            required_field_message["display"] = "message1"
            continue
        elif not (
            selected_member[PARSED] in OPTIONS
            or valid_list_digit(member_names, selected_member[PARSED])
        ):
            required_field_message["display"] = "message2"
            continue
        elif selected_member[PARSED].isdigit():
            member_index = int(selected_member[PARSED]) - 1
            selected_member_name = member_names[member_index]
            members_state[selected_member_name] = not members_state[
                selected_member_name
            ]
        elif selected_member[PARSED] in OPTIONS:
            if selected_member[PARSED] == "d":
                selected_members = [
                    member for member, state in members_state.items() if state
                ]
                if selected_members:
                    return selected_members
                required_field_message["display"] = "message3"
                continue
            elif selected_member[PARSED] == "b":
                return GO_BACK


def get_organization_details():
    required_field_message = {"message": "You cannot submit blank!", "display": False}

    while True:
        print(version.display)

        if required_field_message["display"]:
            print(Colors.color_error_message(required_field_message["message"]))
            print()
            required_field_message["display"] = False

        name = input.parse("Enter your organization name: ")
        screen.clear()

        if not name[PARSED]:
            required_field_message["display"] = True
            continue

        members = collect_member_names()

        if members == GO_BACK:
            continue

        return {NAME: name[PARSED], MEMBERS: members}


def choose_menu_option():
    required_field_message = {
        "message1": "You cannot submit blank!",
        "message2": "Please enter a valid option!",
        "display": "",
    }

    while True:
        print(version.display)

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            print()
            required_field_message["display"] = False

        print("(1) Create New Project")
        # Already created projects displayed in between if any
        print("(2) Back")
        print()
        print()

        choice = input.parse("> ")
        screen.clear()

        if not choice[PARSED]:
            required_field_message["display"] = "message1"
        elif choice[PARSED] == "1":
            return CREATE_PROJECT
        elif choice[PARSED] == "2":
            return GO_BACK
        else:
            required_field_message["display"] = "message2"


def project_details(member_names):
    required_field_message = {
        "message1": "This field is required!",
        "message2": "Progress has to be a digit between 0 & 100!",
        "display": "",
    }

    while True:
        print(version.display)

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            required_field_message["display"] = ""

        name = input.parse("Enter project name or (b) back: ")
        screen.clear()

        if not name[PARSED]:
            required_field_message["display"] = "message1"
            continue

        if name[PARSED] == "b":
            return GO_BACK
        break

    while True:
        print(version.display)

        print(get_input_status(name))
        print()

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            required_field_message["display"] = ""

        goal = input.parse("Enter project goal or (b) back: ")
        screen.clear()

        if not goal[PARSED]:
            required_field_message["display"] = "message1"
            continue

        if goal[PARSED] == "b":
            return GO_BACK
        break

    while True:
        print(version.display)

        print(get_input_status(name))
        print()
        print(get_input_status(goal))
        print()

        if required_field_message["display"]:
            print(
                Colors.color_error_message(
                    required_field_message[required_field_message["display"]]
                )
            )
            required_field_message["display"] = ""

        progress = input.parse("Enter your project progress from 0-99 or (b) back: ")
        screen.clear()

        if not progress[PARSED]:
            required_field_message["display"] = "message1"
            continue
        elif progress[PARSED] == "b":
            return GO_BACK
        elif valid_range_digit(range(100), progress[PARSED]):
            break
        else:
            required_field_message["display"] = "message2"

    while True:
        before_prompt_messages = [
            get_input_status(name),
            get_input_status(goal),
            get_input_status(progress),
            "List participating members from your organization\n",
        ]

        members = select_member_names(member_names, before_prompt_messages)

        if members == GO_BACK:
            return GO_BACK

        return {
            NAME: name[PARSED],
            GOAL: goal[PARSED],
            PROGRESS: int(progress[PARSED]),
            MEMBERS: members,
        }


def project_management():
    pass
