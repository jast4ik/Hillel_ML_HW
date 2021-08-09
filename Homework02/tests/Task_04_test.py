import unittest as ut
from Homework02.Task_04 import get_square_side
import numpy as np


class GetSumTest(ut.TestCase):
    """Tests for get_square_side(). Task 04."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 04 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 04 tests complete.\t-----\n")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(get_square_side("16"), 4.0)

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_square_side("  16   "), 4.0)

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_square_side(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(get_square_side(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(get_square_side(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(get_square_side([1, '1', 2]), -1)

        print("\t\tInput negative number.")
        self.assertEqual(get_square_side("-16"), -1)


if __name__ == "__main__":
    ut.main()
