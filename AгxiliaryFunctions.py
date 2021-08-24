"""Auxiliary function for Hillel Machine Learning course homeworks."""


import re


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"
__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def is_string(prefix: str, input_string: str):
    """The function checks if the input variable is a string."""
    try:
        if isinstance(input_string, str):
            return True
        else:
            print(prefix + "{} is not a string instance.".format(str(input_string)))
            return False
    except (Exception,):
        print(str(prefix) + "Error processing input data.")
        return False


def extract_numbers(prefix: str, input_string: str, skip_element_at_index: int):
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


def extract_tuples(prefix: str, input_string: str, separator_id=1):
    """The function returns a tuples from string."""

    regexp_enum = {
        1: r'\((.*?)\)',
        2: r'\[(.*?)\]',
        3: r'\{(.*?)\}'
    }

    if not is_string(prefix, input_string):
        print(str(prefix) + "\tThe input variable must be a string.")
        return None, input_string

    a = "r"
    tuples = re.findall(regexp_enum[separator_id], input_string)

    if tuples is None or len(tuples) == 0:
        print(str(prefix) + "There is no tuples.")
        return None, input_string

    input_wo_tuples = str(input_string)

    for t_index, current_t in enumerate(tuples):
        processed_t = re.findall(r"[-+]?\d*\.?\d+|\d+", current_t)

        if processed_t is None:
            print(str(prefix) + "\tCan't extract tuple from {}.".format(str(current_t)))
            return None, input_string

        input_wo_tuples = str.replace(input_wo_tuples, "(" + str(current_t) + ")", "")

        for e_index, num in enumerate(processed_t):
            try:
                processed_t[e_index] = float(num)

            except (TypeError, ValueError):
                return None, input_string

        tuples[t_index] = processed_t

    return tuples, input_wo_tuples


def get_task_to_run(input_string: str, input_range: tuple):
    """Returns the number of task to run."""
    if not is_string("get_task_to_run():", input_string):
        return None

    input_string = input_string.strip()

    try:
        number = int(input_string)
    except (ValueError, TypeError):
        print("get_task_to_run():\t{} is not a number.".format(str(input_string)))
        return None

    if number < min(input_range) or number > max(input_range):
        print("get_task_to_run():\tPlease, enter number between {} and {}.".format(
            str(min(input_range)),
            str(max(input_range))
        ))
        return None

    return int(number)


def print_time_relation(prefix: str, time_1: float, time_2: float):
    time_relation = 1.0
    result_string = prefix + " is {:.2f} times "

    if time_1 > time_2:
        result_string += "slower."
        time_relation = time_1 / time_2
    else:
        result_string += "faster."
        time_relation = time_2 / time_1

    print(result_string.format(time_relation))


if __name__ == "__main__":
    exit(0)
