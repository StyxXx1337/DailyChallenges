# [ HARD ]
# This function takes 1 Arguments:
# 			number_list: a list of numbers
#
# 	Function should find the first positive integer greater than 0, that is missing in the array
# 	E.g. Input: [3,-1,1,4,5] --> 2
#
# 	2021-07-20


def find_missing_integer(number_list: list) -> int:
    value = 1
    while True:
        if not (value in number_list):
            return value
        else:
            value += 1


print(find_missing_integer([3, -1, 1, 4, 5]))  # 2
print(find_missing_integer([3, 0, 2, 4, 5]))  # 1
print(find_missing_integer([0, 2, 3, 4, 5]))  # 1
print(find_missing_integer([1, 1, 1, 1, 1]))  # 2
print(find_missing_integer([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # 10
