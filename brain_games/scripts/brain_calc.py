# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""A game: calculate the result of an expression."""

from brain_games.cli import play
from brain_games.games import calc


def main():
    """Run the brain-calc game in terminal."""
    play(calc)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
