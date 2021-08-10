"""The task #9.
Two numbers are given defining the interval.
Withdraw two numbers from an interval, rational and whole.
"""


import numpy as np
import random


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_random_numbers(input_string=None):
    """Get two numbers from a string and returns two numbers from an interval, rational and whole.

    :param input_string:
        String to be processed.
    :return:
        Tuple: Rational, whole.
    """

    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return np.inf

    input_string = input_string.strip()
    separated_string = input_string.split()
    numbers = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print(str(element) + " is not a number.")
            return np.inf
        except TypeError:
            print(str(element) + " is not a number.")
            return np.inf
        finally:
            numbers.append(element_value)

    if len(numbers) != 2:
        print("Please, enter TWO numbers.")
        return np.inf

    rational = random.uniform(numbers[0], numbers[1])
    whole = random.randint(int(numbers[0]), int(numbers[1]))

    return rational, whole


if __name__ == "__main__":
    user_input = input("Please, enter two numbers, separated by space:\n")
    result = get_random_numbers(user_input)
    if result != np.inf:
        print("\nRandom rational is {:.6f}, whole is {}.".format(result[0], result[1]))
