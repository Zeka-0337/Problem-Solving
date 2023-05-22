def solution(x: int,
             y: int,
             n: int) -> int:
    dist = [1000000] * 1000001
    dist[x] = 0
    queue = [x]
    if x == y:
        return 0
    while queue:
        pos = queue.pop(0)
        num = dist[pos]
        for next_pos in [pos+n, 2*pos, 3*pos]:
            if next_pos == y:
                return num+1
            if next_pos < y and num+1 < dist[next_pos]:
                dist[next_pos] = num+1
                queue.append(next_pos)
    return -1


if __name__ == '__main__':
    x, y, n = 10, 40, 5
    result = solution(x, y, n)
    assert result == 2, "wrong answer"
