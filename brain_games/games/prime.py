# -*- coding:utf-8 -*-

"""Game logic for the 'brain-even.py' game script."""

from random import randint
from typing import Tuple

RULESET = ('Answer "yes" if the number is prime. Otherwise answer "no".')


def is_prime(number: int) -> bool:
    """Define if a number is prime.

    # noqa: DAR101
    # noqa: DAR201
    """
    # To avoid unnecessary time complexity we check the
    # easiest cases before starting a while loop.
    if number <= 1:
        return False
    if number in {2, 3}:
        return True

    # Most numbers > 3 aren't prime because their third
    # divisor is either 2 or 3.
    if (number % 2 == 0 or number % 3 == 0):
        return False

    # Finally, we loop through the rest of potential
    # prime divisors 5, 7, 11, 13 ... up to √number.
    divisor = 5
    while (divisor * divisor <= number):
        if (number % divisor == 0 or number % (divisor + 2) == 0):
            return False
        divisor += 6

    return True


def create_round(min_number=2, max_number=100) -> Tuple[str, str]:
    """Show a random number, ask the user if the number is prime.

    Args:
        min_number: mininum random number
            setting it to 1 or lower will test if the user
            remembers the full definition of prime numbers
        max_number: maximum random number

    Returns:
        the number, the correct answer to the question
        as strings, because the game engine only accepts strings
    """
    random_number = randint(min_number, max_number)
    true_answer = 'yes' if is_prime(random_number) else 'no'
    question = str(random_number)
    return question, true_answer
