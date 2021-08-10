import unittest as ut
from Homework02.Task_06 import get_total_and_overpayment


class GetSumTest(ut.TestCase):
    """Tests for get_total_and_overpayment(). Task 06."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 06 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 06 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input.")
        self.assertEqual(get_total_and_overpayment("1000 10"), (1100.0, 100.0))

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_total_and_overpayment("   1000  10  "), (1100.0, 100.0))

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_total_and_overpayment(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(get_total_and_overpayment(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(get_total_and_overpayment(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(get_total_and_overpayment([1, '1', 2]), -1)

        print("\t\tInput more than two numbers.")
        self.assertEqual(get_total_and_overpayment("1 2 6"), -1)

        print("\t\tInput alphabetical value.")
        self.assertEqual(get_total_and_overpayment("1 aaa"), -1)


if __name__ == "__main__":
    ut.main()
