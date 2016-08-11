# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import sys


donor_dict = {
    'Steven': [3, 6],
    'David': [1, 5, 7],
    'Zach': [5, 3, 6]
}


def main():
    while True:
        welcome_message()
        user_input = input("Selection: ")
        if not is_valid_input(user_input, ['1', '2', '3']):
            continue
        handle_input(user_input)()


def welcome_message():
    print("Welcome to the donor database.")
    print("Enter 1 to send thank you note")
    print("Enter 2 to view report")
    print("Enter 3 to exit\n")


def is_valid_input(user_input, my_list):
    """Promt user input check if in a list."""
    if user_input in my_list:
        return True
    return False


def handle_input(user_input):
    actions = {'1': send_thanks, '2': report_donors, '3': exit}
    return actions[user_input]


def generate_thankyou(donor, amount):
    print('Thank you, {0} for your donation of {1} dollars.\n'.format(
        donor, amount)
    )


def send_thanks():
    donor = input("Enter Donor name or list > ")
    if donor == 'list':
        print(donor_dict)
        send_thanks()
    elif donor != 'return':
        amount = ''
        while type(amount) is str:
            amount = input("Input donation amount: ")
            try:
                amount = int(amount)
            except ValueError:
                continue
            else:
                donor_dict.setdefault(donor, []).append(amount)
        generate_thankyou(donor, amount)
    elif donor == 'return':
        return


def report_donors():
    donor_list = []
    for donor in donor_dict:
        donor_list.append((donor, sum(donor_dict[donor])))
    donor_list.sort(key=lambda x: -x[1])
    print('-' * 24 + '|' + '-' * 10)
    print('{0}{1}|{2}'.format('Name', ' ' * 20, 'Total'))
    print('-' * 24 + '|' + '-' * 10)
    for donor in donor_list:
        print('{0}{1}|{2}'.format(
            donor[0], ' ' * (24 - len(donor[0])), donor[1])
        )
    print('-' * 24 + '|' + '-' * 10 + '\n')


def exit():
    sys.exit(0)


if __name__ == '__main__':
    main()
