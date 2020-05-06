# -*- coding:utf-8 -*-

"""Command Line Interface module, contains functions to interact with users."""


import prompt


def welcome_user() -> None:
    """Ask for user's name and greet them."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
