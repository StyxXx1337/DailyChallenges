# This function takes 2 Arguments:
# 			number: 	 int
# 			number_list: a list of numbers
#
#	Function returns True, if 2 numbers in the number_list can be added to make number
#
#	2021-07-15

from time import time

def any_two_numbers(number: int, number_list: list) -> bool:

	temp_list = []

	for n in number_list:
		if (number - n) in number_list:
			return True

	return False


print(any_two_numbers(15, [1,3,9,10,12])) # True
print(any_two_numbers(12, [10,7,9,11,12])) # False
print(any_two_numbers(99, [10,30,9,100,18])) # False
print(any_two_numbers(0, [])) # False
print(any_two_numbers(0, [-1,3,9,1,12])) # True