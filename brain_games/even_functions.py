# -*- coding:utf-8 -*-

"""Functions for the 'brain-even.py' game script."""

from random import randint

import prompt


def is_even(number: int) -> bool:
    """Define if the number is even.

    # noqa: DAR101
    # noqa: DAR201
    """
    return number % 2 == 0


def even_question(questions: int) -> bool:
    """Show a random number, ask the user if the number is even.

    Args:
        questions: how many questions to ask

    Returns:
        bool: were all user's answers correct or not
    """
    while questions > 0:
        # We can ignore S301 because we don't
        # use randint "for security/cryptographic purposes".
        number = randint(1, 100)  # noqa: S311
        true_answer = 'yes' if is_even(number) else 'no'

        print('Question: {0}'.format(number))
        users_answer = prompt.string('Your answer: ')

        if users_answer == true_answer:
            print('Correct!')
            questions -= 1
        else:
            # We split this print into several lines to stay < 80 symbols.
            # We do it via explicit concatenation to follow WPS 326.
            # C813 asks for a trailing comma in the end.
            print(
                "'{0}' is the wrong answer ;(.".format(users_answer)
                +
                "The correct answer was '{0}'.".format(true_answer),
            )
            # Task in step 5 says that the game ends after one wrong answer.
            return False

    return True
