from typing import List
from collections import defaultdict


def solution(
    enroll: List[str], referral: List[str], seller: List[str], amount: List[int]
) -> List[int]:
    relation = defaultdict(str)
    sales = defaultdict(int)
    for e, r in zip(enroll, referral):
        relation[e] = r
    for s, a in zip(seller, amount):
        money = a * 100
        parent = relation[s]
        while s != "-" and money != 0:
            give = int(money * 0.1)
            sales[s] += money - give
            money = give
            s, parent = parent, relation[parent]

    return [sales[n] for n in enroll]
