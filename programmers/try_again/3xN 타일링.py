def solution(n: int) -> int:
    if n%2:
        return 0
    dp = [3]
    for _ in range(n//2-1):
        dp.append((dp[-1]*3 + sum(dp[:-1])*2 + 2)%1000000007)
    return dp[-1]