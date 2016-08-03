from datetime import timedelta,datetime
from balance import matcher
from functools import reduce
import re


def forecast_balance_trend(balance, start, end, rules):

    balances = []
    for day in _daterange(start, end):
        delta = _calculate_delta_for_day(day, rules)
        balance += delta
        balances.append((_to_date(day), balance))

    return balances 


def _calculate_delta_for_day(day, rules):
    day_delta = 0;
    for rule in rules:
        if matcher.match_conditions(rule["when"], day):
            day_delta += rule["delta"]
    return day_delta


def forecast_diff(start, end, rules):

    deltas = [ 
        rule["delta"] 
        for day in _daterange(start, end)
        for rule in rules 
        if matcher.match_conditions(rule["when"], day)
    ]
    return reduce(lambda x,y: x+y, deltas) if rules else 0


def _daterange(start, end):
    start_date = _parse_date(start)
    end_date   = _parse_date(end)
    return (start_date + timedelta(days=i) 
        for i in range((end_date - start_date).days + 1))


def _parse_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def _to_date(date):
    return date.strftime("%Y-%m-%d")
