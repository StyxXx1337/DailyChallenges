# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
# subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# •	10 = max(10, 5, 2)
# •	7 = max(5, 2, 7)
# •	8 = max(2, 7, 8)
# •	8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

def max_sub_array(array: list, length: int)-> list:
    """Solution with 
    Time Complexity: O(n)
    Space Complexity: O(n+k)
    """
    start = 0
    result =[] # Additional Space of (len(array) - 1)
    end = length

    while end <= len(array): # Time Complexity O(n-k) -> Worst Case O(n) n -> inf k = 1
        result.append(max(array[start:end])) # Additional Space in every loop of O(k)
        start += 1
        end += 1

    return result


print(max_sub_array([10,5,2,7,8,7],3))

def max_sub_array_inplace(array: list, length: int)-> list:
    """Solution with 
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    start = 0
    end = length

    while end <= len(array): # Time Complexity O(n-k) -> Worst Case O(n) n -> inf k = 1
        array[start] = max(array[start:end]) # Additional Space in every loop of O(k)
        start += 1
        end += 1

    return array[:-2]

print(max_sub_array_inplace([10,5,2,7,8,7],3))
