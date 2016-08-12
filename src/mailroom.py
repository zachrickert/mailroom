# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import sys


donor_dict = {
    'Steven': [3, 6],
    'David': [1, 5, 7],
    'Zach': [5, 3, 6]
}


def main():
    """Main func that get executed when run in the cli"""
    while True:
        print(welcome_message())
        user_input = input("Selection: ")
        if not is_valid_input(user_input, ['1', '2', '3']):
            continue
        handle_input(user_input)()


def welcome_message():
    """Returns welcome message and instruction when the app starts"""
    return ('Welcome to the donor database.\n'
            'Enter 1 to send thank you note\n'
            'Enter 2 to view report\n'
            'Enter 3 to exit\n')


def is_valid_input(user_input, my_list):
    """Promt user input check if in a list."""
    if user_input in my_list:
        return True
    return False


def handle_input(user_input):
    actions = {'1': send_thanks, '2': report_donors, '3': exit}
    return actions[user_input]


def generate_thankyou(donor, amount):
    return 'Thank you, {0} for your donation of {1} dollars.\n'.format(
        donor, amount)


def build_report_table(donor_list):
    """Generate a report table from donor list"""
    top_border = '\n{0}|{1}\n'.format('-' * 24, '-' * 10)
    row_separator = '{0}|{1}\n'.format('-' * 24, '-' * 10)
    header = '{0}{1}|{2}\n'.format('Name', ' ' * 20, 'Total')
    body = ''
    for donor in donor_list:
        body += '{0}{1}|{2}\n'.format(
            donor[0], ' ' * (24 - len(donor[0])), donor[1])
    return top_border + header + row_separator + body + row_separator


def donor_list_by_total(my_dict):
    donor_list = []
    for donor in my_dict:
        donor_list.append((donor, sum(my_dict[donor])))
    donor_list.sort(key=lambda x: -x[1])
    return donor_list

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
        print(generate_thankyou(donor, amount))
    elif donor == 'return':
        return


def report_donors():
    """Print the list of all donors in a organized table"""
    donor_list = donor_list_by_total(donor_dict)
    print(build_report_table(donor_list))


def exit():
    sys.exit(0)

if __name__ == '__main__':
    main()
