from typing import List


def solution(key: List[List[int]], lock: List[List[int]]) -> bool:
    lock = [[1 - x for x in row] for row in lock]
    locks = [lock]
    # transpose and reverse => rotate
    for _ in range(3):
        lock = [list(col)[::-1] for col in (zip(*lock))]
        locks.append(lock)

    K, L = len(key), len(lock)
    pad = [[0] * (2 * L - 2 + K) for _ in range(L - 1)]
    padded_key = [[0] * (L - 1) + row + [0] * (L - 1) for row in key]
    padded_key = pad + padded_key + pad

    for lock in locks:
        for i in range(len(padded_key) - L):
            for j in range(len(padded_key) - L):
                if lock == [row[j : j + L] for row in padded_key[i : i + L]]:
                    return True
    return False
