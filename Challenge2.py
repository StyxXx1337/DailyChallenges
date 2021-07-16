# This function takes 1 Arguments:
# 			number_list: a list of numbers
#
#	Function returns a n number list which has the product of all other numbers besides the number at the given location
# 	E.g. Input: [1,2,3,4,5] --> [120, 60, 40, 30, 24]
#
#	2021-07-16

from typing import List
import math

# simple implementation
def product_list(number_list: List[int]) -> List[int]:
	maximum = math.prod(number_list)
	return [maximum/x for x in number_list]

print("---------- Standard Solution ---------")
print(product_list([1,2,3,4,5]))
print(product_list([10,2,3,4,5]))
print(product_list([5,5,5,5,5]))
print(product_list([1,1,1,1,1]))


@Timer
# implementation without division 1 [List Comprehension]
def product_list_no_division_1(number_list: List[int]) -> List[int]:
	temp = []
	for i, number in enumerate(number_list):
		temp.append(math.prod([el for index, el in enumerate(number_list) if index != i]))

	return temp

print("---------- No Division Solution # 1 ---------")
print(product_list_no_division_1([1,2,3,4,5]))
print(product_list_no_division_1([10,2,3,4,5]))
print(product_list_no_division_1([5,5,5,5,5]))
print(product_list_no_division_1([1,1,1,1,1]))


# implementation without division 2 [List Buffer]
def product_list_no_division_2(number_list: List[int]) -> List[int]:
	copy = number_list.copy()
	temp = []
	result = []
	for el in copy:
		number_list.remove(el)
		if temp:
			result.append(math.prod(temp) * math.prod(number_list))
		else:
			result.append(math.prod(number_list))

		temp.append(el)

	return result


print("---------- No Division Solution # 2 ---------")
print(product_list_no_division_2([1,2,3,4,5]))
print(product_list_no_division_2([10,2,3,4,5]))
print(product_list_no_division_2([5,5,5,5,5]))
print(product_list_no_division_2([1,1,1,1,1]))