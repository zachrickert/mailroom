# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import os
import sys

DEFAULT_DONORS = {
    'Steven': [3, 6],
    'David': [1, 5, 7],
    'Zach': [5, 3, 6]
}


def main_menu():    # pragma: no cover
    """Main func that get executed when run in the CLI."""
    try:
        while True:
            print(welcome_message())
            user_input = input("Selection: ")
            if not is_valid_input(user_input, ['1', '2', '3']):
                continue
            clear_screen()
            handle_input(user_input)()
    except KeyboardInterrupt:
        print('\nScript terminated\n')


def send_thanks():  # pragma: no cover
    """Send thank-you note submenu."""
    while True:
        donor = input("Enter Donor name, 'list' or 'return': ")
        if donor == 'list':
            print(build_report_table(donor_list_by_total(donor_dict)))
        elif donor == 'return':
            return
        else:
            amount = 0
            while not amount:
                amount = validate_donation(
                    input("Input donation amount: "))
            else:
                donor_dict.setdefault(donor, []).append(amount)
            print('')
            print(generate_thankyou(donor, amount))
            print('-Sincerely, Gov. Whoever')
            press_to_continue()


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
    sys.exit(0)


def clear_screen():     # pragma: no cover
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():
    """Return welcome message and instruction when the app starts."""
    clear_screen()
    return ('Welcome to the donor database.\n'
            'Enter 1 to send thank you note\n'
            'Enter 2 to view report\n'
            'Enter 3 to exit\n')


def press_to_continue():        # pragma: no cover
    """Wait for user input before proceeding."""
    input('Press any button to continue.')


def read_donors():
    """Read donor data from a txt file."""
    global donor_dict
    donor_dict = {}
    file_found = True
    try:
        donor_file = open('donor.txt', 'r')
    except IOError:
        try:
            donor_file = open('src/donor.txt', 'r')
        except IOError:
            print('Could not find donor.txt file.')
            file_found = False

    if file_found:
        for line in donor_file:
            temp_list = line.split('||')
            donor = temp_list.pop().rstrip()
            donor_dict[donor] = [float(i) for i in temp_list]
    else:
        print('Test')
        donor_dict = DEFAULT_DONORS

    donor_file.close()
    return donor_dict


def save_donors(donor_dict):    # pragma: no cover
    """Save donors information to a test file."""
    try:
        donor_file = open('donor.txt', 'w')
    except IOError:
        print('Could not save to the donor.txt file.')

    for donor in donor_dict:
        line = ''
        for amount in donor_dict[donor]:
            line += '{}||'.format(amount)

        line = '{}{}{}'.format(line, donor, '\n')
        donor_file.write(line)
    donor_file.close()


def is_valid_input(user_input, my_list):
    """Promt user input check if in a list."""
    if user_input in my_list:
        return True
    return False


def handle_input(user_input):
    """Return function to execute to main()."""
    actions = {'1': send_thanks, '2': report_donors_wait, '3': exit}
    return actions[user_input]


def generate_thankyou(donor, amount):
    """Create thank-you not from donor name and amount."""
    return 'Thank you, {0} for your donation of ${1:.2f}.\n'.format(
        donor, round(amount, 2))


def build_report_table(donor_list):     # pragma: no cover
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
    """Return a sorted list of tuples, each tuple contains donor name and total donated amount."""
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
