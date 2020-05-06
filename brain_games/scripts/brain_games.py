# -*- coding:utf-8 -*-

"""Contains the general logic for Brain Games."""

from brain_games.cli import welcome_user


def main():
    """Print a greeting."""
    print('Welcome to the Brain Games!\n')  # add empty line like in the task
    welcome_user()


# check if the script runs as a program
if __name__ == '__main__':
    main()
