# -*- coding:utf-8 -*-

"""Game logic for the 'brain-gcd.py' game script."""

# as gcd is a part of the Python Standard Library since Python 3.5,
# we don't need to write our own function for it
from math import gcd
from random import randint
from typing import Tuple

RULES = ('Find the greatest common divisor of given numbers.')


def create_question(max_number=50) -> Tuple[str, int]:
    """Show two random numbers, ask what's their greatest common divisor.

    Args:
        max_number: maximum random numbers in the expression

    Returns:
        A question string and the correct answer
    """
    # We can ignore S311 because we don't
    # use randint "for security/cryptographic purposes".
    random_number1 = randint(1, max_number)  # noqa: S311
    random_number2 = randint(1, max_number)  # noqa: S311
    true_answer = int(gcd(random_number1, random_number2))
    question = '{0} {1}'.format(random_number1, random_number2)
    return question, true_answer
