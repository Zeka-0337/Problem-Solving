from typing import List
import sys
sys.setrecursionlimit(10**5)


def solution(maps: List[str]) -> List[int]:
    answer = []
    H, W = len(maps), len(maps[0])
    visit = [[False] * W for _ in range(H)]

    def dfs(r, c):
        if r in [-1, H] or c in [-1, W] or visit[r][c] or maps[r][c] == 'X':
            return 0
        ls = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        days = int(maps[r][c])
        visit[r][c] = True
        for dr, dc in ls:
            days += dfs(r + dr, c + dc)
        return days

    for r in range(H):
        for c in range(W):
            if maps[r][c] == 'X' or visit[r][c]:
                continue
            answer.append(dfs(r, c))

    return sorted(answer) if answer else [-1]
