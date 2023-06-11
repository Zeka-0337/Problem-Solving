import math
from typing import List


def solution(stones: List[int], k: int) -> int:
    l, r = 0, max(stones)
    # binary search
    # need to find where n can cross and n+1 can't cross.
    while l < r:
        # so, need to try n+1 when l == n, r == (n+1).
        mid = math.ceil((l + r) / 2)
        skip = 0
        cross = True
        for stone in stones:
            if stone < mid:
                skip += 1
                if skip == k:
                    cross = False
                    break
            else:
                skip = 0
        if cross:
            # l is lower bound of answer. so not "mid - 1"
            l = mid
        else:
            r = mid - 1
    return l
