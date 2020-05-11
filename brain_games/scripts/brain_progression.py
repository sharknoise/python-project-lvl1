# -*- coding:utf-8 -*-

"""A game: name a member of an arithmetic progression."""

from brain_games.cli import play
from brain_games.games import progression


def main():
    """Run the brain-progression game in terminal."""
    play(progression)


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
