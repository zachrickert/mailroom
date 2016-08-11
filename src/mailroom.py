# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import sys

donor_1 = {'name': 'Steven', 'donations': [3, 6]}
donor_2 = {'name': 'David', 'donations': [1, 10, 9]}
donor_3 = {'name': 'Zach', 'donations': [1, 2]}
donor_list = [donor_1, donor_2, donor_3]

def main():
    while True:
        welcome_message()
        user_input = input("Selection: ")
        if not is_valid_input(user_input, ['1', '2', '3']):
            continue
        handle_input(user_input)()

def welcome_message():
    print("Welcome to the donor database. Please enter 1, 2 or 3")

def is_valid_input(user_input, my_list):
    """Promt user input check if in a list."""
    if user_input in my_list:
        return True
    return False


def handle_input(user_input):
    actions = {'1': send_thanks, '2':list_donors, '3': exit}
    return actions[user_input]


def send_thanks():
    my_list = []
    for donor in donor_list:
        my_list.append(donor['name'])
    donor = input ("Enter Donor name or list > ")
    if donor == 'list':
        print(my_list)
        send_thanks()




def list_donors():
    pass


def exit():
    sys.exit(0)


if __name__ == '__main__':
    main()
