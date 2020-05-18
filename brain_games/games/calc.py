# -*- coding:utf-8 -*-

"""Game logic for the 'brain-calc.py' game script."""

from operator import add, mul, sub
from random import choice, randint
from typing import Tuple

RULESET = ('What is the result of the expression?')


def create_round(max_number=20) -> Tuple[str, str]:
    """Show a random expression, ask what it equals to.

    Args:
        max_number: maximum random numbers in the expression

    Returns:
        the expression to calculate, the correct answer to the question
        as strings, because the game engine only accepts strings
    """
    random_number1 = randint(1, max_number)
    random_number2 = randint(1, max_number)
    operations = {'+': add, '-': sub, '*': mul}
    sign = choice(list(operations.keys()))
    true_answer = operations[sign](random_number1, random_number2)
    expression = '{0} {1} {2}'.format(random_number1, sign, random_number2)
    return expression, str(true_answer)
