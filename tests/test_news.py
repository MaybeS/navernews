# -*- coding: utf-8 -*-
"""
    test.utility
    ---------------
    Test utility of navernews
    :author: maydev(alice.maydev@gmail.com)
"""

import pytest

from navertools import News

@pytest.fixture
def instance():
    return News({
        'keyword': 'test'
    })

def test_press():
    """ Testing for get_press
    """
    news = instance()
    for press in News.get_press():
        assert isinstance(press, str)
        news.press = press

    for press in News.get_press(label=False):
        assert isinstance(press, str)

def test_category():
    """ Testing for get_category
    """
    news = instance()
    for major, minors in News.get_category():
        assert isinstance(major, str)
        news.category = major
        for minor in minors:
            assert isinstance(minor, str)
            news.category = minor

    for major, minors in News.get_category(label=False):
        assert isinstance(major, str)
        for minor in minors:
            assert isinstance(minor, str)
