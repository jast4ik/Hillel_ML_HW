"""The task #2.
Three numbers are given. Withdraw their sum.
"""


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_sum(input_string=None):
    """Get numbers from a string and sum their values.

    :param input_string:
        String to be processed.
    :return:
        The sum of numbers in a line.
    """

    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return -1

    input_string = input_string.strip()
    separated_string = input_string.split()
    numbers = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print(str(element) + " is not a number.")
        except TypeError:
            print(str(element) + " is not a number.")
        finally:
            numbers.append(element_value)

    return sum(numbers)


if __name__ == "__main__":
    user_input = input("Please, enter set of numbers, separated by space:\n")
    print("\nSum of entered numbers is: " + str(get_sum(user_input)))
