# -*- coding: utf-8 -*-
"""
The mailroom script allows someone to add donors to a database and generate a
thank you letter. It also allows the user to view the list of donors in a table
format, sorted by total amount donated. The data is persisted between
application runs.
"""

import os
import sys

DEFAULT_DONORS = {
    'Steven': [3, 6],
    'David': [1, 5, 7],
    'Zach': [5, 3, 6]
}

DEFAULT_LETTER = 'Thank you, {name} for your donation of {amount}.\n'


def main_menu():    # pragma: no cover
    """Main func that get executed when run in the CLI."""
    try:
        while True:
            clear_screen()
            print(welcome_message())
            user_input = input("Selection: ")
            if user_input not in ['1', '2', '3']:
                continue
            handle_input(user_input)()
    except KeyboardInterrupt:
        exit()


def send_thanks():  # pragma: no cover
    """Send thank-you note submenu."""
    while True:
        donor = input("Enter Donor name, 'list' or 'return': ")
        if donor == 'list':
            print(build_report_table(donor_list_by_total(donor_dict)))
        elif donor == 'return':
            return
        elif donor == '':
            continue
        else:
            amount = 0
            while not amount:
                amount = validate_donation(
                    input("Input donation amount: "))
            else:
                donor_dict.setdefault(donor, []).append(amount)
            print('')
            print(generate_thankyou(donor, format_amount(amount)))


def report_donors():    # pragma: no cover
    """Report submenu."""
    clear_screen()
    donor_list = donor_list_by_total(donor_dict)
    print(build_report_table(donor_list))


def report_donors_wait():    # pragma: no cover
    """Report submenu."""
    report_donors()
    press_to_continue()


def exit():     # pragma: no cover
    """Terminate program without error."""
    save_donors(donor_dict)
    print('\nScript terminated.\n')
    sys.exit(0)


def clear_screen():     # pragma: no cover
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def press_to_continue():        # pragma: no cover
    """Wait for user input before proceeding."""
    input('Press any button to continue.')


def welcome_message():
    """Return welcome message and instruction when the app starts."""
    return ('Welcome to the donor database.\n'
            'Enter 1 to send thank you note\n'
            'Enter 2 to view report\n'
            'Enter 3 to exit\n')


def read_donors(donor_file_name='donor.txt'):
    """Read donor data from a txt file."""
    donor_dict = {}
    try:
        donor_file = open('{}/{}'.format(
            os.path.dirname(os.path.abspath(__file__)),
            donor_file_name
        ), 'r')
        for line in donor_file:
            temp_list = line.split('||')
            donor = temp_list.pop().rstrip()
            donor_dict[donor] = [float(i) for i in temp_list]
        donor_file.close()
    except IOError:
        donor_dict = DEFAULT_DONORS
    return donor_dict


def save_donors(donor_dict):    # pragma: no cover
    """Save donors information to a test file."""
    try:
        donor_file = open('{}/donor.txt'.format(
            os.path.dirname(os.path.abspath(__file__))), 'w'
        )
        for donor in donor_dict:
            line = ''
            for amount in donor_dict[donor]:
                line += '{}||'.format(amount)

            line = '{}{}{}'.format(line, donor, '\n')
            donor_file.write(line)
        donor_file.close()
    except IOError:
        print('Could not save to the donor.txt file.')


def handle_input(user_input):
    """Return function to execute to main()."""
    actions = {'1': send_thanks, '2': report_donors_wait, '3': exit}
    return actions[user_input]


def format_amount(amount):
    """Format amount as a string with $ and rounding."""
    return '${:.2f}'.format(round(amount, 2))


def generate_thankyou(donor, amount, template='letter_template.txt'):
    """Print the template_letter.txt file or a default thank you."""
    try:
        f = open('{}/{}'.format(
            os.path.dirname(os.path.abspath(__file__)), template), 'r'
        )
        letter = ''
        for line in f:
            if line[0] != '#':
                letter += line
        f.close()
    except IOError:
        letter = DEFAULT_LETTER
    return letter.format(name=donor, amount=amount)


def build_report_table(donor_list):
    """Generate a report table from donor list."""
    top_border = '\n{0}|{1}\n'.format('-' * 24, '-' * 10)
    row_separator = '{0}|{1}\n'.format('-' * 24, '-' * 10)
    header = '{0}{1}|{2}\n'.format('Name', ' ' * 20, 'Total')
    body = ''
    for donor in donor_list:
        body += '{0}{1}|{2}\n'.format(
            donor[0], ' ' * (24 - len(donor[0])), donor[1])
    return top_border + header + row_separator + body + row_separator


def donor_list_by_total(my_dict):
    """Return a sorted list of tuples, each tuple contains donor name and total
    donated amount."""
    donor_list = []
    for donor in my_dict:
        donor_list.append((donor, sum(my_dict[donor])))
    donor_list.sort(key=lambda x: -x[1])
    return donor_list


def validate_donation(my_str):
    """Check for valid donation amount, should be > 0."""
    try:
        amount = float(my_str)
    except ValueError:
        return 0
    else:
        if amount > 0:
            return amount
        else:
            return 0

if __name__ == '__main__':  # pragma: no cover
    donor_dict = read_donors()
    main_menu()
