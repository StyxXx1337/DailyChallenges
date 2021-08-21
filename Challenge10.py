# [ MEDIUM ]
# Implement a job scheduler
# which takes in a function f and an integer n,
# and calls f after n milliseconds.

# =================== Without Thread ============================

from typing import Callable
import time


def job_scheduler(func: Callable, n: int) -> Callable:
    time.sleep(n)
    return func()


def print_something() -> bool:
    return True


print("=========== None-Threading Solution ============")
print(job_scheduler(print_something, 0.50))
print('\n')


# =================== Without Thread ============================
print("=========== Threading Solution ============")
from threading import Thread


def print_something_with_args(something: str) -> bool:
    print(something)
    return True


job = Thread(
    target=job_scheduler, args=(lambda: print_something_with_args("Hello There!"), 0.5)
)

print("Start")
job.start()
time.sleep(1)
print("Stop")
