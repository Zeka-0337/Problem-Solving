from itertools import product
from typing import List

def solution(users: List, emoticons: List[int]) -> List:
    sales = [10, 20, 30, 40]
    answer = []
    # for all sale cases, max=2**14
    for case in product(sales, repeat=len(emoticons)):
        sub, money = 0, 0
        # for all users, max=100
        for ratio, price in users:
            total = 0
            # for all emojis, max = 7
            for sale, emoji in zip(case, emoticons):
                if sale >= ratio:
                    total += emoji * (100 - sale) / 100
            if total >= price:
                sub += 1
            else:
                money += total
        answer.append([sub, money])
    answer.sort(reverse=True)
    return answer[0]
