# -*- coding:utf-8 -*-

"""Command Line Interface module, contains functions to interact with users."""


from types import ModuleType

import prompt


def print_intro(rule: str = None):
    """
    Greet the user and print the rules.

    Args:
        rule: the rules of the game (if there are any)
    """
    print('Welcome to the Brain Games!\n')

    if rule is not None:
        print('{0}\n'.format(rule))


def ask_username() -> str:
    """Asks for user's name, greets the user by it."""
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
    print_intro(game.RULES)
    username = ask_username()

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
