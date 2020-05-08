# -*- coding:utf-8 -*-

"""Command Line Interface module, contains functions to interact with users."""


import prompt


def welcome_user(rules=None) -> str:
    """
    Greet the user, print the rules, ask user's name.

    Args:
        rules: the rules of the game (if there are any)

    Returns:
        str: the name entered by the user (we need it later in games)
    """
    print('Welcome to the Brain Games!\n')

    # Task in step 5 adds a line about game rules
    # after "Welcome..."" but before "May I have...".
    if rules is not None:
        print('{0}\n'.format(rules))

    username = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(username))
    return username


def play(game, questions=3) -> None:
    """Run the game logic.

    Args:
        game: which of the brain games to run
        questions: how many questions to ask

    Returns:
        None
    """
    username = welcome_user(game.RULES)

    while questions > 0:
        question, correct_answer = game.create_question()

        print('Question: {0}'.format(question))
        users_answer = prompt.string('Your answer: ')

        if users_answer == correct_answer:
            print('Correct!')
            questions -= 1
        else:
            # We split this print into several lines to stay < 80 symbols.
            # We do it via explicit concatenation to follow WPS 326.
            # C813 asks for a trailing comma in the end.
            print(
                "'{0}' is the wrong answer ;(.".format(users_answer)
                +
                "The correct answer was '{0}'.".format(correct_answer),
            )
            print("Let's try again, {0}!".format(username))
            # Task in step 5 says that the game ends after one wrong answer.
            return None

    print('Congratulations, {0}!'.format(username))
