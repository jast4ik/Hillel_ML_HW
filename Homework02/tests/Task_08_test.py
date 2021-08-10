import unittest as ut
from Homework02.Task_08 import get_random_numbers


import numpy as np


class GetSumTest(ut.TestCase):
    """Tests for get_random_numbers(). Task 08."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 08 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 08 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_random_numbers(123), np.inf)

        print("\t\tInput is float.")
        self.assertEqual(get_random_numbers(123.55), np.inf)

        print("\t\tInput is None.")
        self.assertEqual(get_random_numbers(None), np.inf)

        print("\t\tInput is list.")
        self.assertEqual(get_random_numbers([1, '1', 2]), np.inf)

        print("\t\tInput more than two numbers.")
        self.assertEqual(get_random_numbers("1 2 6"), np.inf)

        print("\t\tInput alphabetical value.")
        self.assertEqual(get_random_numbers("1 aaa"), np.inf)


if __name__ == "__main__":
    ut.main()
