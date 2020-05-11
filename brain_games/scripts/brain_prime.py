# -*- coding:utf-8 -*-

"""A game: answer if a random number is prime."""

from brain_games.cli import play
from brain_games.games import prime


def main():
    """Run the brain-prime game in terminal."""
    play(prime)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
