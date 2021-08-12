"""
#1.     User enters a name. Say hello to him by name and with an exclamation mark at the end.
#2.     Three nums are given. Withdraw their sum.
#3.     Given a number, display the next and previous relative to it.
#4.     Calculate the side of a square by its area.
#5.     Three sides of the triangle are given. Find its perimeter and area.
#6.     The size of the loan and one-time interest on it are given.Calculate the total with interest and overpayment.
#7.     Implement a simple calculator.
#8.     Two nums are given defining the interval. Withdraw two nums from an interval, rational and whole.
#9.     Two nums are given. Withdraw smaller.
#11.    Same as #7
#14.    One letter is given. Determine whether it is a vowel or a consonant.
#15.    Three sides of the triangle are given. Determine if a triangle is isosceles or equilateral.
"""

import re
import math
import random

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"
__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


# region Task #1
def get_hello_string(user_name=None):
    """Returns invitation string.

    :param user_name:
        User name. Only alphabetical characters will be proceed.
    :return:
        Invitation string.
    """

    if type(user_name) is not str:
        return "get_hello_string():\tCan't handle this type of input."

    regex = re.compile("[^a-zA-Z]")
    user_name = regex.sub("", user_name)

    return "Hello, {}!".format(user_name.strip())


# endregion


# region Task #2
def get_sum(input_string=None):
    """Get nums from a string and sum their values.

    :param input_string:
        String to be processed.
    :return:
        The sum of nums in a line.
    """

    if type(input_string) is not str:
        print("get_sum():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    numbs = []

    for element in separated_string:
        try:
            numbs.append(float(element))
        except ValueError:
            print("get_sum():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("get_sum():\t{} is not a number.".format(str(element)))
            return None

    return sum(numbs)


# endregion


# region Task #3
def get_next_and_previous(input_string=None):
    """Returns the previous, entered and next number.

    :param input_string:
        String to be processed.
    :return:
        Tuple. Previous, current, next.
    """
    if type(input_string) is not str:
        print("get_next_and_previous():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    try:
        number = int(input_string)
    except ValueError:
        print("get_next_and_previous():\t{} is not a number.".format(str(input_string)))
        return None
    except TypeError:
        print("get_next_and_previous():\t{} is not a number.".format(str(input_string)))
        return None

    return number - 1, number, number + 1


# endregion


# region Task #4
def get_square_side(input_string=None):
    """Returns the side of a square.

    :param input_string:
        String to be processed.
    :return:
        The side.
    """
    if type(input_string) is not str:
        print("get_square_side():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()

    try:
        number = float(input_string)
    except ValueError:
        print("get_square_side():\t{} is not a number.".format(str(input_string)))
        return None
    except TypeError:
        print("get_square_side():\t{} is not a number.".format(str(input_string)))
        return None

    if number < 0.0:
        print("get_square_side():\tPlease, enter positive number.")
        return None

    return math.sqrt(number)
# endregion


# region Task #5
def find_area_and_perimeter(input_string=None):
    """Get three sides of the triangle and returns its perimeter and area.

    :param input_string:
        String to be processed.
    :return:
        Tuple: Area, perimeter.
    """

    if type(input_string) is not str:
        print("find_area_and_perimeter():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    sides = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("find_area_and_perimeter():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("find_area_and_perimeter():\t{} is not a number.".format(str(element)))
            return None
        finally:
            sides.append(element_value)

    if len(sides) != 3:
        print("find_area_and_perimeter():\tPlease, enter THREE sides.")
        return None

    for side in sides:
        if side <= 0.0:
            print("find_area_and_perimeter():\tLength cannot be negative or zero.")
            return None

    perimeter = sum(sides)
    p = perimeter / 2.0

    triangle_exist = False
    if (sides[0] + sides[1]) > sides[2]:
        triangle_exist = True

    if not triangle_exist:
        print("find_area_and_perimeter():\tA triangle with such sides does not exist.")
        return None

    area = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

    factor = 10.0 ** 4

    return math.trunc(area * factor) / factor, math.trunc(perimeter * factor) / factor


# endregion


# region Task #6
def get_total_and_overpayment(input_string=None):
    """Get two nums from a string and returns total and overpayment.

    :param input_string:
        String to be processed.
    :return:
        Tuple: Total, overpayment.
    """

    if type(input_string) is not str:
        print("get_total_and_overpayment():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    nums = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("get_total_and_overpayment():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("get_total_and_overpayment():\t{} is not a number.".format(str(element)))
            return None
        finally:
            nums.append(element_value)

    if len(nums) != 2:
        print("get_total_and_overpayment():\tPlease, enter TWO nums.")
        return None

    total = nums[0] * (nums[1] / 100.0) + nums[0]
    overpayment = total - nums[0]

    return total, overpayment


# endregion


# region Task #7
def calc(input_string=None):
    if type(input_string) is not str:
        print("calc():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    operators = ("+", "-", "*", "/", "**", "//", "%")
    nums = []
    operator = ""
    operators_count = 0

    for element in separated_string:
        element_value = 0.0
        try:
            nums.append(float(element))
        except ValueError:
            operator = element
            operators_count += 1
        except TypeError:
            operator = element
            operators_count += 1

    if len(nums) > 2:
        print("calc():\tThere should be only TWO numbers.")
        return None

    if operators_count > 1:
        print("calc():\tThere should be only ONE operator.")
        return None

    if operator not in operators:
        print("calc():\tOperator should be from {}.".format(str(operators)))
        return None

    result = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0.0 else None,
        "**": lambda x, y: x ** y,
        "//": lambda x, y: x // y if y != 0.0 else None,
        "%": lambda x, y: x % y if y != 0.0 else None
    }[operator](nums[0], nums[1])

    if result is None:
        print("calc():\tDivision by zero is not allowed.")

    return result
# endregion


# region Task #8
def get_random_nums(input_string=None):
    """Get two nums from a string and returns two random nums from an interval, rational and whole.

    :param input_string:
        String to be processed.
    :return:
        Tuple: Rational, whole.
    """

    if type(input_string) is not str:
        print("get_random_nums():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    nums = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("get_random_nums():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("get_random_nums():\t{} is not a number.".format(str(element)))
            return None
        finally:
            nums.append(element_value)

    if len(nums) != 2:
        print("get_random_nums():\tPlease, enter TWO nums.")
        return None

    rational = random.uniform(nums[0], nums[1])
    whole = random.randint(int(nums[0]), int(nums[1]))

    return rational, whole


# endregion


# region Task #9
def get_smallest(input_string=None):
    """Get two nums from a string and returns smaller one.

    :param input_string:
        String to be processed.
    :return:
        Smallest number.
    """

    if type(input_string) is not str:
        print("get_smallest():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    nums = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("get_smallest():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("get_smallest():\t{} is not a number.".format(str(element)))
            return None
        finally:
            nums.append(element_value)

    if len(nums) != 2:
        print("get_smallest():\tPlease, enter TWO nums.")
        return None

    return min(nums)


# endregion


# region Task #10

# endregion


# region Task #11

# endregion


# region Task #12

# endregion


# region Task #13

# endregion


# region Task #14
def determine_vowel_consonant(input_string=None):
    """Defines letter is vowel or consonant.

    :param input_string:
        String to be processed.
    :return:
        True if vowel, False if consonant.
    """
    if type(input_string) is not str:
        print("determine_vowel_consonant():\tCan't handle this type of input.")
        return -1

    input_string = input_string.strip()

    if len(input_string) != 1:
        print("determine_vowel_consonant():\tPlease, enter only one letter.")
        return -1

    if not input_string.isalpha():
        print("determine_vowel_consonant():\tPlease, enter ONLY letters.")
        return -1

    is_vowel = False

    vowel_letters = ['e', 'u', 'i', 'o', 'a']

    if input_string in vowel_letters:
        is_vowel = True

    return is_vowel
# endregion


# region Task #15
def is_isosceles_or_equilateral(input_string=None):
    """Get three sides of the triangle and returns is it isosceles or equilateral.

    :param input_string:
        String to be processed.
    :return:
        String: Is isosceles, is equilateral in natural language.
    """

    if type(input_string) is not str:
        print("is_isosceles_or_equilateral():\tCan't handle this type of input.")
        return -1

    input_string = input_string.strip()
    separated_string = input_string.split()
    sides = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("is_isosceles_or_equilateral():\t{} is not a number.".format(str(element)))
            return -1
        except TypeError:
            print("is_isosceles_or_equilateral():\t{} is not a number.".format(str(element)))
            return -1
        finally:
            sides.append(element_value)

    if len(sides) != 3:
        print("is_isosceles_or_equilateral():\tPlease, enter THREE sides.")
        return -1

    for side in sides:
        if side <= 0.0:
            print("is_isosceles_or_equilateral():\tLength cannot be negative or zero.")
            return -1

    triangle_exist = False
    if (sides[0] + sides[1]) > sides[2]:
        triangle_exist = True

    if not triangle_exist:
        print("is_isosceles_or_equilateral():\tA triangle with such sides does not exist.")
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


# endregion


# region Task #16

# endregion

# region Select task
def get_task_to_run(input_string=None):
    """Returns the side of a square.

    :param input_string:
        String to be processed.
    :return:
        Integer: Number of the task.
    """
    if type(input_string) is not str:
        print("get_task_to_run():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()

    try:
        number = int(input_string)
    except ValueError:
        print("get_task_to_run():\t{} is not a number.".format(str(input_string)))
        return None
    except TypeError:
        print("get_task_to_run():\t{} is not a number.".format(str(input_string)))
        return None

    if number < 0 or number > 16:
        print("get_task_to_run():\tPlease, enter number between 1 and 16.")
        return None

    return number
# endregion


if __name__ == "__main__":
    #user_input = input("Please, enter task number to run:\n")
    print(str(calc("-2 // 5")) + " {}".format(str(-2//5)))
