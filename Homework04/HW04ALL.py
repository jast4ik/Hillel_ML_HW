"""Hillel Machine Learning course. Homework 04."""

import AгxiliaryFunctions as af
import numpy as np
import time
import gc
import random

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

    numpy_array = np.random.rand(dimension[0], dimension[1])
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

    gc.collect()

    if benchmark_mode:
        return False
    else:
        return numpy_transposed_array


# endregion


if __name__ == "__main__":

    print("=======================Task 01=======================")
    print("\n----------10x10 matrix----------")
    print(get_col_sum((10, 10), 2, False))
    print("\n----------100x100 matrix----------")
    get_col_sum((100, 100), 2)
    print("\n----------1000x1000 matrix----------")
    get_col_sum((1000, 1000), 2)

    print("\n=======================Task 02=======================")
    print("\n----------10x10 matrix----------")
    print(get_identity_matrix(10, False))
    print("\n----------100x100 matrix----------")
    get_identity_matrix(100)
    print("\n----------1000x1000 matrix----------")
    get_identity_matrix(1000)

    print("\n=======================Task 03=======================")
    print("\n----------2x3 matrix----------")
    get_transposed_matrix((2, 3), False)
    print("\n----------20x30 matrix----------")
    get_transposed_matrix((20, 30))
    print("\n----------200x300 matrix----------")
    get_transposed_matrix((200, 300))
    print("\n----------2000x3000 matrix----------")
    get_transposed_matrix((2000, 3000))
    print("\n----------5000x3000 matrix----------")
    get_transposed_matrix((5000, 3000))
