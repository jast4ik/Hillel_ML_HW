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
#10.    Implement the function sign(x)
#11.    Same as #7
#12.    Coefficients a b c of the quadratic equation (ax^2 + bx + c = 0) are given. Find the roots of the equation.
#13.    The mobile communication package provides for 100 minutes and 30 SMS per month with a fixed monthly
        fee of UAH 30. Further, calls are charged at UAH 0.3 per minute, and SMS at UAH 0.25.
        The number of minutes and SMS used per month is given.
        Calculate the cost of the services provided.
#14.    One letter is given. Determine whether it is a vowel or a consonant.
#15.    Three sides of the triangle are given. Determine if a triangle is isosceles or equilateral.
#16.    Task from www.codewars.com
        https://www.codewars.com/kata/56684677dc75e3de2500002b
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
        print("get_hello_string():\tCan't handle this type of input.")
        return None

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
def calc(input_string=None, get_operators=False):
    """Simple calculator.

    :param input_string:
        String to be processed.
    :param get_operators
        If True, returns a string with allowed operators.
    :return:
        Float. Result of calculator work.
    """
    if type(input_string) is not str:
        print("calc():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    operators = ("+", "-", "*", "/", "**", "//", "%")
    nums = []
    operator = ""
    operators_count = 0

    if get_operators:
        operators_string = ""
        for item in operators:
            operators_string += " {}".format(item)
        return operators_string

    for element in separated_string:
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
def sign(input_string=None):
    """ Returns sign(x) (also known as sng(x)).

    :param input_string:
        String to be processed.
    :return:
        Integer: sign(x).
    """

    if type(input_string) is not str:
        print("sign():\tCan't handle this type of input.")
        return None

    try:
        number = float(input_string)
    except TypeError:
        print("sign():\tInput isn't number.")
        return None
    except ValueError:
        print("sign():\tInput isn't number.")
        return None

    if number > 0:
        result = 1
    elif number < 0:
        result = -1
    else:
        result = 0

    return result


# endregion


# region Task #11
# See task #7.
# endregion


# region Task #12
def get_roots(input_string=None):
    """ Returns roots of the quadratic equation.

    :param input_string:
        String to be processed.
    :return:
        Tuple: roots
    """
    if type(input_string) is not str:
        print("get_roots():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    coefficients = []

    for element in separated_string:
        try:
            coefficients.append(float(element))
        except ValueError:
            print("get_roots():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("get_roots():\t{} is not a number.".format(str(element)))
            return None

    if len(coefficients) != 3:
        print("get_roots():\tPlease, enter THREE coefficients.")
        return None

    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]

    d = b ** 2.0 - 4.0 * a * c

    if d < 0.0:
        print(print("get_roots():\tThe equation does not have real roots."))
        return None

    roots = [
        (-1 * b - math.sqrt(b ** 2 - 4.0 * a * c)) / (2.0 * a),
        (-1 * b + math.sqrt(b ** 2 - 4.0 * a * c)) / (2.0 * a)
    ]

    return roots


# endregion


# region Task #13
def get_cost_of_service(input_string=None):
    """ Returns total cost of services provided.

    :param input_string:
        String to be processed.
    :return:
        Float: Total cost of services provided.
    """

    if type(input_string) is not str:
        print("cost_of_service():\tCan't handle this type of input.")
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    nums = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("cost_of_service():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("cost_of_service():\t{} is not a number.".format(str(element)))
            return None
        finally:
            nums.append(element_value)

    if len(nums) != 2:
        print("cost_of_service():\tPlease, enter TWO numbers.")
        return None

    result = 30.0
    if nums[0] > 100.0:
        result += (nums[0] - 100.0) * 0.3

    if nums[1] > 30.0:
        result += (nums[1] - 30.0) * 0.25

    return result


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
        return None

    input_string = input_string.strip()

    if len(input_string) != 1:
        print("determine_vowel_consonant():\tPlease, enter only one letter.")
        return None

    if not input_string.isalpha():
        print("determine_vowel_consonant():\tPlease, enter ONLY letters.")
        return None

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
        return None

    input_string = input_string.strip()
    separated_string = input_string.split()
    sides = []

    for element in separated_string:
        element_value = 0.0
        try:
            element_value = float(element)
        except ValueError:
            print("is_isosceles_or_equilateral():\t{} is not a number.".format(str(element)))
            return None
        except TypeError:
            print("is_isosceles_or_equilateral():\t{} is not a number.".format(str(element)))
            return None
        finally:
            sides.append(element_value)

    if len(sides) != 3:
        print("is_isosceles_or_equilateral():\tPlease, enter THREE sides.")
        return None

    for side in sides:
        if side <= 0.0:
            print("is_isosceles_or_equilateral():\tLength cannot be negative or zero.")
            return None

    triangle_exist = False
    if (sides[0] + sides[1]) > sides[2]:
        triangle_exist = True

    if not triangle_exist:
        print("is_isosceles_or_equilateral():\tA triangle with such sides does not exist.")
        return None

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
def define_if_word_comfortable(input_string=None):
    """Defines if entered word is comfortable for QWERTY printing.

    :param input_string:
        String to be processed.
    :return:
        Boolean: Is or not comfortable.
    """
    if type(input_string) is not str:
        print("define_if_word_comfortable():\tCan't handle this type of input.")
        return None

    left_hand_letters = ("q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b")
    work_string = input_string.strip()

    regex = re.compile("[^a-zA-Z]")
    work_string = regex.sub("", work_string)
    work_string = work_string.lower()

    hand_change = [True] * len(work_string)
    for index, char in enumerate(work_string):
        if char in left_hand_letters:
            hand_change[index] = True
        else:
            hand_change[index] = False

    is_comfortable = True
    for index, item in enumerate(hand_change[:-1]):
        if item is hand_change[index + 1]:
            is_comfortable = False
            break

    return is_comfortable


# endregion


# region Select task
def get_task_to_run(input_string=None):
    """Returns the number of task to run.

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

    return int(number)


# endregion


prompts = {
    1: "Please, enter your name:\n",
    2: "Please, enter set of numbers to calculate their sum:\n",
    3: "Please, enter the number (integer):\n",
    4: "Please, enter the area of the square:\n",
    5: "Please, enter three sides of the triangle:\n",
    6: "Please, enter two numbers.\n"
       + "First one is total loan, second is one-time interest:\n",
    7: "Please enter simple math equation:\n",
    8: "Please, enter two borders of the interval:\n",
    9: "Please, enter two numbers to define smallest:\n",
    10: "Please, enter the number to calculate sign(x):\n",
    11: "Please enter simple math equation:\n",
    12: "Please, enter three coefficients of quadratic equation (a, b, c):\n",
    13: "Please, enter minutes and SMS used (separated by space):\n",
    14: "Please, enter the char to define is it vowel or consonant:\n",
    15: "Please, enter three sides of the triangle:\n",
    16: "Please, enter the word:"
}
functions = {
    1: get_hello_string,
    2: get_sum,
    3: get_next_and_previous,
    4: get_square_side,
    5: find_area_and_perimeter,
    6: get_total_and_overpayment,
    7: calc,
    8: get_random_nums,
    9: get_smallest,
    10: sign,
    11: calc,
    12: get_roots,
    13: get_cost_of_service,
    14: determine_vowel_consonant,
    15: is_isosceles_or_equilateral,
    16: define_if_word_comfortable
}


if __name__ == "__main__":
    while True:
        user_input = input("\nPlease, enter task number to run, or 'q' to exit:\n")
        if user_input.lower().strip() == "q":
            break

        print("\nPlease, note that all values are entered on one line and separated by a space.\n"
              + "To return to task selection enter 'q'\n")

        task_to_run = get_task_to_run(user_input)
        if task_to_run is None:
            continue

        while True:
            user_input = input(prompts[task_to_run])
            if user_input.lower().strip() == "q":
                break

            result = functions[task_to_run](user_input)
            if result is None:
                continue

            if task_to_run == 1:
                print(result)
            elif task_to_run == 2:
                print("Sum of numbers is {}.\n".format(str(result)))
            elif task_to_run == 3:
                print("Next for number {} is {} and previous is {}.\n".format(result[1], result[2], result[0]))
            elif task_to_run == 4:
                print("Side of the square is {:.2f}\n".format(result))
            elif task_to_run == 5:
                print("Area of the triangle is {:.2f} and perimeter is {:.2f}.\n".format(result[0], result[1]))
            elif task_to_run == 6:
                print("Total payment is ${:.2f} and overpayment is {:.2f}.\n".format(result[0], result[1]))
            elif task_to_run == 7:
                print("Result is {}.\n".format(result))
            elif task_to_run == 8:
                print("Random rational is {:.5f} and whole is {}.\n".format(result[0], result[1]))
            elif task_to_run == 9:
                print("Smallest number is {}.\n".format(str(result)))
            elif task_to_run == 10:
                print("sign(x) is {}.\n".format(str(result)))
            elif task_to_run == 11:
                print("Result is {}.\n".format(result))
            elif task_to_run == 12:
                print("Roots of the equation is {:.4f} and {:.4f}".format(result[0], result[1]))
            elif task_to_run == 13:
                print("Total payment is ${:.2f}.\n".format(result))
            elif task_to_run == 14:
                if result:
                    print("Letter is vowel.\n")
                else:
                    print("Letter is consonant.\n")
            elif task_to_run == 15:
                print(result)
            elif task_to_run == 16:
                if result:
                    print("Word is comfortable.\n")
                else:
                    print("Word is not comfortable.\n")
