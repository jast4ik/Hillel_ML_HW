"""Hillel Machine Learning course. Homework 04."""

import AгxiliaryFunctions as af
import numpy as np
import time

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"
__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


# region Task01
def get_col_sum(input_string: str, separator_id=1):

    if not af.is_string("get_col_sum():\t", input_string):
        return None

    input_data = af.extract_tuples("get_col_sum():\t", input_string, separator_id)[0]
    if input_data is None:
        return None

    for row_index, row in enumerate(input_data[0:-2:1]):
        if len(row) != len(input_data[row_index + 2]):
            return None

    col_sums = {}

    print("\nSolution using Python list...")
    start_time = time.time()

    for row in input_data:
        for col_index, col_element in enumerate(row):
            if col_index not in col_sums:
                col_sums[col_index] = col_element
            else:
                col_sums[col_index] += col_element

    python_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_time))

    numpy_array = np.array(input_data)
    print("Solution using NumPy numpy.sum()...")
    start_time = time.time()
    sums = np.sum(numpy_array, axis=0)
    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))
    af.print_time_relation("NumPy np.sum()", numpy_time, python_time)

    return sums

# endregion


if __name__ == "__main__":

    print("Task 01...")
    print("\n----------10x10 matrix----------")
    a = np.full((30, 30), 4)
    print(get_col_sum(np.array2string(a), 2))
    print("\n----------100x100 matrix----------")
    a = np.full((100, 100), 4)
    print(get_col_sum(np.array2string(a), 2))
    print("\n----------1000x1000 matrix----------")
    a = np.full((1000, 1000), 4)
    print(get_col_sum(np.array2string(a), 2))
    print("\n----------10000x10000 matrix----------")
    a = np.full((10000, 10000), 4)
    print(get_col_sum(np.array2string(a), 2))

