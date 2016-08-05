from nose.tools import assert_equal
from balance import forecaster

# feature: balance forecasting
# the future balance should be predictable based on a set of rules that 
# describe what transactions are to be expected. The output should be a 
# daily balance from start date until end date

def test_no_balance_change():
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = []

    expected = 0
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_simple_balance_addition():
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": { "regex": "\d+-\d+-01" } }
    ]

    expected = 3000
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_simple_balance_reduction():
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "rent", "delta": -500, "when": { "regex": "\d+-\d+-01" } }
    ]

    expected = -500
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rules():
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": { "regex": "\d+-\d+-01" } },
        { "what": "rent", "delta": -500, "when": { "regex": "\d+-\d+-02" } },
        { "what": "something", "delta": -100, "when": { "regex": "\d+-\d+-03" } }
    ]

    expected = 2400
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rules_same_date():
    start_date    = "2000-01-01"
    end_date      = "2000-01-31"
    rules = [
        { "what": "salary", "delta": 3000, "when": { "regex": "\d+-\d+-01" } },
        { "what": "rent", "delta": -500, "when":  { "regex": "\d+-\d+-01" } },
        { "what": "something", "delta": -100, "when": { "regex": "\d+-\d+-01" } }
    ]

    expected = 2400
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_multiple_rule_applications():
    start_date    = "2000-01-01"
    end_date      = "2000-12-31"
    rules = [
        { "what": "something", "delta": -100, "when": { "regex": "\d+-\d+-01" } }
    ]

    expected = -1200
    actual = forecaster.forecast_diff(start_date, end_date, rules)
    assert_equal(actual, expected)


def test_forecast_balance_trend():
    start_balance = 1000
    start_date    = "2016-01-01"
    end_date      = "2016-01-15"
    rules = [
        { "what": "salary1", "delta": 2000, "when": { "regex": "\d+-\d+-01" } },
        { "what": "salary2", "delta": 1000, "when": { "regex": "\d+-\d+-01" } },
        { "what": "rent", "delta": -500, "when":  { "regex": "\d+-\d+-03" } },
        { "what": "sth once", "delta": -100, "when": { "regex": "2016-01-10" } },
        { "what": "sth weekly", "delta": -150, "when": { "weekday": 1 } }
    ]

    expected = [
        ("2016-01-01", 4000),
        ("2016-01-02", 4000),
        ("2016-01-03", 3500),
        ("2016-01-04", 3500),
        ("2016-01-05", 3350),
        ("2016-01-06", 3350),
        ("2016-01-07", 3350),
        ("2016-01-08", 3350),
        ("2016-01-09", 3350),
        ("2016-01-10", 3250),
        ("2016-01-11", 3250),
        ("2016-01-12", 3100),
        ("2016-01-13", 3100),
        ("2016-01-14", 3100),
        ("2016-01-15", 3100)
    ]
    actual = forecaster.forecast_balance_trend(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


