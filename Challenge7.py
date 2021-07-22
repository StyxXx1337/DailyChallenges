# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# 
# 
# 
# 2021-07-22

# Simple Brute Force Implementation
def decode_numbers(message: str, decoder: dict) -> int:
	amount = 0
	# In case a Integer is given instead of a string
	message = str(message)

	if message == "":
		return 1

	for el in decoder.values():
		if message.find(str(el)) == 0:
			amount += decode_numbers(message[len(str(el)):], decoder)
	
	return amount


# Including memorization
def decode_numbers_memo(message: str, decoder: dict, memo = {}) -> int:
	# In case a Integer is given instead of a string
	message = str(message)	
	amount = 0


	if message == "":
		return 1
	if message in memo:
		return memo[message]

	for el in decoder.values():
		if message.find(str(el)) == 0:
			amount += decode_numbers_memo(message[len(str(el)):], decoder, memo)
			memo[message] = amount

	return amount





dec = {
	   'a': 1, 'b': 2 , 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
	   'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
	   'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 
	   }

print(decode_numbers(1111, dec))
print(decode_numbers_memo(1111111111111111111111111111111111111111111111111, dec))
print(decode_numbers_memo(123456789987654321123456789987654321, dec))
print(decode_numbers_memo(1212121212121212121212121212121212121, dec))
print(decode_numbers_memo(111, dec))
print(decode_numbers_memo(26262626262626262626, dec))
