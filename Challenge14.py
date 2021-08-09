# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.


import random
import math


def pi_monte_carlo(amount: int) -> float:
    """Creates amount of random point to estimate PI and returns the estimation
    :param amount: amount of points created to estimate PI
    :return float: estimation of PI
    """

    points_inside = 0
    points_outside = 0

    # random range between 0 and 1 creates a quater circle
    for i in range(amount):
        x = random.random()
        y = random.random()

        radius = x * x + y * y

        if radius <= 1:
            points_inside += 1
        else:
            points_outside += 1

    # pi estimate is the relationship between correct and wrong times 4
    # (Quater of a circle to full circle)
    estimate = (points_inside / (points_inside + points_outside)) * 4

    return estimate


def pi_monte_carlo_pre(precision: int) -> float:
    """returns an estimation of PI with amount of matching decimal numbers
    :param precision: amount of matching decimal numbers
    :return pi: float
    """
    points_inside = 0
    points_outside = 0
    # random range between 0 and 1 creates a quater circle
    gap = 1
    while gap >= 1:
        x = random.random()
        y = random.random()

        radius = x * x + y * y

        if radius <= 1:
            points_inside += 1
        else:
            points_outside += 1

        # pi estimate is the relationship between correct and wrong times 4
        # (Quater of a circle to full circle)
        estimate = (points_inside / (points_inside + points_outside)) * 4

        gap = abs(math.pi - estimate)
        gap *= 10 ** (precision + 1)

    return estimate


# Test Code:


print(math.pi)  # Returns PI to compare
print(pi_monte_carlo(1000000))  # Creates 1000000 points to estiamte PI
print(pi_monte_carlo_pre(3))  # Runs until 3 decimal precision is reached.
