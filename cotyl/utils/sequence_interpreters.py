# sequence_interpreters.py

from typing import List


def coalesce(*args, default=None):
    for a in args:
        if a is not None:
            return a
    if default:
        return default


def filter_dict(d: dict, keys: List[str]) -> bool:
    temp = {}
    for k in keys:
        if k in d.keys():
            temp[k] = d[k]
    return temp