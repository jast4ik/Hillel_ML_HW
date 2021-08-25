"""Hillel Machine Learning course. Homework 04."""

import AгxiliaryFunctions as af
import numpy as np
import time
import gc

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"
__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


# region Task 01
def get_col_sum(dimension: tuple, value: float, benchmark_mode=True):
    """The function returns sum by column in two dimensional array"""

    print("Creating Python list...")
    start_time = time.time()

    python_list = af.create_list(dimension, value)

    python_creation_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_creation_time))

    if python_list is None:
        return None

    col_sums = {}

    print("\nCalculating sum of Python list with for loop...")
    start_time = time.time()

    for row in python_list:
        for col_index, col_element in enumerate(row):
            if col_index not in col_sums:
                col_sums[col_index] = col_element
            else:
                col_sums[col_index] += col_element

    python_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_time))

    print("\nCreating NumPy array...")
    start_time = time.time()

    numpy_array = np.full(dimension, value, dtype=float)

    numpy_creation_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_creation_time))

    print("\nCalculating sum of NumPy array with numpy.sum()...")
    start_time = time.time()

    col_sums = np.sum(numpy_array, axis=0)

    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))

    af.print_time_relation("\nNumPy array creation", numpy_creation_time, python_creation_time)
    af.print_time_relation("NumPy np.sum()", numpy_time, python_time)

    print("\nCleaning up memory...")
    del numpy_array
    del python_list

    if benchmark_mode:
        del col_sums

    gc.collect()

    if benchmark_mode:
        return None
    else:
        return col_sums

# endregion


# region Task 02
def get_identity_matrix(size: int, benchmark_mode=True):
    """The function returns identity matrix."""

    print("Creating identity matrix using Python list...")

    start_time = time.time()

    python_matrix = af.create_list((size, size), 0.0)
    if python_matrix is None:
        return

    for row_index, row in enumerate(python_matrix):
        for col_index, col in enumerate(python_matrix):
            if row_index == col_index:
                python_matrix[row_index][col_index] = 1.0
                continue

    python_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_time))

    print("\nCreating identity matrix using NumPy array...")
    start_time = time.time()

    numpy_matrix = np.identity(size)

    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))

    af.print_time_relation("\nNumPy identity", numpy_time, python_time)

    if benchmark_mode:
        del numpy_matrix
        del python_matrix
        print("\nCleaning up memory...")
        gc.collect()
        return None

    del python_matrix
    print("\nCleaning up memory...")
    gc.collect()

    return numpy_matrix
# endregion


# region Task 03
def get_transposed_matrix(dimension: tuple, benchmark_mode=True):
    """The function returns transposed array."""

    print("Transposing array using Python for...")
    start_time = time.time()

    python_array = af.create_list(dimension, -1, True)
    transposed_array = [[python_array[j][i] for j in range(len(python_array))] for i in range(len(python_array[0]))]

    python_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_time))

    print("\nTransposing array using numpy.transpose()...")
    start_time = time.time()

    numpy_array = np.array(python_array)
    numpy_transposed_array = np.transpose(numpy_array)

    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))

    af.print_time_relation("\nNumPy transpose", numpy_time, python_time)

    if not benchmark_mode:
        print("---Original---")
        af.print_list(python_array)
        print("---Python---")
        af.print_list(transposed_array)
        print("---Numpy----")
        np.set_printoptions(precision=2)
        print(numpy_transposed_array)

    del numpy_array
    del python_array
    del transposed_array

    if benchmark_mode:
        del numpy_transposed_array

    print("\nCleaning up memory...")
    gc.collect()

    if benchmark_mode:
        return False
    else:
        return numpy_transposed_array


# endregion


# region Task 04
def calculate_word_instances(input_string: str):
    """The function calculates number of instances of each word in the given string."""

    if not af.is_string("calculate_word_instances():", input_string):
        return None

    word_count = dict()

    for word in input_string.strip().split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    print("The given string:\n{}\n".format(input_string))

    for word in word_count:
        if word_count[word] > 1:
            print("{} has {} instances.".format(word, word_count[word]))
        else:
            print("{} has {} instance.".format(word, word_count[word]))


# endregion


# region Task 05
def get_unique_numbers_count(input_list: list, benchmark_mode=True):
    """The function returns number of unique values in list."""

    print("\nCounting unique numbers using Python...")
    start_time = time.time()

    python_unique = set(input_list)

    python_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_time))

    print("\nCounting unique numbers using Numpy...")
    start_time = time.time()

    numpy_unique = np.unique(input_list)

    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))

    af.print_time_relation("\nNumPy", numpy_time, python_time)

    if not benchmark_mode:
        print("\nThe given list is:\n{}\nNumber of unique elements is {}:\n{}.".format(
            input_list,
            len(numpy_unique),
            numpy_unique
        ))

    if benchmark_mode:
        return None
    else:
        return numpy_unique

# endregion


# region Task 08
def process_dict(input_dict: dict):
    """The function makes some very weird things..."""

    print("input = {")
    for key in input_dict:
        temp_str = "{}:".format(key)
        for value in input_dict[key]:
            temp_str += " {} ".format(value)
        print(temp_str)
    print("}\n")

    sorted_dict = dict()
    # Sorting key in min->max order
    sorted_keys = sorted(input_dict, key=lambda x: int(x))

    # Removing duplicate values from each list in dictionary. First appearance is kept.
    for key in sorted_keys:
        for c_value in input_dict[key]:
            # get indexes of not unique list elements
            e_indexes = [i for i in range(len(input_dict[key])) if input_dict[key][i] == c_value]

            if len(e_indexes) > 1:
                # removing elements in reverse order to prevent "out of range" error.
                for index in sorted(e_indexes)[-1:0:-1]:
                    del input_dict[key][index]

            # creating dictionary sorted by key. Without duplicates in value list.
            sorted_dict[key] = input_dict[key]

    # s_index - straight index from last to second
    for s_index in range(len(sorted_keys) - 1, 0, -1):
        s_index -= len(sorted_keys)
        # r_index - reverse index from 0 to m_index - 1
        for s_value in sorted_dict[sorted_keys[s_index]]:
            for r_index in range(0, s_index + len(sorted_keys)):
                for index, r_value in enumerate(sorted_dict[sorted_keys[r_index]]):
                    if s_value == r_value:
                        del sorted_dict[sorted_keys[r_index]][index]

    print("output = {")
    for key in sorted_dict:
        temp_str = "{}:".format(key)
        for value in sorted_dict[key]:
            temp_str += " {} ".format(value)
        print(temp_str)
    print("}\n")

    return sorted_dict
# endregion


if __name__ == "__main__":
    # region 01 run
    print("=======================Task 01=======================")
    print("\n----------10x10 matrix----------")
    print(get_col_sum((10, 10), 2, False))
    print("\n----------100x100 matrix----------")
    get_col_sum((100, 100), 2)
    print("\n----------1000x1000 matrix----------")
    get_col_sum((1000, 1000), 2)
    # endregion

    # region 02 run
    print("\n=======================Task 02=======================")
    print("\n----------10x10 matrix----------")
    print(get_identity_matrix(10, False))
    print("\n----------100x100 matrix----------")
    get_identity_matrix(100)
    print("\n----------1000x1000 matrix----------")
    get_identity_matrix(1000)
    # endregion

    # region 03 run
    print("\n=======================Task 03=======================")
    print("\n----------2x3 matrix----------")
    get_transposed_matrix((2, 3), False)
    print("\n----------20x30 matrix----------")
    get_transposed_matrix((20, 30))
    print("\n----------200x300 matrix----------")
    get_transposed_matrix((200, 300))
    # endregion

    # region 04 run
    print("\n=======================Task 04=======================")
    calculate_word_instances("asd asd fgh jkll rew rew asdfg")
    # endregion

    # region 05 run
    print("\n=======================Task 05=======================")
    print("\n----------10 elements----------")
    get_unique_numbers_count([1, 2, 55, 6, 77, 3, 3, 2, 5, 6], False)
    print("\n----------100 elements----------")
    test_list = np.random.rand(1, 100).tolist()
    get_unique_numbers_count(test_list[0])
    print("\n----------1000 elements----------")
    test_list = np.random.rand(1, 1000).tolist()
    get_unique_numbers_count(test_list[0])
    print("\n----------10000 elements----------")
    test_list = np.random.rand(1, 10000).tolist()
    get_unique_numbers_count(test_list[0])
    print("\n----------100000 elements----------")
    test_list = np.random.rand(1, 100000).tolist()
    get_unique_numbers_count(test_list[0])
    print("\n----------1000000 elements----------")
    test_list = np.random.rand(1, 1000000).tolist()
    get_unique_numbers_count(test_list[0])
    # endregion

    # region 06 run
    print("\n=======================Task 06=======================")
    print("Enter 'q' to stop.")
    entered_numbers = list()
    while True:
        user_input = input("Enter a number: ")
        user_input = user_input.strip().lower()

        if user_input == 'q':
            break

        entered_number = None
        try:
            entered_number = round(float(user_input), 2)
        except (Exception, ):
            continue

        if entered_number not in entered_numbers:
            entered_numbers.append(entered_number)
        else:
            print("{} was entered before.".format(entered_number))
    # endregion

    # region 07 run
    print("\n=======================Task 07=======================")
    print("Enter 'q' to stop.")
    commands = ["insert", "delete", "get"]

    database = dict()

    while True:
        user_input = input("Enter a command:")

        if user_input.strip().lower() == 'q':
            break

        for command in commands:
            if command in user_input.strip().lower():
                processed_input = user_input.strip().replace(command, "")
                processed_input = processed_input.split()
                name = str()

                if command == "insert":
                    for word_index, word in enumerate(processed_input):
                        if not word.isdigit():
                            name = word
                            processed_input.pop(word_index)
                            break
                    if name not in database:
                        database[name] = processed_input[0]
                    break
                elif command == "delete":
                    if processed_input[0] in database:
                        del database[processed_input[0]]
                    else:
                        print("There is no name {} in database.".format(processed_input[0]))

                    break
                elif command == "get":
                    if processed_input[0] in database:
                        print(database[processed_input[0]])
                    else:
                        print("There is no name {} in database.".format(processed_input[0]))

                    break

        print(database)
    # endregion
    # region 08 run
    print("\n=======================Task 08=======================")
    in_dict = {
        "432": ["A", "A", "B", "D", "A"],
        "53": ["L", "G", "B", "C"],
        "236": ["L", "A", "X", "G", "X", "H", "X"],
        "11": ["P", "R", "S", "D"]
    }

    process_dict(in_dict)
    # endregion


