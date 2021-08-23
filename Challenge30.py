# [ MEDIUM ]
# You are given an array of non-negative integers that represents a two-dimensional elevation map
# where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
# and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def trapped_water(elevation_map: list[int]) -> int:
    last_max = None
    counter = 0
    liters = 0

    for i in range(len(elevation_map) - 1):
        if last_max is None:
            last_max = elevation_map[i]

        elif elevation_map[i] < last_max:
            counter += 1
            liters += (last_max - elevation_map[i])

        elif elevation_map[i] >= last_max:
            counter = 0
            last_max = elevation_map[i]

    if elevation_map[-1] < last_max:
        liters -= (last_max - elevation_map[-1]) * counter

    if liters < 0:
        liters = 0

    return liters


print(trapped_water([3, 0, 1, 0, 5]))  # 8
print(trapped_water([1, 2, 3, 2, 1]))  # 0
print(trapped_water([3, 2, 1, 1, 2, 5]))  # 6
print(trapped_water([3, 1, 2, 1, 0, 5]))  # 8
print(trapped_water([3, 1, 2, 1, 0, 2]))  # 4
print(trapped_water([3, 1, 1, 1, 1, 3]))  # 8
print(trapped_water([3, 1, 5, 1, 1, 3]))  # 6
print(trapped_water([1, 2, 3, 2, 1, 1, 1, 1]))  # 0
