from typing import List
from collections import Counter

def solution(topping: List[int]) -> int:
    left_topping = set()
    right_topping = Counter(topping)
    answer = 0
    for t in topping:
        right_topping[t] -= 1
        left_topping.add(t)
        if right_topping[t] == 0:
            del right_topping[t]
        if len(left_topping) == len(right_topping):
            answer += 1
    return answer

if __name__ == "__main__":
    topping = [1, 2, 1, 3, 1, 4, 1, 2]	
    answer = solution(topping)
    assert answer == 2, "Wrong Answer"
