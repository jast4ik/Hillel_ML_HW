import unittest as ut
import Homework04.HW04ALL as hw04


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

    def test_process_dict(self):
        """Testing process_dict() function"""
        in_dict = {
            "432": ["A", "A", "B", "D", "A"],
            "53": ["L", "G", "B", "C"],
            "236": ["L", "A", "X", "G", "X", "H", "X"],
            "11": ["P", "R", "S", "D"]
        }

        expected_dict = {
            "11": ["P", "R", "S"],
            "53": ["C"],
            "236": ["L", "X", "G", "H"],
            "432": ["A", "B", "D"]
        }
        self.assertEqual(hw04.process_dict(in_dict), expected_dict)

        in_dict = {
            "1": ["A"],
            "2": ["A"],
            "3": ["A"]
        }

        expected_dict = {
            "1": [],
            "2": [],
            "3": ["A"]
        }
        self.assertEqual(hw04.process_dict(in_dict), expected_dict)

        in_dict = {
            "1": ["C", "F", "G"],
            "2": ["A", "B", "C"],
            "3": ["A", "B", "D"]
        }

        expected_dict = {
            "1": ["F", "G"],
            "2": ["C"],
            "3": ["A", "B", "D"]
        }
        self.assertEqual(hw04.process_dict(in_dict), expected_dict)


# region main
if __name__ == "__main__":
    ut.main()
# endregion
