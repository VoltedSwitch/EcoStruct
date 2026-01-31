from states import States
from user_phases import get_organization_name, get_member_names, get_menu_option


class Navigation:
    STARTING_STATE = States.GET_ORGANIZATION_NAME
    current_state = STARTING_STATE
    previous_states = []

    PHASES = {
        States.GET_ORGANIZATION_NAME: get_organization_name,
        States.GET_MEMBER_NAMES: get_member_names,
        States.GET_MENU_OPTION: get_menu_option,
    }

    @staticmethod
    def navigate_state(state):
        if state not in Navigation.PHASES:
            raise ValueError("Invalid state within phases!")

        if Navigation.current_state not in Navigation.previous_states:
            Navigation.previous_states.append(Navigation.current_state)
        else:
            Navigation.previous_states.remove(Navigation.current_state)
        Navigation.current_state = state

    @staticmethod
    def run_current_state():
        return Navigation.PHASES[Navigation.current_state]()
