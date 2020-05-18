# -*- coding:utf-8 -*-

"""Game logic for the 'brain-even.py' game script."""

from random import randint
from typing import Tuple

RULE = ('Answer "yes" if a number is even, otherwise answer "no".')


def is_even(number: int) -> bool:
    """Define if the number is even.

    # noqa: DAR101
    # noqa: DAR201
    """
    return number % 2 == 0


def create_round(max_number=100) -> Tuple[str, str]:
    """Show a random number, ask the user if the number is even.

    Args:
        max_number: maximum random number

    Returns:
        the number, the correct answer to the question
        as strings, because the game engine only accepts strings
    """
    random_number = randint(1, max_number)
    true_answer = 'yes' if is_even(random_number) else 'no'
    question = str(random_number)
    return question, true_answer
