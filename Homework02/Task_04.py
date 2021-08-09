"""The task #4.
Calculate the side of a square by its area.
"""

import math


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_square_side(input_string=None):
    """Returns the side of a square.

    :param input_string:
        String to be processed.
    :return:
        The side.
    """
    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return -1

    input_string = input_string.strip()
    number = 0.0

    try:
        number = float(input_string)
    except ValueError:
        print(str(input_string) + " is not a number.")
        return -1
    except TypeError:
        print(str(input_string) + " is not a number.")
        return -1

    if number < 0.0:
        print("Please, enter positive number.")
        return -1

    return math.sqrt(number)


if __name__ == "__main__":
    user_input = input("Please, enter the area of the square:\n")
    side = get_square_side(user_input)
    if side != -1:
        print("The side of the square is: {:.4f}".format(side))
