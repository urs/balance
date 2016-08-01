
from nose.tools import assert_equal
from datetime import date
from balance import calculator

# feature: balance forecasting
# the future balance should be predictable based on a set of rules that 
# describe what transactions are to be expected. The output should be a 
# daily balance from start date until end date

def test_no_balance_change():
    start_balance = 1000
    start_date    = date(2000, 1, 1)
    end_date      = date(2000, 1, 31)
    rules = []

    expected = 1000
    actual = calculator.calculate_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)


def test_simple_balance_addition():
    start_balance = 1000
    start_date    = date(2000, 1, 1)
    end_date      = date(2000, 1, 31)
    rules = [
        { "what": "salary", "delta": 3000, "when": "\d+-\d+-01" }
    ]

    expected = 4000
    actual = calculator.calculate_balance(start_balance, start_date, end_date, rules)
    assert_equal(actual, expected)



