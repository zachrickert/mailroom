# -*- coding: utf-8 -*-
"""Test of mailroom.py."""

import pytest
import mailroom as m

DONOR_THANKYOU = [
    ('David', '10', 'Thank you, David for your donation of 10 dollars.\n'),
    ('Steven', 10, 'Thank you, Steven for your donation of 10 dollars.\n'),
    ('Zach', 9.99, 'Thank you, Zach for your donation of 9.99 dollars.\n')
]

DONOR_DICT = [
    ({'a': [1, 2, 3], 'b': [4, 5, 6], 'c':[7, 8, 9]}, [('c', 24), ('b', 15), ('a', 6)]),
    ({'a': [1], 'b': [2], 'c':[3]}, [('c', 3), ('b', 2), ('a', 1)]),
    ({'a': [1, 3], 'b': [2, 2], 'c':[4, 0]}, [('a', 4), ('b', 4), ('c', 4)]),
    ({'a': [1, 3], 'b': [2, 5], 'c':[]}, [('b', 7), ('a', 4), ('c', 0)])
]


@pytest.mark.parametrize('donor, amount, message', DONOR_THANKYOU)
def test_generate_thankyou(donor, amount, message):
    """Test generate_thankyou func to output correct thankyou message based on
    donor's name and donation amout"""
    assert m.generate_thankyou(donor, amount) == message

INPUT_FUNCS = [
    ('1', m.send_thanks),
    ('2', m.report_donors),
    ('3', m.exit)
]


@pytest.mark.parametrize('user_input, func', INPUT_FUNCS)
def test_handle_input(user_input, func):
    """Test handle_input func if return correct func to be called at each valid
    user input"""
    assert m.handle_input(user_input) == func


def test_welcome_message():
    """Test welcone_message func to output correct info and instructions"""
    assert m.welcome_message() == ('Welcome to the donor database.\n'
                                   'Enter 1 to send thank you note\n'
                                   'Enter 2 to view report\n'
                                   'Enter 3 to exit\n')

# TODO for Steven: write test for build_report_table func


@pytest.mark.parametrize('donor_dictionary, result', DONOR_DICT)
def test_donor_list_by_total(donor_dictionary, result):
    assert m.donor_list_by_total(donor_dictionary) == result

