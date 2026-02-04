def parse(text, give_prompt=False, give_unparsed_user_input_also=False):
    unparsed = input(text)
    parsed = unparsed.strip().lower()

    if give_prompt:
        if give_unparsed_user_input_also:
            return parsed, text, unparsed
        return parsed, text
    else:
        if give_unparsed_user_input_also:
            return parsed, unparsed
        return parsed
