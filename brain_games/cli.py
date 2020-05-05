# -*- coding:utf-8 -*-

import prompt


def welcome_user() -> None:
    """Ask for user's name and greet them."""
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
