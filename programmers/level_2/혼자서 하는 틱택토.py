from typing import List

def solution(board: List) -> int:
    o_cnt, x_cnt = 0, 0
    for row in board:
        o_cnt += row.count('O')
        x_cnt += row.count('X')
    # 선공인 o의 개수가 하나 많거나 같아야 함.
    if o_cnt - x_cnt not in [0, 1]:
        return 0
    CASE = [
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]]
    o_made = False
    x_made = False
    for (a1, a2), (b1, b2), (c1, c2) in CASE:
        if board[a1][a2] == board[b1][b2] and board[b1][b2] == board[c1][c2]:
            if board[a1][a2] == "O":
                o_made = True
            elif board[a1][a2] == "X":
                x_made = True
    # 둘다 성공할수는 없음.
    if o_made and x_made:
        return 0
    # o의 차례에 안끝나면 안됨.
    if o_made and o_cnt - x_cnt != 1:
        return 0
    # x의 차례에 안끝나면 안됨.
    if x_made and o_cnt != x_cnt:
        return 0
    return 1
