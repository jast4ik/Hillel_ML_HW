import unittest as ut
from HW_02.HW_02_EX_01 import get_hello_string


class GetHelloStringTest(ut.TestCase):
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
        self.assertEqual(get_hello_string("Yevgen"), "Hello, Yevgen!")

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(get_hello_string("   Yevgen   "), "Hello, Yevgen!")

        print("\t\tInput with non alphabetical characters.")
        self.assertEqual(get_hello_string(" @*^#$  Yevgen  213413 "), "Hello, Yevgen!")

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(get_hello_string(123), "Can't handle this type of input.")

        print("\t\tInput is float.")
        self.assertEqual(get_hello_string(123.55), "Can't handle this type of input.")

        print("\t\tInput is None.")
        self.assertEqual(get_hello_string(None), "Can't handle this type of input.")

        print("\t\tInput is list.")
        self.assertEqual(get_hello_string([1, '1', 2]), "Can't handle this type of input.")


if __name__ == "__main__":
    ut.main()
