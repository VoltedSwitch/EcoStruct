from constants.key import PARSED, PROMPT, UNPARSED


def parse(prompt):
    unparsed = input(prompt)
    parsed = unparsed.strip().lower()

    return {PARSED: parsed, PROMPT: prompt, UNPARSED: unparsed}
