import re
from itertools import product
from typing import List

def solution(user_id: List[str], banned_id: List[str]) -> int:
    # replace * to . for using regular expressions
    banned_id = [ban.replace("*", ".") for ban in banned_id]
    # cache match user id for  each banned id.
    matches = []
    for ban in banned_id:
        match = []
        for user in user_id:
            m = re.match(ban, user)
            if m and len(ban) == len(user):
                match.append(user)
        matches.append(match)
    # count all match cases that has no duplicated user id.
    # use set and sort to exclude the same match cases.
    cases = set()
    for case in product(*matches):
        set_case = set(case)
        if len(case) != len(set_case):
            continue
        cases.add(tuple(sorted(case)))
    return len(cases)
