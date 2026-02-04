import input
import screen
import control
import presentation

from constants.default import MEMBER_COUNTER


def organization_name():
    while True:
        presentation.display_version()
        user_input = input.parse("Enter your organization name: ")

        if user_input:
            return control.generate_map(output=user_input, to_run=member_names)

        screen.clear()


def member_names():
    member_counter = MEMBER_COUNTER
    member_names = []

    while True:
        user_input = input.parse(
            f"Enter name of member #{member_counter} OR 1 -> Back, 2 -> Done: "
        )

        if user_input == "1":
            screen.clear()
            return control.generate_map(output=None, to_run=organization_name)
        elif user_input == "2":
            screen.clear()
            return control.generate_map(output=member_names, to_run=menu_option)
        else:
            member_names.append(user_input)
            member_counter += 1


def menu_option():
    while True:
        presentation.display_version()
        print("1 -> Create New Project")
        print("2 -> Back")
        presentation.seperate_options_and_input()
        user_input = input.parse("> ")
        screen.clear()

        if user_input == "1":
            break
        elif user_input == "2":
            pass
