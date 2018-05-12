# -*- coding: utf-8 -*-
"""
    test.utility
    ---------------
    Test utility of navernews
    :author: maydev(alice.maydev@gmail.com)
"""

import pytest

from navernews import get_press, get_category

def test_press():
    """ Testing for get_press
    """
    for press in get_press():
        assert isinstance(press) == str

    for press in get_press(label=False):
        assert isinstance(press) == str

def test_category():
    """ Testing for get_category
    """
    for major, minors in get_category():
        assert isinstance(major) == str
        for minor in minors:
            assert isinstance(minor) == str

    for major, minors in get_category(label=False):
        assert isinstance(major) == str
        for minor in minors:
            assert isinstance(minor) == str
