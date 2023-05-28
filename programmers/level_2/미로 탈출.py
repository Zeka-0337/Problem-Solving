import copy
from typing import List, Tuple

def bfs(r: int, c: int, maps: List, target: str) -> Tuple[int, int, int]:
    maps = copy.deepcopy(maps)
    queue = [[r, c, 0]]
    H, W = len(maps), len(maps[0])
    while queue:
        r, c, cnt = queue.pop(0)
        if r in [-1, H] or c in [-1, W] or maps[r][c] == "X":
            continue
        if maps[r][c] == target:
            return (r, c, cnt)
        maps[r] = maps[r][:c] + "X" + maps[r][c+1:]
        case = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in case:
            queue.append([r+dr, c+dc, cnt+1])
    return (0, 0, -1)

def solution(maps: List) -> int:
    for r in range(len(maps)):
        if "S" in maps[r]:
            c = maps[r].index("S")
            break
    r, c, to_lever = bfs(r, c, maps, "L")
    _, _, to_exit = bfs(r, c, maps, "E")
    if to_lever == -1 or to_exit == -1:
        return -1
    return to_lever + to_exit
