
from datetime import date
from balance import matcher
from nose.tools import assert_equal

def test_simple_regex_date_match():

    conditions = {
        "regex": "\d+-\d+-\d+"
    }
    day = date(2016,8,1)
    
    expected = True
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_simple_regex_date_match_fail():

    conditions = {
        "regex": "\d+-02-\d+"
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_weekday_date_match():

    conditions = {
        "weekday": 0
    }
    day = date(2016,8,1)

    expected = True
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_weekday_date_match_fail():

    conditions = {
        "weekday": 6
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_multiple_conditions_match():
    conditions = {
        "weekday": 0,
        "regex": "2016-08-\d+"
    }
    day = date(2016,8,1)

    expected = True
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_multi_conditions_1st_fail_2nd_ok_doesnt_match():
    conditions = {
        "regex": "2016-05-\d+",
        "weekday": 0
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)


def test_multi_conditions_1st_ok_2nd_fail_doesnt_match():
    conditions = {
        "regex": "2016-08-\d+",
        "weekday": 1
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_conditions(conditions, day)
    assert_equal(actual, expected)

