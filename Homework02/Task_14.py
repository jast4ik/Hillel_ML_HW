"""The task #14.
One letter is given. Determine whether it is a vowel or a consonant.
"""

__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def detemine_vowel_consonant(input_string=None):
    """Defines letter is vowel or consonant.

    :param input_string:
        String to be processed.
    :return:
        True if vowel, False if consonant.
    """
    if type(input_string) is not str:
        print("Can't handle this type of input.")
        return -1

    input_string = input_string.strip()

    if len(input_string) != 1:
        print("Please, enter only one letter.")
        return -1

    if not input_string.isalpha():
        print("Please, enter ONLY letters.")
        return -1

    is_vowel = False

    vowel_letters = ['e', 'u', 'i', 'o', 'a']

    if input_string in vowel_letters:
        is_vowel = True

    return is_vowel


if __name__ == "__main__":
    user_input = input("Please, enter letter:\n")
    result = detemine_vowel_consonant(user_input)
    if result != -1:
        if result:
            print("Letter " + user_input + " is vowel.")
        else:
            print("Letter " + user_input + " is consonant.")
