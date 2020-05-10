# -*- coding:utf-8 -*-

"""Game logic for the 'brain-calc.py' game script."""

from operator import add, mul, sub
from random import choice, randint
from typing import Tuple

RULES = ('What is the result of the expression?')


# We ignore WPS210 as 6 local variables are readable here
def create_question(max_number=20) -> Tuple[str, int]:  # noqa: WPS210
    """Show a random expression, ask what it equals to.

    Args:
        max_number: maximum random numbers in the expression

    Returns:
        the expression to calculate and the correct answer to the question
    """
    # We can ignore S311 because we don't
    # use randint "for security/cryptographic purposes".
    random_number1 = randint(1, max_number)  # noqa: S311
    random_number2 = randint(1, max_number)  # noqa: S311
    operations = {' + ': add, ' - ': sub, ' * ': mul}
    symbol = choice(list(operations.keys()))  # noqa: S311
    true_answer = operations[symbol](random_number1, random_number2)
    expression = str(random_number1) + symbol + str(random_number2)
    return expression, true_answer
