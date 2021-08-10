# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
#

def string_to_list(string: str, word_list: list) -> list:
	"""
	Recursive Solution"""
	result = []
	if string == "":
		return []

	# checker is a word was found
	found = False
	for word in word_list:
		if string.find(word) == 0:
			found = True
			way = string_to_list(string[len(word):], word_list)
			
			# Check if a matching word was found
			if way == None:
				return None

			# Create a list to extend with the result, so that the words are in the right order
			result = [word, ]
			result.extend(way)
	
	# if no word could be found, then it can't be created
	if found == False:
		return None

	return result



print(string_to_list("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(string_to_list("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
print(string_to_list("aaaaaaaaaaaaaaaaaaz", ['aaaaaaaaa', 'bbbbbbbb', 'cccccc', 'dddddd', 'eeeeee']))