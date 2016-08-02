import re
import matcher
from functools import reduce

def match_conditions(conditions, day):
    return reduce( 
        (lambda x,y: x and y), [
            _condition_matches(matcher_type, condition, day)
            for matcher_type, condition in conditions.items()
        ]
    )


def _condition_matches(matcher_type, condition, day):
    matcher_func = _get_matcher(matcher_type)
    return matcher_func(condition, day)


def _get_matcher(matcher_type):
    return getattr(matcher, matcher_type)


def regex(condition, day):
    return bool(re.match(condition, day.strftime("%Y-%m-%d")))


def weekday(condition, day):
    return day.weekday() == condition
