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

    username = prompt.string('May I have your name? ', empty=True)
    if username is None:
        quit_when_silent()
    else:
        print('Hello, {0}!\n'.format(username))
    return username


def quit_when_silent() -> None:
    """Quit when the user is silent.

    If the user only presses Enter with no real answer,
    we end the game instead of endlessly repeating the prompt.
    """
    print('We can play later if you want.')
    quit()


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

        # Answer to some games may be an integer, but
        # we always get users_answer as a string
        # because the prompt package doesn't have
        # an easy way to get int OR string
        users_answer = prompt.string('Your answer: ', empty=True)
        # That's why we compare it to str(correct_answer)
        if users_answer == str(correct_answer):
            print('Correct!')
            questions -= 1
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
            return None

    print('Congratulations, {0}!'.format(username))
