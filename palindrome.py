# palindrome example
# by Jostein Dyrset
# 02.10.17

from collections import deque


def is_palindrome(my_string):
    my_deque = deque(list(my_string))
    for i in range(len(my_deque)):
        if my_deque[i] != my_deque[len(my_deque) - i - 1]:
            return False
        print("{}: {}".format(i, my_deque))
        input("Press Enter to continue...")
    return True
