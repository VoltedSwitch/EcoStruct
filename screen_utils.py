def clear_screen():
    print("\033[2J\033[H", end="")


def hide_cursor():
    print("\033[?25l", end="")


def show_cursor():
    print("\033[?25h", end="")
