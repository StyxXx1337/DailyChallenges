# [ EASY ]
# The power set of a set is the set of all its subsets.
# Write a function that, given a set, generates its power set.
#
# For example, given the set {1, 2, 3}:
# it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.


def power_of_sets(in_set: set) -> set:
    if len(in_set) == 0:
        return in_set

    return_set = set()
    print(in_set)

    for el in in_set:
        sub_set = in_set.copy()
        sub_set.remove(el)
        re = power_of_sets(sub_set)

        if re is None:
            return_set.add({})
        else:
            return_set.add(re)

        return sub_set

    return return_set


print(power_of_sets({1, 2, 3}))
