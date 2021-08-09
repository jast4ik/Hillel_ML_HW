import unittest as ut
from Homework02.Task_03 import get_next_and_previous
import numpy as np


class GetSumTest(ut.TestCase):
    """Tests for get_next_and_previous(). Task 03."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 03 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 03 tests complete.\t-----\n")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(get_next_and_previous("22"), (21, 22, 23))

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_next_and_previous("   22   "), (21, 22, 23))

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_next_and_previous(123), (np.inf, np.inf, np.inf))

        print("\t\tInput is float.")
        self.assertEqual(get_next_and_previous(123.55), (np.inf, np.inf, np.inf))

        print("\t\tInput is None.")
        self.assertEqual(get_next_and_previous(None), (np.inf, np.inf, np.inf))

        print("\t\tInput is list.")
        self.assertEqual(get_next_and_previous([1, '1', 2]), (np.inf, np.inf, np.inf))


if __name__ == "__main__":
    ut.main()
