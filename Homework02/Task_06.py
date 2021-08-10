"""The task #6.
The size of the loan and one-time interest on it are given.
Calculate the total with interest and overpayment.
"""


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_total_and_overpayment(input_string=None):
    """Get two numbers from a string and returns total and overpayment.

    :param input_string:
        String to be processed.
    :return:
        String: Total, overpayment.
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
            return -1
        except TypeError:
            print(str(element) + " is not a number.")
            return -1
        finally:
            numbers.append(element_value)

    if len(numbers) != 2:
        print("Please, enter TWO numbers.")
        return -1

    total = numbers[0] * (numbers[1] / 100.0) + numbers[0]
    overpayment = total - numbers[0]


    return total, overpayment


if __name__ == "__main__":
    user_input = input("Please, enter two numbers, separated by space.\n"
                       + "First one is total loan, second is one-time interest:\n")
    result = get_total_and_overpayment(user_input)
    if result != -1:
        print("\nTotal is ${:.2f}, overpayment is ${:.2f}.".format(result[0], result[1]))
