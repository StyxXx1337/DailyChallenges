# [ EASY ]
# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def run_length_encoding(in_string: str) -> str:

    last_element = None
    counter = 0
    return_string = ""

    for el in in_string:
        if last_element == None:
            last_element = el
            counter += 1

        elif last_element == el:
            counter += 1

        else:
            return_string += str(counter) + last_element
            last_element = el
            counter = 1

    return_string += str(counter) + last_element

    return return_string


print(run_length_encoding("AAAABBBCCDAA"))  # 4A3B2C1D2A
print(run_length_encoding("AAAAAAAA"))  # 8A
print(run_length_encoding("C"))  # 1C
