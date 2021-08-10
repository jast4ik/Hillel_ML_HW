"""The task #5.
Three sides of the triangle are given. Find its perimeter and area.
"""

import math

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def find_area_and_perimeter(input_string=None):
    """Get three sides of the triangle and returns its perimeter and area.

    :param input_string:
        String to be processed.
    :return:
        Tuple: Area, perimeter.
    """

    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return -1

    input_string = input_string.strip()
    separated_string = input_string.split()
    sides = []

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
            sides.append(element_value)

    if len(sides) != 3:
        print("Please, enter THREE sides.")
        return -1

    for side in sides:
        if side <= 0.0:
            print("Length cannot be negative or zero.")
            return -1

    perimeter = sum(sides)
    p = perimeter / 2.0

    triangle_exist = False
    if (sides[0] + sides[1]) > sides[2] \
            and (sides[0] + sides[2]) > sides[1] \
            and (sides[1] + sides[2]) > sides[0]:
        triangle_exist = True

    if not triangle_exist:
        print("A triangle with such sides does not exist.")
        return -1

    area = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

    factor = 10.0 ** 4

    return math.trunc(area * factor) / factor, math.trunc(perimeter * factor) / factor


if __name__ == "__main__":
    user_input = input("Please, enter three sides of the triangle, separated by space:\n")
    triangle_metrics = find_area_and_perimeter(user_input)
    if triangle_metrics != -1:
        print(
            "\nArea of the triangle is {} and perimeter is {}.".format(
                triangle_metrics[0], triangle_metrics[1]
            )
        )
