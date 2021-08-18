"""Hillel Machine Learning course. Homework 03.
#1.     Write a program that reads a number, prints its square root and takes the next number.
        The program stops working when you enter a negative number.
#2.     The number of numbers to enter and the numbers themselves are given.
        Display the maximum among the entered numbers.
#3.     Given a "+" or "*" sign, the number of numbers and the numbers themselves.
        Display the sum or product of numbers depending on the entered sign.
#4.     Given a number N. Print first N numbers of the Fibanacci sequence.
#5.     Given a number N. Print a sequence of Fibonacci numbers less than N.
#6.     Write a program that builds a correspondence table between Celsius and Fahrenheit.
        The starting and ending values are given in degrees Celsius, step.
        Display the correspondence table.
#7.     The number N is given. After that, in the order of traversal, N pairs of coordinates of the polygon on the plane
        are entered. Find the perimeter of this polygon.
#8.     The number N is given and a list of N numbers. For each number from the list, output its ratio to the arithmetic
        mean of this list (less, greater, equal).
#9.     The number N is given and a list of N numbers.
        Print all numbers greater than both of their neighbors in the list.
#10.    The number N is given and a list of N numbers. Display the list in reverse order.
#11.    The number N is given and a list of N numbers.
        Further, pairs of numbers (A, B) greater than zero are given to the input. For each pair,
        print the values of the list with indices from A (inclusive) to B (not inclusive). Exit on entering two zeros.
        Consider the case when A>B.
#12.    The number N is given and a list of N numbers. Print all numbers that appear in the list only once.
#13.    The number N is given and a list of N numbers. The number M is given and a list of M numbers.
        Print all numbers that are in both lists.
#14.    Implement a CRM system that should accept and process the following types of requests:
            - add employee named <name> to the system (add);
            - check if there is an employee named <name> in the system (find);
            - list all employees (list);
            - remove employee named <name> from the system (delete);
            - shut down the system (stop).
#15.    Task from www.codewars.com
        https://www.codewars.com/kata/5263a84ffcadb968b6000513

"""

import math
import numpy as np
import re

# region Input and result strings definition
prompt_strings = {
    1: "\nEnter a number to calculate the square root.",
    2: "\nEnter a sequence of numbers.",
    3: "\nEnter the symbol of the mathematical operation and the sequence of numbers to which it should be applied.",
    4: "\nEnter the number of the number in the Fibanacci sequence.",
    5: "\nEnter the number.",
    6: "\nEnter the start and end of the range, step.",
    8: "\nEnter a sequence of numbers.",
    9: "\nEnter a sequence of numbers.",
    10: "\nEnter a sequence of numbers.",
    12: "\nEnter a sequence of numbers."
}

result_strings = {
    1: "The square root of the entered number is {}.",
    2: "The maximum in the sequence is the number {}.",
    3: "The result of a mathematical operation on all elements of the sequence is {}.",
    4: "Fibonacci sequence up to specified number is {}.",
    5: "Elements of the Fibanacci sequence less than the specified number are {}.",
    6: "Table of correspondence:\n",
    8: "Numbers refer to the arithmetic mean as follows.",
    9: "The numbers greater than the neighbors in the list:\n {}",
    10: "Sequence in reverse order: {}.",
    12: "Numbers that appears only once in a sequence:\n{}.",
    13: "Numbers that appears in bots sequences is:\n{}"
}


# endregion

# region Auxiliary functions
def convert_to_fahrenheit(input_temp=0.0):
    """The function returns tuple (input_temp, input_temp -> F)."""
    return round(input_temp, 2), round((input_temp * 9.0 / 5.0) + 32.0, 2)


def is_string(prefix, input_string=None):
    """The function checks if the input variable is a string."""
    try:
        if isinstance(input_string, str):
            return True
        else:
            print(str(prefix) + "Error processing input data.")
            return False
    except (Exception,):
        print(str(prefix) + "Error processing input data.")
        return False


def extract_numbers(prefix, input_string=None, skip_element_at_index=None):
    """The function converts a string to a list of numbers."""
    if not is_string(prefix, input_string):
        print(str(prefix) + "\tThe input variable must be a string.")
        return None

    list_of_numbers = []

    for index, sub_string in enumerate(input_string.strip().split()):
        try:
            if skip_element_at_index is not None:
                if index != skip_element_at_index:
                    list_of_numbers.append(float(sub_string))
            else:
                list_of_numbers.append(float(sub_string))
        except (ValueError, TypeError):
            print(str(prefix) + "\tCan't convert {} to number.".format(str(sub_string)))

    if len(list_of_numbers) == 0:
        print(str(prefix) + "\tThere is no numbers in the input line.")
        return None

    return list_of_numbers


def extract_tuples(prefix, input_string=None):
    """The function returns a tuples from string."""

    if not is_string(prefix, input_string):
        print(str(prefix) + "\tThe input variable must be a string.")
        return None

    tuples = re.findall(r'\((.*?)\)', input_string)

    for t_index, current_t in enumerate(tuples):
        current_t = re.findall(r"[-+]?\d*\.?\d+|\d+", current_t)

        if current_t is None:
            print("extract_tuples()\tCan't extract tuple from {}.".format(str(current_t)))
            return None

        for e_index, num in enumerate(current_t):
            try:
                current_t[e_index] = float(num)

            except (TypeError, ValueError):
                return

        tuples[t_index] = current_t

    print(tuples)

    return None


def get_task_to_run(input_string=None):
    """Returns the number of task to run."""
    if not is_string("get_task_to_run():", input_string):
        return None

    input_string = input_string.strip()

    try:
        number = int(input_string)
    except (ValueError, TypeError):
        print("get_task_to_run():\t{} is not a number.".format(str(input_string)))
        return None

    if number < 0 or number > 15:
        print("get_task_to_run():\tPlease, enter number between 1 and 15.")
        return None

    return int(number)


# endregion

# region Task #1
def get_square_root(input_string=None):
    """The function returns the square root of the entered number."""
    nums = extract_numbers("get_square_root():", input_string)
    if nums is None:
        return None

    if len(nums) != 1:
        print("get_square_root():\tPlease enter only ONE number.")
        return None

    if nums[0] < 0.0:
        print("get_square_root():\tPlease enter only POSITIVE number.")
        return None

    return round(math.sqrt(nums[0]), 3)


# endregion
# region Task 02
def max_in_sequence(input_string=None):
    """The function returns the maximum number entered."""
    nums = extract_numbers("max_in_sequence():", input_string)
    if nums is None:
        return None

    return max(nums)


# endregion


# region Task 03
def apply_math_to_list(input_string=None):
    """The function returns the sum or product of all the elements in the list."""
    if not is_string("apply_math_to_list():", input_string):
        return None

    nums = extract_numbers("apply_math_to_list():", input_string, 0)

    if nums is None:
        return None

    if len(nums) < 2:
        print("apply_math_to_list():\tThere should be at least TWO numbers.")
        return None

    operators = ("+", "*")

    operator = input_string.strip().split()[0]

    if operator not in operators:
        print("apply_math_to_list():\t Valid operators is {}.".format(str(operators)))
        return None

    if operator == "+":
        return round(sum(nums), 3)
    elif operator == "*":
        return round(math.prod(nums), 3)
    else:
        return None


# endregion


# region Task 04
def get_n_fibonacci_sequence(input_string=None, at_index=False):
    """The function returns the first N numbers of the Fibonacci sequence. Or number at index N."""

    if not is_string("get_n_fibonacci_sequence():", input_string):
        return None

    nums = extract_numbers("get_n_fibonacci_sequence()\t", input_string)
    if nums is None:
        return None

    if len(nums) != 1:
        print("get_n_fibonacci_sequence():\tPlease enter only ONE number.")
        return None

    if int(nums[0]) <= 0:
        print("get_n_fibonacci_sequence():\tN should be positive and nonzero.")
        return None

    f_matrix = np.matrix([[1, 1], [1, 0]])

    f_sequence = []

    if not at_index:
        for index in range(1, int(nums[0]) + 1):
            f_sequence.append((f_matrix ** (index - 1))[0, 0])
    else:
        f_sequence = (f_matrix ** (int(nums[0]) - 1))[0, 0]

    return f_sequence


# endregion

# region Task 05
def get_fibonacci_sequence_to_n(input_string=None):
    """The function returns a Fibonacci sequence less than a given number."""
    if not is_string("get_fibonacci_sequence_to_n():", input_string):
        return None

    nums = extract_numbers("get_fibonacci_sequence_to_n()\t", input_string)
    if nums is None:
        return None

    if int(nums[0]) <= 1:
        return None

    if len(nums) != 1:
        print("get_fibonacci_sequence_to_n():\tPlease enter only ONE number.")
        return None

    f_sequence = []
    f_number = 1
    index = 1
    while f_number < int(nums[0]):
        f_sequence.append(f_number)
        index += 1
        f_number = get_n_fibonacci_sequence(input_string=str(index), at_index=True)
        if f_number is None:
            break

    return f_sequence


# endregion


# region Task 06
def get_cel_fahr_cor_table(input_string=None):
    """The function returns temperature pairs. Celsius and corresponding Fahrenheit."""
    if not is_string("get_cel_fahr_cor_table():", input_string):
        return None

    nums = extract_numbers("get_cel_fahr_cor_table()\t", input_string)
    if nums is None:
        return None

    if len(nums) != 3:
        print("get_cel_fahr_cor_table():\tPlease enter THREE numbers.")
        return None

    start_temp = min(nums[0:2])
    end_temp = max(nums[0:2])
    step = math.fabs(nums[2])

    current_temp = start_temp
    correspondence = list()
    correspondence.append(convert_to_fahrenheit(start_temp))

    while current_temp < end_temp - step:
        current_temp += step
        correspondence.append(convert_to_fahrenheit(current_temp))

    correspondence.append(convert_to_fahrenheit(end_temp))
    return correspondence


# endregion


# region Task 08
def get_ratio(input_string):
    """The function determines the ratio of each number in the list to its arithmetic mean."""
    if not is_string("get_ratio():", input_string):
        return None

    nums = extract_numbers("get_ratio()\t", input_string)
    if nums is None or len(nums) == 0:
        return None

    a_mean = sum(nums) / len(nums)

    ratio = list()

    for num in nums:
        if num > a_mean:
            ratio.append((num, "greater than", a_mean))
        elif num < a_mean:
            ratio.append((num, "less than", a_mean))
        else:
            ratio.append((num, "equal to", a_mean))

    ratio.sort(key=lambda x: (x[1], x[0]))
    return ratio


# endregion


# region Task 09
def greater_than_neighbors(input_string=None):
    """The function returns numbers greater than their neighbors."""
    if not is_string("greater_than_neighbors():", input_string):
        return None

    nums = extract_numbers("greater_than_neighbors()\t", input_string)
    if nums is None or len(nums) == 0:
        return None

    greater_nums = list()
    for index, num in enumerate(nums[1:-1]):
        index += 1
        if num > nums[index - 1] and num > nums[index + 1]:
            greater_nums.append(num)

    if len(greater_nums) != 0:
        return greater_nums
    else:
        return "There is no such numbers in the given sequence."


# endregion


# region Task 10
def reverse_list(input_string=None):
    """The function returns given sequence in reverse order"""

    if not is_string("reverse_list():", input_string):
        return None

    nums = extract_numbers("reverse_list()\t", input_string)
    if nums is None or len(nums) == 0:
        return None

    return nums[::-1]


# endregion


# region Task 12
def get_unique_numbers(input_string=None):
    """The function returns numbers that appears ony once in a sequence."""

    if not is_string("get_unique_numbers():", input_string):
        return None

    nums = extract_numbers("get_unique_numbers()\t", input_string)
    if nums is None or len(nums) == 0:
        return None

    one_instance_nums = list(set(nums))
    unique_nums = list()

    for num in one_instance_nums:
        if nums.count(num) == 1:
            unique_nums.append(num)

    if len(unique_nums) > 0:
        return unique_nums
    else:
        return "There is no unique elements in the sequence."


# endregion


# region Task 13
def get_numbers_in_two_sequences(num_sequences=None):
    """The function returns numbers that present in both sequences."""

    nums_list = list()
    for sequence in num_sequences:
        if not is_string("get_numbers_in_two_sequences()\t", sequence):
            return None
        else:
            current_s = extract_numbers("get_numbers_in_two_sequences()\t", sequence)
            if current_s is None or len(current_s) == 0:
                return None
            else:
                nums_list.append(current_s)

    if len(nums_list) != 2:
        print("get_numbers_in_two_sequences():\t There should be TWO sequence of numbers.")

    nums_in_both_lists = list()

    for num in nums_list[0]:
        if num in nums_list[1]:
            nums_in_both_lists.append(num)

    nums_in_both_lists = list(set(nums_in_both_lists))

    if len(nums_in_both_lists) > 0:
        return nums_in_both_lists
    else:
        return "The entered sequences do not contain the same elements."


# endregion


# region Functions dictionary definition
functions = {
    1: get_square_root,
    2: max_in_sequence,
    3: apply_math_to_list,
    4: get_n_fibonacci_sequence,
    5: get_fibonacci_sequence_to_n,
    6: get_cel_fahr_cor_table,
    8: get_ratio,
    9: greater_than_neighbors,
    10: reverse_list,
    12: get_unique_numbers,
    13: get_numbers_in_two_sequences
}
# endregion


# region __main__
if __name__ == "__main__":
    extract_tuples("extract_tuples():\t", "1 2 3 4 (4 4) (6.54, 4.3)")
    while True:
        user_input = input("\nPlease enter task number to run or 'q' to exit:\n")
        if user_input.lower().strip() == "q":
            break

        print("Please, note that all values are entered on one line and separated by a space.\n"
              + "('q' to return to the task selection).\n")

        task_to_run = get_task_to_run(user_input)
        if task_to_run is None:
            continue

        while True:
            result = None
            same_input_scheme = (1, 2, 3, 4, 5, 6, 9, 10, 12)
            try:
                if task_to_run in same_input_scheme:
                    user_input = input(prompt_strings[task_to_run] + " ('q' to return to the task selection):\n")
                elif task_to_run == 13:
                    sequences = list()

                    user_input = input("Enter first sequence of numbers:\n")
                    if user_input.lower().strip() == "q":
                        break
                    else:
                        sequences.append(user_input)

                    user_input = input("Enter second sequence of numbers:\n")
                    if user_input.lower().strip() == "q":
                        break
                    else:
                        sequences.append(user_input)

                    result = get_numbers_in_two_sequences(sequences)
            except (Exception,):
                print("Main:\tCan't run specified task.")
                break

            if user_input.lower().strip() == "q":
                break

            try:
                if task_to_run in same_input_scheme:
                    result = functions[task_to_run](user_input)
            except (Exception,):
                print("Main:\tCan't run specified task.")
                continue

            if result is None:
                continue

            same_output_scheme = (1, 2, 3, 4, 5, 6, 9, 10, 12, 13)

            if task_to_run in same_output_scheme:
                print(result_strings[task_to_run].format(str(result)))
            elif task_to_run == 6:
                print(result_strings[task_to_run].format(str(result)))
                for element in result:
                    print("{}C\tcorresponds to\t{}F".format(str(element[0]), str(element[1])))
            elif task_to_run == 8:
                print(result_strings[task_to_run].format(str(result)))
                for element in result:
                    print("{}\tis {}\t{}.".format(element[0], element[1], element[2]))

# endregion
