
from datetime import date
from balance import matcher
from nose.tools import assert_equal

def test_simple_regex_date_match():

    rule = {
        "regex": "\d+-\d+-\d+"
    }
    day = date(2016,8,1)

    print matcher.weekday

    expected = True
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_simple_regex_date_match_fail():

    rule = {
        "regex": "\d+-02-\d+"
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_weekday_date_match():

    rule = {
        "weekday": 0
    }
    day = date(2016,8,1)

    expected = True
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_weekday_date_match_fail():

    rule = {
        "weekday": 6
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_multiple_conditions_match():
    rule = {
        "weekday": 0,
        "regex": "2016-08-\d+"
    }
    day = date(2016,8,1)

    expected = True
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_multi_conditions_1st_fail_2nd_ok_doesnt_match():
    rule = {
        "regex": "2016-05-\d+",
        "weekday": 0
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)


def test_multi_conditions_1st_ok_2nd_fail_doesnt_match():
    rule = {
        "regex": "2016-08-\d+",
        "weekday": 1
    }
    day = date(2016,8,1)

    expected = False
    actual = matcher.match_rule(rule, day)
    assert_equal(actual, expected)

