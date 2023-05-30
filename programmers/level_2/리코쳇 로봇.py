from typing import List

def solution(board: List) -> int:
    H, W = len(board), len(board[0])
    visit = [[False] * W for _ in range(H)]
    # Find Start Position
    for r in range(len(board)):
        c = board[r].index("R")
        if c != -1:
            break
    # use bfs
    queue = [[r, c, 0]]
    while queue:
        r, c, cnt = queue.pop(0)
        if visit[r][c]:
            continue
        if board[r][c] == "G":
            return cnt
        visit[r][c] = True
        case = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in case:
            r2, c2 = r, c
            # sliding until the wall or obstacle
            while r2+dr in range(H) and c2+dc in range(W) \
                and board[r2+dr][c2+dc] != "D":
                r2, c2 = r2+dr, c2+dc
            queue.append([r2, c2, cnt+1])
    return -1
