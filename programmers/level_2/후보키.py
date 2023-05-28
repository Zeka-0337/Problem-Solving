from itertools import combinations
from typing import List

def solution(relation: List) -> int:
    H, W = len(relation), len(relation[0])
    indices = [i for i in range(W)]
    unique_case = []
    for num in range(1, W+1):
        for case in combinations(indices, num):
            tmp = set([tuple([row[idx] for idx in case]) for row in relation])
            if len(tmp) == H:
                case_set = set(case)
                for c in unique_case:
                    if c.issubset(case_set):
                        break
                else:
                    unique_case.append(case_set)                        
    return len(unique_case)
