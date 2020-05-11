# -*- coding:utf-8 -*-

"""A game: find the greatest common divisor."""

from brain_games.cli import play
from brain_games.games import gcd


def main():
    """Run the brain-gcd game in terminal."""
    play(gcd)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
