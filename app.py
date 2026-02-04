import screen
import prompt
import control
from constants.key import OUTPUT, TO_RUN
from navigation import Navigation
from organization import Organization

screen.clear()

to_run = control.generate_map(to_run=prompt.organization_name)[TO_RUN]

organization_name = None
member_names = None
menu_option = None

while True:
    if to_run is prompt.organization_name:
        control_map = prompt.organization_name()

        organization_name = control_map[OUTPUT]
        to_run = control_map[TO_RUN]

    elif to_run is prompt.member_names:
        control_map = prompt.member_names()

        member_names = control_map[OUTPUT]
        to_run = control_map[TO_RUN]

    elif to_run is prompt.menu_option:
        control_map = prompt.menu_option()

        menu_option = control_map[OUTPUT]
        to_run = control_map[TO_RUN]
        
    print()
