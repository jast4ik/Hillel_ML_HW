"""Hillel Machine Learning course. Homework 03.
#1. Write a program that reads a number, prints its square root and takes the next number.
    The program stops working when you enter a negative number.
#2. The number of numbers to enter and the numbers themselves are given. Display the maximum among the entered numbers.
#3. Given a "+" or "*" sign, the number of numbers and the numbers themselves.
    Display yhe sum or product of numbers depending on the entered sign.
#4. Given a number N. Print first N numbers of the Fibanacci sequence.
#5. Given a number N. Print a sequence of Fibonacci numbers less than N.
#6. Write a program that builds a correspondence table between Celsius and Fahrenheit.
    The starting and ending values are given in degrees Celsius, step.
    Display the correspondence table.
#7. The number N is given. After that, in the order of traversal, N pairs of coordinates of the polygon on the plane
    are entered. Find the perimeter of this polygon.
#8. The number N is given and a list of N numbers. For each number from the list, output its ratio to the arithmetic
    mean of this list (less, more, equal).
#9. The number N is given and a list of N numbers. Print all numbers greater than both of their neighbors in the list.
#10.The number N is given and a list of N numbers. Display the list in reverse order.
#11.The number N is given and a list of N numbers. Further, pairs of numbers (A, B) greater than zero are given to the
    input. For each pair, print the values of the list with indices from A (inclusive) to B (not inclusive). Exit on
    entering two zeros. Consider the case when A>B.
#12.The number N is given and a list of N numbers. Print all numbers that appear in the list only once.
#13.The number N is given and a list of N numbers. The number M is given and a list of M numbers.
    Print all numbers that are in both lists.
#14.
"""


# region Check input for string
def is_string(prefix, input_string=None):
    """
    The function checks if the input variable is a string.
    :param prefix:
        The prefix for the error message string.
    :param input_string:
        Variable to check.
    :return:
        True if variable is a string. False if not.
    """
    try:
        if isinstance(input_string, str):
            return True
        else:
            return False
    except Exception:
        print(str(prefix) + "Error processing input data.")
        return False


# endregion


# region String processing
def process_string(input_string=None):
    """
    The function converts a string to a list of numbers.
    :param input_string:
        String to be processed.
    :return:
        List of numbers.
    """
    list_of_strings = input_string.stip().split()
    list_of_numbers = []

    for element in list_of_strings:
        if element.isnumeric():
            list_of_numbers.append(float(element))

    return list_of_numbers


# endregion

# region Task #1
def get_square_root(prefix, input_string=None):
    if not is_string(input_string):
        print(str(prefix), "The input variable must be a string.")
        return None

# endregion
