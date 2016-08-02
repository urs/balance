from nose.tools import assert_equal
from balance import forecaster

# feature: balance forecasting
# the future balance should be predictable based on a set of rules that 
# describe what transactions are to be expected. The output should be a 
# daily balance from start date until end date

def test_no_balance_change():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = []

    expected = 1000
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_simple_balance_addition():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": "\d+-\d+-01" }
    ]

    expected = 4000
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_simple_balance_reduction():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "rent", "delta": -500, "when": "\d+-\d+-01" }
    ]

    expected = 500
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rules():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": "\d+-\d+-01" },
        { "what": "rent", "delta": -500, "when": "\d+-\d+-02" },
        { "what": "something", "delta": -100, "when": "\d+-\d+-03" }
    ]

    expected = 3400
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rules_same_date():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": "\d+-\d+-01" },
        { "what": "rent", "delta": -500, "when": "\d+-\d+-01" },
        { "what": "something", "delta": -100, "when": "\d+-\d+-01" }
    ]

    expected = 3400
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rule_applications():
    start_balance = 1000
    start_date    = "2000-01-01"
    end_date      = "2000-12-31"
    rules = [
        { "what": "something", "delta": -100, "when": "\d+-\d+-01" }
    ]

    expected = -200
    actual = forecaster.forecast_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


