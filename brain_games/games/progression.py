# -*- coding:utf-8 -*-

"""Game logic for the 'brain-progression.py' game script."""

from random import randint
from typing import Tuple

RULESET = ('What number is missing in the progression?')


def create_round(length=10, max_start=5, max_step=5) -> Tuple[str, str]:
    """Generate an arithmetic progression with a hidden member.

    Args:
        length: how many members the progression has
        max_start: maximum value of the random first member
        max_step: maximum value of the random step

    Returns:
        the progression as string ready to be printed, the hidden member
    """
    step = randint(1, max_step)
    start = randint(1, max_start)
    progression = []
    for index in range(0, length):
        progression.append(str(start + index * step))
    hidden_member_index = randint(0, length - 1)
    true_answer = progression[hidden_member_index]
    progression[hidden_member_index] = '..'
    question = ' '.join(progression)
    return question, true_answer
