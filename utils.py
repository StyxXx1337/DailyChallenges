from time import time

class Timer:
	__enter__(self):
		enter_time = time.now()

	__exit__(self):
		time_taken = enter_time - time.now()
		print("It took:", time_taken)


