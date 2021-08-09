"""The task #9.
Two numbers are given. Withdraw smaller.
"""


import numpy as np


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_smallest(input_string=None):
    """Get two numbers from a string and returns smaller one.

    :param input_string:
        String to be processed.
    :return:
        Smallest number.
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

    if len(numbers) > 2:
        print("Please, enter TWO numbers.")
        return np.inf

    return min(numbers)


if __name__ == "__main__":
    user_input = input("Please, enter two numbers, separated by space:\n")
    smallest_number = get_smallest(user_input)
    if smallest_number != np.inf:
        print("\nSmallest numbers is: " + str(smallest_number))
