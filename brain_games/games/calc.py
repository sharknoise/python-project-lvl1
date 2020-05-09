# -*- coding:utf-8 -*-

"""Game logic for the 'brain-calc.py' game script."""

from operator import add, mul, sub
from random import choice, randint
from typing import Tuple

RULES = ('What is the result of the expression?')


# We ignore WPS210 as 6 local variables are readable here
def create_question(maxnum=20) -> Tuple[str, int]:  # noqa: WPS210
    """Show a random expression, ask what it equals to.

    Args:
        maxnum: maximum random numbers in the expression

    Returns:
        the expression to calculate and the correct answer to the question
    """
    # We can ignore S311 because we don't
    # use randint "for security/cryptographic purposes".
    randnum1 = randint(1, maxnum)  # noqa: S311
    randnum2 = randint(1, maxnum)  # noqa: S311
    operations = {' + ': add, ' - ': sub, ' * ': mul}
    symbol = choice(list(operations.keys()))  # noqa: S311
    true_answer = operations[symbol](randnum1, randnum2)
    expression = str(randnum1) + symbol + str(randnum2)
    return expression, true_answer
