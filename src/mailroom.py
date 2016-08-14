# -*- coding: utf-8 -*-
"""The mailroom script will do stuff."""

import sys


donor_dict = {
    'Steven': [3, 6],
    'David': [1, 5, 7],
    'Zach': [5, 3, 6]
}

DEFAULT_LETTER = 'Thank you, {name} for your donation of {amount}.\n'


def main_menu():    # pragma: no cover
    """Main func that get executed when run in the CLI."""
    try:
        while True:
            print(welcome_message())
            user_input = input("Selection: ")
            if not is_valid_input(user_input, ['1', '2', '3']):
                continue
            handle_input(user_input)()
    except KeyboardInterrupt:
        print('\nScript terminated\n')


def send_thanks():  # pragma: no cover
    """Send thank-you note submenu."""
    while True:
        donor = input("Enter Donor name, 'list' or 'return' > ")
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
            print(generate_thankyou(donor, format_amount(amount)))


def generate_thankyou(donor, amount, template='letter_template.txt'):
    """Print the template_letter.txt file or a default thank you."""
    file_found = True
    try:
        f = open(template, 'r')
    except IOError:
        try:
            template = 'src/' + template
            f = open(template, 'r')
        except IOError:
            file_found = False

    if file_found:
        letter = ""
        for line in f:
            if(not(line[0] == '#')):
                letter = letter + line
        f.close()
    else:
        letter = DEFAULT_LETTER

    return letter.format(name=donor, amount=amount)


def report_donors():    # pragma: no cover
    """Report submenu."""
    donor_list = donor_list_by_total(donor_dict)
    print(build_report_table(donor_list))


def exit():     # pragma: no cover
    """Terminate program without error."""
    sys.exit(0)


def welcome_message():
    """Return welcome message and instruction when the app starts."""
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
    """Return function to execute to main()."""
    actions = {'1': send_thanks, '2': report_donors, '3': exit}
    return actions[user_input]


def format_amount(amount):
    """Format amount as a string with $ and rounding."""
    return '${:.2f}'.format(round(amount, 2))


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
    main_menu()
