from prompt import (
    organization_name,
    member_names,
    menu_option,
)


class Navigation:
    STARTING_STEP = organization_name

    _NEXT = {
        organization_name: member_names,
        member_names: menu_option,
    }
    _PREVIOUS = {
        member_names: organization_name,
        menu_option: member_names,
    }

    current_step = STARTING_STEP

    @staticmethod
    def move_to_previous_step():
        Navigation._update_current_state(Navigation._PREVIOUS)

    @staticmethod
    def move_to_next_step():
        Navigation._update_current_state(Navigation._NEXT)

    @staticmethod
    def _update_current_state(mapping):
        Navigation.current_step = mapping[Navigation.current_step]
