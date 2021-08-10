import unittest as ut
from Homework02.Task_15 import is_isosceles_or_equilateral 


class GetSumTest(ut.TestCase):
    """Tests for is_isosceles_or_equilateral(). Task 09."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 15 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 15 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(is_isosceles_or_equilateral("2 2 3"), "Triangle is isosceles.")
        self.assertEqual(is_isosceles_or_equilateral("2 2 2"), "Triangle is equilateral.")
        self.assertEqual(is_isosceles_or_equilateral("2 3 4"), "Triangle neither isosceles nor equilateral.")

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(is_isosceles_or_equilateral("   2 2 3  "), "Triangle is isosceles.")
        self.assertEqual(is_isosceles_or_equilateral("   2 2 2  "), "Triangle is equilateral.")
        self.assertEqual(is_isosceles_or_equilateral("   2 3 4  "), "Triangle neither isosceles nor equilateral.")

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(is_isosceles_or_equilateral(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(is_isosceles_or_equilateral(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(is_isosceles_or_equilateral(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(is_isosceles_or_equilateral([1, '1', 2]), -1)

        print("\t\tEnter the sides for which triangle does not exist.")
        self.assertEqual(is_isosceles_or_equilateral("1 2 3"), -1)

        print("\t\tEnter two numbers.")
        self.assertEqual(is_isosceles_or_equilateral("1 2"), -1)

        print("\t\tEnter four numbers.")
        self.assertEqual(is_isosceles_or_equilateral("1 2 3 4"), -1)

        print("\t\tEnter string.")
        self.assertEqual(is_isosceles_or_equilateral("1 2 fff"), -1)


if __name__ == "__main__":
    ut.main()
