import unittest as ut
from Homework02.Task_14 import determine_vowel_consonant


class GetSumTest(ut.TestCase):
    """Tests for determine_vowel_consonant(). Task 04."""

    @classmethod
    def setUpClass(cls) -> None:
        print("-----\tTask 14 tests start.\t-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-----\tTask 14 tests complete.\t-----\n")

    def setUp(self) -> None:
        print("\t[" + self.shortDescription() + "]")

    def tearDown(self) -> None:
        print("\t[Complete.]\n")

    def test_correct_input(self):
        """Testing correct input."""

        print("\t\tid: " + self.id())

        print("\t\tAbsolutely correct input. Vowel letter.")
        self.assertEqual(determine_vowel_consonant("a"), True)

        print("\t\tAbsolutely correct input. Consonant letter.")
        self.assertEqual(determine_vowel_consonant("b"), False)

        print("\t\tInput with leading and trailing spaces.")
        self.assertEqual(determine_vowel_consonant("  a   "), True)

    def test_incorrect_input(self):
        """Testing with the wrong input type."""

        print("\t\tid: " + self.id())

        print("\t\tInput is integer.")
        self.assertEqual(determine_vowel_consonant(123), -1)

        print("\t\tInput is float.")
        self.assertEqual(determine_vowel_consonant(123.55), -1)

        print("\t\tInput is None.")
        self.assertEqual(determine_vowel_consonant(None), -1)

        print("\t\tInput is list.")
        self.assertEqual(determine_vowel_consonant([1, '1', 2]), -1)

        print("\t\tInput several letters.")
        self.assertEqual(determine_vowel_consonant("asd"), -1)

        print("\t\tInput non letter.")
        self.assertEqual(determine_vowel_consonant("2"), -1)


if __name__ == "__main__":
    ut.main()
