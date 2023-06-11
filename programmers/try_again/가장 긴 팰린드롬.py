def solution(s: str) -> int:
    N = len(s)
    dp = [[False] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = True
    for i in range(N - 1):
        dp[i + 1][i] = True
    answer = 1
    for delta in range(1, N):
        for a in range(N - delta):
            b = a + delta
            if s[a] == s[b] and dp[a + 1][b - 1]:
                dp[a][b] = True
                answer = delta + 1
            else:
                dp[a][b] = False
    return answer
