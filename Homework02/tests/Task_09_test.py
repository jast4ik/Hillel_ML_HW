import unittest as ut
from Homework02.Task_09 import get_smallest


import numpy as np


class GetSumTest(ut.TestCase):
    """Tests for get_smallest(). Task 09."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 09 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 09 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(get_smallest("2 3"), 2)

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_smallest("   2 3  "), 2)

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_smallest(123), np.inf)

        print("\t\tInput is float.")
        self.assertEqual(get_smallest(123.55), np.inf)

        print("\t\tInput is None.")
        self.assertEqual(get_smallest(None), np.inf)

        print("\t\tInput is list.")
        self.assertEqual(get_smallest([1, '1', 2]), np.inf)

        print("\t\tInput more than two numbers.")
        self.assertEqual(get_smallest("1 2 6"), np.inf)

        print("\t\tInput alphabetical value.")
        self.assertEqual(get_smallest("1 aaa"), np.inf)


if __name__ == "__main__":
    ut.main()
