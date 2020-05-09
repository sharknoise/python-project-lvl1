# -*- coding:utf-8 -*-

"""Game logic for the 'brain-gcd.py' game script."""

# as gcd is a part of the Python Standard Library since Python 3.5,
# we don't need to write our own function for it
from math import gcd
from random import randint
from typing import Tuple

RULES = ('Find the greatest common divisor of given numbers.')


def create_question(maxnum=50) -> Tuple[str, int]:
    """Show two random numbers, ask what's their greatest common divisor.

    Args:
        maxnum: maximum random numbers in the expression

    Returns:
        A question string and the correct answer
    """
    # We can ignore S311 because we don't
    # use randint "for security/cryptographic purposes".
    randnum1 = randint(1, maxnum)  # noqa: S311
    randnum2 = randint(1, maxnum)  # noqa: S311
    true_answer = int(gcd(randnum1, randnum2))
    question = '{0} {1}'.format(randnum1, randnum2)
    return question, true_answer
