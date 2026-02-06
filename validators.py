def valid_list_digit(lst, digit):
    if not digit.isdigit():
        return False

    index = int(digit) - 1

    if 0 <= index < len(lst):
        return True


def valid_range_digit(range, digit):
    if not digit.isdigit():
        return False

    if int(digit) in range:
        return True

    return False
