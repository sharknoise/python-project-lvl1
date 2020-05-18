# -*- coding:utf-8 -*-

"""Example script for Brain Games.

Greets user by name, but there's no game after that.
"""

from brain_games.cli import ask_username, print_intro


def main():
    """Print a general greeting, then greets user by name.

    This script doesn't use the cli.py engine like all other scripts,
    because there's no game and no game logic module. This script only
    shows how each game begins.
    """
    # We don't need to print any rules when running brain_games.py,
    # but other games will have rules.
    print_intro(rule=None)
    # We don't assign the name returned by ask_username()
    # because there's no game in this example, but in other games
    # the user name may be used more than once.
    ask_username()


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
