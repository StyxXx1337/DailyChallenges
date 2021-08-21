# [ HARD ]
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Can you do this in O(N) time and constant space?


def non_adjust_sum(number_list: list) -> int:

    if len(number_list) == 0:
        return 0
    elif len(number_list) <= 2:
        return max(number_list)

    uneven = non_adjust_sum(number_list[:-2]) + number_list[-1]
    even = non_adjust_sum(number_list[:-1])

    return max(uneven, even)


print(non_adjust_sum([2, 3, 6, 2, 5]))  # 13
print(non_adjust_sum([5, 1, 1, 5]))  # 10
print(non_adjust_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 23
print(non_adjust_sum([1, 2]))  # 2
print(non_adjust_sum([1]))  # 1
