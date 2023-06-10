from typing import List

def solution(A: List[int], B: List[int]) -> int:
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    while A:
        a = A.pop(0)
        if B[0] > a:
            B.pop(0)
            answer += 1
        else:
            B.pop()
    return answer
