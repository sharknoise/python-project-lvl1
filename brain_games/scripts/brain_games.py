# -*- coding:utf-8 -*-

"""Example script for Brain Games.

Greets user by name, but there's no game after that.
"""

from brain_games.cli import welcome_user


def main():
    """Print a greeting."""
    # We don't need to print any rules when running brain_games.py
    # but we will use welcome_user() in other game scripts which
    # have rules.
    welcome_user(rules=None)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
