"""The task #1.
User enters a name. Say hello to him by name and with an exclamation mark at the end.
"""


import re


__author__ = "Yevgen Iliashchienko"
__copyright__ = "Copyright 2021, Yevgen Iliashchienko"

__license__ = "GNU GPL"
__version = "1.0.0"
__maintainer__ = "Yevgen Iliashchienko"
__email__ = "yevgen.iliashchienko@gmail.com"
__status__ = "Development"


def get_hello_string(user_name=None):
    """Returns invitation string.

    :param user_name:
        User name. Only alphabetical characters will be proceed.
    :return:
        Invitation string.
    """

    if type(user_name) is not str:
        return "Can't handle this type of input."

    regex = re.compile("[^a-zA-Z]")
    user_name = regex.sub("", user_name)

    return "Hello, " + user_name.strip() + "!"


if __name__ == "__main__":
    user_input = input("Please, enter your name: ")

    print(get_hello_string(user_input))
