# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# • 1, 1, 1, 1
# • 2, 1, 1
# • 1, 2, 1
# • 1, 1, 2
# • 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def unique(steps: int) -> int:
    one_step = {1, 2}
    ways = 0

    if steps < 1:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2

    for el in one_step:
        remainder = steps - el
        result = unique(remainder)
        if result is not None:
            ways += result

    return ways


# print(unique(4))  # Result: 5
# print(unique(2))  # Result: 2
# print(unique(1))  # Result: 1
# print(unique(0))  # Result: None
# print(unique(6))  # Result: 13


def unique_plus(target: int, one_steps=[1, 2]) -> int:
    ways = 0

    if target < 0:
        return None

    if target == 0:
        return 1

    for step in one_steps:
        remainder = target - step
        if unique_plus(remainder) is not None:
            ways += unique_plus(remainder)

    return ways


print(unique_plus(4))  # Result: 5
print(unique_plus(2))  # Result: 2
print(unique_plus(1))  # Result: 1
print(unique_plus(0))  # Result: 1 - None of the elements.
print(unique_plus(6))  # Result: 13
