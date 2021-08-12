import unittest as ut
import Homework02.AllTasks as HW2


class GetHelloStringTest(ut.TestCase):
    """Tests for get_hello_string(). Task 01."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tHomework 02 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tHomework 02 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        for f_key in HW2.functions:
            print("\t\tInput is integer.")
            self.assertEqual(HW2.functions[f_key](123), None)

            print("\t\tInput is float.")
            self.assertEqual(HW2.functions[f_key](123.55), None)

            print("\t\tInput is None.")
            self.assertEqual(HW2.functions[f_key](None), None)

            print("\t\tInput is list.")
            self.assertEqual(HW2.functions[f_key]([1, '1', 2]), None)


if __name__ == "__main__":
    ut.main()
