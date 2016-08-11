# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import sys


def main():
    user_input = prompt_user()
    handle_input(user_input)()


def prompt_user():
    """Promt user input for Send Thanks, List Donors pr Quit."""
    while True:
        user_input = raw_input('Selection: ')
        if user_input in ['1', '2', '3']:
            return user_input


def handle_input(user_input):
    actions = {'1': send_thanks, '2':list_donors, '3': exit}
    return actions[user_input]



if __name__ == '__main__':
    pass
