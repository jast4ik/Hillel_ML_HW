"""The task #3.
Given a number, display the next and previous relative to it.
"""

import numpy as np

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_next_and_previous(input_string=None):
    """Returns the previous, entered and next number.

    :param input_string:
        String to be processed.
    :return:
        Tuple. Previous, current, next.
    """
    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return np.inf, np.inf, np.inf

    input_string = input_string.strip()
    number = 0.0

    try:
        number = int(input_string)
    except ValueError:
        print(str(input_string) + " is not a number.")
        return np.inf, np.inf, np.inf
    except TypeError:
        print(str(input_string) + " is not a number.")
        return np.inf, np.inf, np.inf

    return number - 1, number, number + 1


if __name__ == "__main__":
    user_input = input("Please, enter the number (integer):\n")
    all_numbers = get_next_and_previous(user_input)
    if all_numbers[0] != np.inf:
        print("Next for number "
              + str(all_numbers[1])
              + " is "
              + str(all_numbers[2])
              + ", previous is "
              + str(all_numbers[0]))
