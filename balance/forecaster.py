from datetime import timedelta,datetime
import re

def forecast_balance(balance, start, end, rules):
    start_date, end_date = [_parse_date(date) for date in [start, end]]

    for day in _daterange(start_date, end_date):
        for rule in rules:
            if _matches(rule, day):
                balance += rule["delta"]
    return balance


def _parse_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def _matches(rule, day):
    return re.match(rule["when"], day.strftime("%Y-%m-%d"))


def _daterange(start, end):
    return (start + timedelta(days=i) 
            for i in range((end - start).days + 1))

