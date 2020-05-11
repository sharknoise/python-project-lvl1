# -*- coding:utf-8 -*-

"""Game logic for the 'brain-calc.py' game script."""

from operator import add, mul, sub
from random import choice, randint
from typing import Tuple

RULES = ('What is the result of the expression?')


def create_question(max_number=20) -> Tuple[str, int]:
    """Show a random expression, ask what it equals to.

    Args:
        max_number: maximum random numbers in the expression

    Returns:
        the expression to calculate, the correct answer to the question
    """
    random_number1 = randint(1, max_number)
    random_number2 = randint(1, max_number)
    operations = {' + ': add, ' - ': sub, ' * ': mul}
    symbol = choice(list(operations.keys()))
    true_answer = operations[symbol](random_number1, random_number2)
    expression = str(random_number1) + symbol + str(random_number2)
    return expression, true_answer
