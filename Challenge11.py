# Implement an autocomplete system.
# That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].


def autocomplete(string: str, option_list: list[str]) -> list[str]:
    answers = []
    for element in option_list:
        if element.find(string) == 0:
            answers.append(element)

    return answers


print(autocomplete("de", ["dog", "deer", "deal"]))  # [deer, deal]
