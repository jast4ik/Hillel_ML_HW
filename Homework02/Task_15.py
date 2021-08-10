"""The task #15.
Three sides of the triangle are given. Determine if a triangle is isosceles or equilateral.
"""

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def is_isosceles_or_equilateral(input_string=None):
    """Get three sides of the triangle and returns is it isosceles or equilateral.

    :param input_string:
        String to be processed.
    :return:
        String: Is isosceles, is equilateral in natural language.
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

    triangle_exist = False
    if (sides[0] + sides[1]) > sides[2]:
        triangle_exist = True

    if not triangle_exist:
        print("A triangle with such sides does not exist.")
        return -1

    is_equilateral = False
    is_isosceles = False

    if (sides[0] == sides[1]) and (sides[0] == sides[2]) and (sides[1] == sides[2]):
        is_equilateral = True
    elif (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]):
        is_isosceles = True

    result = "Triangle"

    if not is_equilateral and not is_isosceles:
        result += " neither isosceles nor equilateral."
    elif is_equilateral:
        result += " is equilateral."
    elif is_isosceles:
        result += " is isosceles."

    return result


if __name__ == "__main__":
    user_input = input("Please, enter three sides of the triangle, separated by space:\n")
    triangle_metrics = is_isosceles_or_equilateral(user_input)
    if triangle_metrics != -1:
        print(triangle_metrics)
