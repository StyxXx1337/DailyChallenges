# [ EASY ]
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def determine_amount_of_rooms(time_schedule: list) -> int:
    pointer = 0
    amount_of_rooms = 1

    while pointer < len(time_schedule):
        for i in range(pointer + 1, len(time_schedule)):
            if (time_schedule[pointer][0] > time_schedule[i][0]) and (
                time_schedule[pointer][0] < time_schedule[i][1]
            ):
                amount_of_rooms += 1

        pointer += 1

    return amount_of_rooms


print(determine_amount_of_rooms([(30, 75), (0, 50), (60, 150)]))  # 2
print(determine_amount_of_rooms([(30, 75), (30, 50), (10, 80)]))  # 3
print(determine_amount_of_rooms([(30, 75), (75, 100), (100, 150)]))  # 1
