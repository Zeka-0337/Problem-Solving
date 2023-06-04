from typing import List


def solution(cap: int, n: int, deliveries: List[int], pickups: List[int]):
    # 택배는 항상 풀로 채워서 들고감
    # 배달/수거 할 상자가 있는 집까지 가는 동안, 멀리있는집부터 채워서 배달함.
    # 멀리있는 집부터 수거상자 꽉채워서 들고옴.
    answer = 0
    for i in range(n-1, -1, -1):
        start = i
        if deliveries[i] or pickups[i]:
            break
    if not start:
        return 0
    answer += start+1
    full, empty = cap, cap
    for i in range(start, -1, -1):
        if deliveries[i]:
            while full < deliveries[i]:
                answer += i+1
                full, empty = full + cap, empty + cap
            full -= deliveries[i]
            deliveries[i] = 0
        if pickups[i]:
            while empty < pickups[i]:
                answer += i+1
                full, empty = full + cap, empty + cap
            empty -= pickups[i]
            pickups[i] = 0
    return answer * 2
