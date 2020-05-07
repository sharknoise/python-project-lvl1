# -*- coding:utf-8 -*-

"""Functions for the 'brain-even.py' game script."""

from random import randint

import prompt


def isEven(number: int) -> bool:
    return True if number % 2 == 0 else False


def even_question(questions: int) -> bool:
    """
    Show a random number, ask the user if the number is even several times,
    return user's success as bool.
    """
    while questions > 0:
        number = randint(1, 100)
        true_answer = 'yes' if isEven(number) else 'no'

        print('Question: {0}'.format(number))
        users_answer = prompt.string('Your answer: ')

        if users_answer == true_answer:
            print('Correct!')
            questions -= 1
        else:
            # We split this print into 2 lines to stay < 80 symbols.
            print("'{0}' is the wrong answer ;(. The correct answer was '{1}'."
                  .format(users_answer, true_answer))
            # Task in step 5 says that the game ends after one wrong answer.
            return False

    return True
