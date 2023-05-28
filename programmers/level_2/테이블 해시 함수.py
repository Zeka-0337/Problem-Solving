from functools import reduce
from typing import List

def solution(data: List, col: int, row_begin: int, row_end: int) -> int:
    data.sort(key = lambda x: [x[col-1], -x[0]])
    answer = []
    for i in range(row_begin-1, row_end):
        row = data[i]
        s_i = sum([x%(i+1) for x in row])
        answer.append(s_i)
    if len(answer) == 1:
        return answer[0]
    return reduce(lambda x, y: x^y, answer)
