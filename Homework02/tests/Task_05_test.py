import unittest as ut
from Homework02.Task_05 import find_area_and_perimeter 


class GetSumTest(ut.TestCase):
    """Tests for find_area_and_perimeter(). Task 09."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 05 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 05 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(find_area_and_perimeter("2 2 3"), (1.9843, 7.0))

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(find_area_and_perimeter("   2 2 3  "), (1.9843, 7.0))

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(find_area_and_perimeter(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(find_area_and_perimeter(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(find_area_and_perimeter(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(find_area_and_perimeter([1, '1', 2]), -1)

        print("\t\tEnter the sides for which triangle does not exist.")
        self.assertEqual(find_area_and_perimeter("1 2 3"), -1)

        print("\t\tEnter two numbers.")
        self.assertEqual(find_area_and_perimeter("1 2"), -1)

        print("\t\tEnter four numbers.")
        self.assertEqual(find_area_and_perimeter("1 2 3 4"), -1)

        print("\t\tEnter string.")
        self.assertEqual(find_area_and_perimeter("1 2 fff"), -1)


if __name__ == "__main__":
    ut.main()
