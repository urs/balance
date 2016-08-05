from datetime import timedelta,datetime
from balance import matcher


def forecast_balance_trend(balance, start, end, rules):
    return [
        (_to_date(day), balance)
        for day in _daterange(start, end)
        for balance in [balance + _delta(day, rules)]
    ]


def forecast_diff(start, end, rules):
    return sum([ 
        rule["delta"] 
        for day in _daterange(start, end)
        for rule in rules 
        if matcher.match_conditions(rule["when"], day)
    ])


def _delta(day, rules):
    return sum([ 
        rule["delta"] 
        for rule in rules 
        if matcher.match_conditions(rule["when"], day)
    ])


def _daterange(date1, date2):
    start = _parse_date(date1)
    end   = _parse_date(date2)
    return (
        start + timedelta(days=i)
        for i in range((end - start).days + 1)
    )


def _parse_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def _to_date(date):
    return date.strftime("%Y-%m-%d")


