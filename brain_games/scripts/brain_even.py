# -*- coding:utf-8 -*-

"""A game where the user needs to answer if a random number is even."""

from brain_games.cli import welcome_user
from brain_games.even_functions import even_question

EVEN_RULES = ('Answer "yes" if a number is even, otherwise answer "no".')


def main():
    """Run the brain-even game in terminal."""
    # We have to send the rules as an argument
    # because they are printed in the middle of the welcome message.
    # welcome_user returns username because we need it in the final message.
    username = welcome_user(EVEN_RULES)
    # The task says that the user needs to give 3 correct answers.
    game_success = even_question(3)
    if game_success:
        print('Congratulations, {0}!'.format(username))
    else:
        print("Let's try again, {0}!".format(username))


# Check if the module runs as a program.
if __name__ == '__main__':
    main()
