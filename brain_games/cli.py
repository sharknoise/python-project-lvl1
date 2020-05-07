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
