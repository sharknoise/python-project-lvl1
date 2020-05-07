# -*- coding:utf-8 -*-

"""Command Line Interface module, contains functions to interact with users."""


import prompt


def welcome_user(rules=None) -> str:
    """Greet the user, print the rules, ask user's name, ."""
    print('Welcome to the Brain Games!\n')

    # Task in step 5 adds a line about game rules
    # after "Welcome..."" but before "May I have...".
    if rules is not None:
        print(rules + '\n')

    username = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(username))
    # We have to return the user name as we'll need it
    # later in games.
    return username
