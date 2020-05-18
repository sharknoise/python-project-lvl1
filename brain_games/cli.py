# -*- coding:utf-8 -*-

"""Command Line Interface module, contains functions to interact with users."""


from types import ModuleType

import prompt


def welcome_user(rules: str = None) -> str:
    """
    Greet the user, print the rules, ask for user's name.

    Args:
        rules: the rules of the game (if there are any)

    Returns:
        str: the name entered by the user (we need it later in games)
    """
    print('Welcome to the Brain Games!\n')

    if rules is not None:
        print('{0}\n'.format(rules))

    username = prompt.string('May I have your name? ', empty=True)
    if username is None:
        quit_when_silent()
    else:
        print('Hello, {0}!\n'.format(username))
    return username


def quit_when_silent() -> None:
    """Quit when the user is silent.

    If the user only presses Enter without a real answer,
    we end the game instead of endlessly repeating the prompt.
    """
    print('We can play later if you want.')
    quit()


def play(game: ModuleType, round_count=3) -> None:
    """Run the game logic.

    Args:
        game: which of the brain games to run
        round_count: how many questions to ask
    """
    username = welcome_user(game.RULESET)

    while round_count > 0:
        # All answers returned by game modules should be
        # strings because we'll be comparing them
        # with strings typed by user.
        question, correct_answer = game.create_round()
        print('Question: {0}'.format(question))

        users_answer = prompt.string('Your answer: ', empty=True)
        if users_answer == correct_answer:
            print('Correct!')
            round_count -= 1
        elif users_answer is None:
            quit_when_silent()
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
            quit()

    print('Congratulations, {0}!'.format(username))
