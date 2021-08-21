# [ MEDIUM ]
# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
# More specifically, you should have as many words as possible in each line. There should be at least one space between each word.
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
# you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


def justify_text(in_list: list[str], k: int) -> list[str]:
    solution = []
    start = 0
    k_counter = 0
    word_counter = 0

    for i in range(len(in_list)):
        k_counter += len(in_list[i])
        word_counter += 1

        if k_counter >= k:
            if k_counter == k:
                # If there is no need for extra spaces just join
                temp = ' '.join(in_list[start : i + 1])
                solution.append(temp)
                start = i + 1
                k_counter = 0

            else:
                # If there are additional spaces to be distributed
                k_counter -= len(in_list[i]) + 1  # -1 for the additional Space
                print(k_counter)
                word_counter -= 1
                extra_spaces = k - k_counter
                space_per_gap = extra_spaces // (word_counter - 1)
                left_overs = extra_spaces % (word_counter - 1)

                # For DEBUGGING
                print("extra_spaces: ", extra_spaces)
                print("space_per_gap: ", space_per_gap)
                print("left_overs: ", left_overs)

                temp_list = []

                # TODO Doesnt work....
                for item in range(start, i):
                    temp_list.append(in_list[item])
                    if item < (i - 1):
                        if space_per_gap > 0:
                            temp_list.append(
                                ' ' * space_per_gap
                            )  # Issue since the 'join' adds an other SPACE.
                        if left_overs > 0:
                            temp_list.append(' ')
                            left_overs -= 1

                print(temp_list)

                temp = ' '.join(temp_list)
                solution.append(temp)
                start = i
                k_counter = len(in_list[i])

        else:
            # Add one for the space
            k_counter += 1

    return solution


print(justify_text(["A", "B", "C"], 5))  # ["A B C"]
print(justify_text(["A", "B", "C"], 1))  # ["A", "B", "C"]
print(
    justify_text(
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16
    )
)  #
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly
