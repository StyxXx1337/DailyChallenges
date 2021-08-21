# [ EASY ]
# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


def is_well_formated(input: str) -> bool:
    opening = "({["
    open_string = []

    pairs = {"(": ")", "{": "}", "[": "]"}

    for ch in input:
        if ch in opening:
            open_string.append(ch)
        elif (len(open_string) > 0) and pairs[open_string[-1]] == ch:
            open_string = open_string[:-1]
        else:
            return False

    if len(open_string) == 0:
        return True
    else:
        return False


print(is_well_formated("([])[]({})"))  # True
print(is_well_formated("([)]"))  # False
print(is_well_formated("((((("))  # False
print(is_well_formated("(((]]]"))  # False
print(is_well_formated("]]]"))  # False
