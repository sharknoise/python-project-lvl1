# -*- coding:utf-8 -*-

"""A game: answer if a random number is even."""

from brain_games.cli import play
from brain_games.games import even


def main():
    """Run the brain-even game in terminal."""
    play(even)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
