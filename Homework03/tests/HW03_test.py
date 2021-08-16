import unittest as ut
import Homework03.HW03ALL as hw03


class Homework03Test(ut.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tHomework 03 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tHomework 03 tests complete.\t-----")

    def setUp(self) -> None:
        print("\t[" + str(self.shortDescription()) + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_is_string(self):
        """Testing is_string() function"""

        print("\t\tTesting for the wrong input type.")

        print("\t\tInteger...")
        self.assertEqual(hw03.is_string("\t\t\t", 1), False)

        print("\t\tFloat...")
        self.assertEqual(hw03.is_string("\t\t\t", 1.0), False)

        print("\t\tNone...")
        self.assertEqual(hw03.is_string("\t\t\t", None), False)

        print("\t\tList...")
        self.assertEqual(hw03.is_string("\t\t\t", [1, 2, 3]), False)

    def test_extract_numbers(self):
        """Testing extract_numbers() function"""

        print("\t\tEmpty string...")
        self.assertEqual(hw03.extract_numbers("\t\t", ""), None)

        print("\t\tMissing numbers in the string...")
        self.assertEqual(hw03.extract_numbers("\t\t", "aaa 3j ccc"), None)

        print("\t\tInvalid separator...")
        self.assertEqual(hw03.extract_numbers("\t\t", "2,54 3,0"), None)

        print("\t\tCorrect sequence of numbers [1.5 2.5 -4.55]...")
        self.assertEqual(hw03.extract_numbers("\t\t", "1.5 2.5 -4.55"), [1.5, 2.5, -4.55])
        print("\t\t\t" + str(hw03.extract_numbers("", "1.5 2.5 -4.55")))

    def test_get_square_root(self):
        """Testing get_square_root() function"""
        print("\t\tEmpty string...")
        self.assertEqual(hw03.get_square_root(""), None)

        print("\t\tNegative number...")
        self.assertEqual(hw03.get_square_root("-1"), None)

        print("\t\tMore than one number...")
        self.assertEqual(hw03.get_square_root("1 2 3"), None)

        print("\t\tNo numbers in the string...")
        self.assertEqual(hw03.get_square_root("aaa bbb ccc"), None)

        print("\t\tCorrect value (4.0)...")
        self.assertEqual(hw03.get_square_root("4.0"), 2.0)
        print(str(hw03.get_square_root("4.0")))

    def test_max_in_sequence(self):
        """Testing max_in_sequence() function"""

        print("\t\tEmpty string...")
        self.assertEqual(hw03.max_in_sequence(""), None)

        print("\t\tNo numbers in the string...")
        self.assertEqual(hw03.max_in_sequence("aaa bbb 3,56"), None)

        print("\t\tCorrect sequence ([-1, 2, 3.0])...")
        self.assertEqual(hw03.max_in_sequence("-1 2 3.0"), 3.0)
        print(str(hw03.max_in_sequence("-1 2 3.0")))

    def test_apply_math_to_list(self):
        """Testing apply_math_to_list() function"""

        print("\t\tEmpty string...")
        self.assertEqual(hw03.apply_math_to_list(""), None)

        print("\t\tNo numbers in the string...")
        self.assertEqual(hw03.apply_math_to_list("aaa bbb 3,56"), None)

        print("\t\tOne number in the string...")
        self.assertEqual(hw03.apply_math_to_list("+ 2.54"), None)

        print("\t\tWrong operator...")
        self.assertEqual(hw03.apply_math_to_list("/ 2. 4"), None)

        print("\t\tCorrect input...")

        print("\t\t\t+ -1 2.0 3.0")
        self.assertEqual(hw03.apply_math_to_list("+ -1 2.0 3.0"), 4.0)
        print(str(hw03.apply_math_to_list("+ -1 2.0 3.0")))

        print("\t\t\t* -1 2.0 3.0")
        self.assertEqual(hw03.apply_math_to_list("* -1 2.0 3.0"), -6.0)
        print(str(hw03.apply_math_to_list("* -1 2.0 3.0")))

    def test_get_n_fibonacci_sequence(self):
        """Testing get_n_fibonacci_sequence() function"""

        print("\t\tEmpty string...")
        self.assertEqual(hw03.get_n_fibonacci_sequence(""), None)

        print("\t\tNegative index...")
        self.assertEqual(hw03.get_n_fibonacci_sequence("-3"), None)

        print("\t\tZero index...")
        self.assertEqual(hw03.get_n_fibonacci_sequence("0"), None)

        print("\t\tSmall float...")
        self.assertEqual(hw03.get_n_fibonacci_sequence("0.35"), None)

        print("\t\tCorrect input...")
        print("\t\tOne to five...")
        self.assertEqual(hw03.get_n_fibonacci_sequence("5"), [1, 1, 2, 3, 5])
        print("\t\t\t" + str(hw03.get_n_fibonacci_sequence("5")))

        print("\t\tFifth...")
        self.assertEqual(hw03.get_n_fibonacci_sequence("5", True), 5)
        print("\t\t\t" + str(hw03.get_n_fibonacci_sequence("5", True)))


# region main
if __name__ == "__main__":
    ut.main()
# endregion
