from datetime import timedelta
import re

def calculate_balance(balance, start, end, rules):
    for day in _daterange(start, end):
        for rule in rules:
            if _matches(rule, day):
                balance += rule["delta"]
    return balance

def _matches(rule, day):
    return re.match(rule["when"], day.strftime("%Y-%m-%d"))

def _daterange(date1, date2):
    return (date1 + timedelta(days=i) 
            for i in range((date2 - date1).days + 1))

