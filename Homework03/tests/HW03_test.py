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

    def test_extract_tuples(self):
        """Testing extract_tuples() function"""

        print("\t\tCorrect sequence of numbers (1.23 3.33) (3 4) (5 6) (7 6.23 5)...")
        self.assertEqual(hw03.extract_tuples("\t\t", "(1.23 3.33) (3 4) (5 6) (7 6.23 5)")[0],
                         [[1.23, 3.33], [3, 4], [5, 6], [7, 6.23, 5]])

        print("\t\tIncorrect sequence of numbers 1 2 3 4 rrr...")
        self.assertEqual(hw03.extract_tuples("\t\t", "1 2 3 4 rrr")[0], None)

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

    def test_get_fibonacci_sequence_to_n(self):
        """Testing get_fibonacci_sequence_to_n() function"""

        print("\t\tCorrect input...")
        print("\t\t21...")
        self.assertEqual(hw03.get_fibonacci_sequence_to_n("21"), [1, 1, 2, 3, 5, 8, 13])
        print("\t\t\t" + str(hw03.get_fibonacci_sequence_to_n("21")))

        print("\t\t1...")
        self.assertEqual(hw03.get_fibonacci_sequence_to_n("1"), None)
        print("\t\t\t" + str(hw03.get_fibonacci_sequence_to_n("1")))

    def test_get_cel_fahr_cor_table(self):
        """Testing get_cel_fahr_cor_table() function"""

        print("\t\tEmpty string...")
        self.assertEqual(hw03.get_cel_fahr_cor_table(""), None)

        print("\t\tOne number...")
        self.assertEqual(hw03.get_cel_fahr_cor_table("1.0"), None)

        print("\t\tTwo numbers...")
        self.assertEqual(hw03.get_cel_fahr_cor_table("1.0 2.0"), None)

        print("\t\tNo numbers...")
        self.assertEqual(hw03.get_cel_fahr_cor_table("fg dfg gf gfd fgd "), None)

        print("\t\tCorrect input [-1.23 1.23 1]...")
        self.assertEqual(hw03.get_cel_fahr_cor_table("-1.23 1.23 1"),
                         [(-1.23, 29.79), (-0.23, 31.59), (0.77, 33.39), (1.23, 34.21)])
        print(str(hw03.get_cel_fahr_cor_table("-1.23 1.23 1")))

        print("\t\tCorrect input [1.23 -1.23 1]...")
        self.assertEqual(hw03.get_cel_fahr_cor_table("1.23 -1.23 1"),
                         [(-1.23, 29.79), (-0.23, 31.59), (0.77, 33.39), (1.23, 34.21)])
        print(str(hw03.get_cel_fahr_cor_table("1.23 -1.23 1")))

    def test_get_polygon_perimeter(self):
        """Testing get_polygon_perimeter() function"""

        print("Incorrect input...")
        self.assertEqual(hw03.get_polygon_perimeter("fg dfg gf gfd fgd "), None)
        self.assertEqual(hw03.get_polygon_perimeter("(1 2)"), None)
        self.assertEqual(hw03.get_polygon_perimeter("(1 2) (1) ( 1 2 3)"), None)
        self.assertEqual(hw03.get_polygon_perimeter("(1 2) ( -6 5)"), None)

        print("Correct input...")
        self.assertEqual(hw03.get_polygon_perimeter("(1 2) (-6 9) (12.3 6.8)"), 40.608)

    def test_get_ratio(self):
        """Testing get_ratio() function"""

        print("Correct input...")
        self.assertEqual(hw03.get_ratio("1 2 3"), [(2, "equal to", 2), (3, "greater than", 2), (1, "less than", 2)])

    def test_greater_than_neighbors(self):
        """Testing greater_than_neighbors() function"""

        print("Correct input...")
        self.assertEqual(hw03.greater_than_neighbors("1 2 3 1 1 1 6 5"), [3, 6])

    def test_reverse_list(self):
        """Testing reverse_list() function"""

        print("Correct input...")
        self.assertEqual(hw03.reverse_list("1 2 3 1 1 1 6 5"), [5, 6, 1, 1, 1, 3, 2, 1])

    def test_get_vals_at_range(self):
        """Testing get_vals_at_range() function"""

        print("Incorrect input...")
        self.assertEqual(hw03.get_vals_at_range("1 2 3 1 1 1 6 5 (-10 3)"), None)
        self.assertEqual(hw03.get_vals_at_range("1 2 3 1 1 1 6 5 "), None)

        print("Correct input...")
        self.assertEqual(hw03.get_vals_at_range("1 2 3 1 1 1 6 5 (1 5)"), [2, 3, 1, 1])
        self.assertEqual(hw03.get_vals_at_range("1 2 3 1 1 1 6 5 (5 1)"), [2, 3, 1, 1])

    def test_get_unique_numbers(self):
        """Testing get_unique_numbers() function"""

        print("Correct input...")
        self.assertEqual(hw03.get_unique_numbers("1 2 3 1 1 1 6 5"), [2, 3, 5, 6])

    def test_get_numbers_in_two_sequences(self):
        """Testing get_numbers_in_two_sequences() function"""

        print("Correct input...")
        self.assertEqual(hw03.get_numbers_in_two_sequences(["1 2 3 1 5", "2 8 -11 5"]), [2, 5])

    def test_product_matrices(self):
        """Testing product_matrices() function"""

        print("Incorrect input...")
        self.assertEqual(hw03.product_matrices(["(1 2 3) (3 4)", "(1) (2 3)"]), None)
        self.assertEqual(hw03.product_matrices(["(1 2 3) (3 4)"]), None)
        self.assertEqual(hw03.product_matrices(["(1 2 3) (3 4 5)", "(1 3) (2 3)"]), None)

        print("Correct input...")
        self.assertEqual(hw03.product_matrices(["(1 2) (3 4)", "(5 6) (7 8)"]),
                         [[19, 22], [43, 50]])

        self.assertEqual(hw03.product_matrices(["(1 2 3) (4 5 6) (7 8 9)", "(10 11 12) (13 14 15) (16 17 18)"]),
                         [[84, 90, 96], [201, 216, 231], [318, 342, 366]])


# region main
if __name__ == "__main__":
    ut.main()
# endregion
