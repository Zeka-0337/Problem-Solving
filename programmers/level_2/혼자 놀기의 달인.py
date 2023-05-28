from typing import List

def solution(cards: List[int]) -> int:
    """Solve with dfs."""
    visit = [False] * (len(cards)+1)
    def dfs(n: int) -> int:
        if visit[n]:
            return 0
        visit[n] = True
        return dfs(cards[n-1]) + 1
    answer = []
    for i in range(1, len(cards)+1):
        if not visit[i]:
            answer.append(dfs(i))
    if len(answer) == 1:
        return 0
    answer.sort()
    return answer[-1] * answer[-2]
