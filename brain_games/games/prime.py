# -*- coding:utf-8 -*-

"""Game logic for the 'brain-even.py' game script."""

from random import randint
from typing import Tuple

RULES = ('Answer "yes" if the number is prime. Otherwise answer "no".')


def is_prime(number: int) -> bool:
    """Define if a number is prime.

    # noqa: DAR101
    # noqa: DAR201
    """
    # Corner cases
    if number == 1:
        return False
    if number == 2 or 3:
        return True

    # Most numbers > 3 aren't prime because their third
    # divisor is either 2 or 3
    if (number % 2 == 0 or number % 3 == 0):
        return False

    # Finally, we loop through the rest of potential
    # prime divisors 5, 7, 11, 13 ... up to √number
    divisor = 5
    while (divisor * divisor <= number):
        if (number % divisor == 0 or number % (divisor + 2) == 0):
            return False
        divisor += 6
    return True


def create_question(max_number=100) -> Tuple[int, str]:
    """Show a random number, ask the user if the number is even.

    Args:
        max_number: maximum random number

    Returns:
        the number, the correct answer to the question
    """
    random_number = randint(1, max_number)
    true_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, true_answer
