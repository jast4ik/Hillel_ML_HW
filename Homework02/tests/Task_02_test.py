import unittest as ut
from Homework02.Task_02 import get_sum


class GetSumTest(ut.TestCase):
    """Tests for get_hello_string()"""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tget_hello_string() tests start.\t\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tget_hello_string() tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(get_sum("2 3 4 5.0 6.25"), 20.25)

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_sum("   2 3 4 5.0 6.25   "), 20.25)

        print("\t\tInput with alphabetical characters.")
        self.assertEqual(get_sum(" @*^#$   2  3 4 5.0 6.25 5, sddf"), 20.25)

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_sum(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(get_sum(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(get_sum(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(get_sum([1, '1', 2]), -1)


if __name__ == "__main__":
    ut.main()
