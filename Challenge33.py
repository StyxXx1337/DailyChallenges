# [ EASY ]
# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def running_median(in_list: list[int]) -> None:
    temp_list = []

    for el in in_list:
        temp_list.append(el)
        if (len(temp_list) % 2) == 1:
            print(sorted(temp_list)[len(temp_list) // 2])
        else:
            temp_list.sort()
            median = (temp_list[len(temp_list) // 2] + temp_list[(len(temp_list) // 2) - 1]) / 2.0
            print(median)

    print("")


running_median([2, 1, 5, 7, 2, 0, 5])
running_median([5, 5, 5, 5, 5, 5, 5])
