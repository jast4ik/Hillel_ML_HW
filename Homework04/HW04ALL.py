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


# region Task01
def get_col_sum(dimension: tuple, value: float):

    if dimension[0] > 10000 or dimension[1] > 10000:
        print("There is no memory check, so size of array is limited to 10000.")
        return None

    python_list = []

    print("Creating Python list...")
    start_time = time.time()
    for row_index in range(dimension[1]):
        python_list.append([])
        for col_index in range(dimension[0]):
            python_list[row_index].append(value)

    python_creation_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(python_creation_time))

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

    print("\nCalculating sum of NumPy with numpy.sum()...")
    start_time = time.time()
    sums = np.sum(numpy_array, axis=0)
    numpy_time = time.time() - start_time
    print("Time to proceed: {:.10f}s.".format(numpy_time))
    numpy_array = None
    af.print_time_relation("\nNumPy array creation ", numpy_creation_time, python_creation_time)
    af.print_time_relation("NumPy np.sum() ", numpy_time, python_time)

    print("\nCleaning up memory...")
    del numpy_array
    del python_list
    gc.collect()

    return sums

# endregion


if __name__ == "__main__":

    print("Task 01...")
    print("\n----------10x10 matrix----------")
    get_col_sum((10, 10), 2)
    print("\n----------100x100 matrix----------")
    get_col_sum((100, 100), 2)
    print("\n----------1000x1000 matrix----------")
    get_col_sum((1000, 1000), 2)
    print("\n----------10000x10000 matrix----------")
    get_col_sum((10000, 10000), 2)
