"""Test of mailroom.py."""
# -*- coding: utf-8 -*-

import pytest
import mailroom as m


INPUT_TABLE = [('1', m.send_thanks), ('2', m.list_donors), ('3', m.exit)]


@pytest.mark.parametrize('input_string, result', INPUT_TABLE)
def test_handle_input(input_string, result):
    """Test the handling the user input."""
    assert m.handle_input(input_string) == result
