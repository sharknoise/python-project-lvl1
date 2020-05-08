# -*- coding:utf-8 -*-

"""Game logic for the 'brain-even.py' game script."""

from random import randint
from typing import Tuple

RULES = ('Answer "yes" if a number is even, otherwise answer "no".')


def is_even(number: int) -> bool:
    """Define if the number is even.

    # noqa: DAR101
    # noqa: DAR201
    """
    return number % 2 == 0


def create_question(maxnum=100) -> Tuple[str, str]:
    """Show a random number, ask the user if the number is even.

    Args:
        maxnum: maximum random number

    Returns:
        the number and the correct answer to the question
    """
    # We can ignore S301 because we don't
    # use randint "for security/cryptographic purposes".
    random_number = randint(1, maxnum)  # noqa: S311
    true_answer = 'yes' if is_even(random_number) else 'no'
    return str(random_number), true_answer
