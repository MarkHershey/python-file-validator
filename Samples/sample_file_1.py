import os
import logging as log

import time

from pathlib import Path
from abc import ABC


logger = logging.getLogger("ROOT")

test_1 = "testing line 1"

print("test_1")

# this is a comment
def main():

    """ all kinds of elements
    """

    a = 1
    b: int = 2

    if True:
        print(a + b)
        return True
    else:
        print(a - b)


def hello(name):
    print(f"hello, {name}")


class Human:
    def __init__(self):
        print("hey I am a class")

    def hey(self):
        print("hey I am a human class")


class nice(ABC):
    """abc"""


logger.debug("testing line 2")


if __name__ == "__main__":
    main()
