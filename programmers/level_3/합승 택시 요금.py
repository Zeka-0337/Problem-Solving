import heapq
from typing import List


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    def dijkstra(idx):
        dists = [float("INF")] * (n + 1)
        dists[idx] = 0
        q = []
        heapq.heappush(q, [dists[idx], idx])
        while q:
            dist, idx = heapq.heappop(q)
            for neighbor_idx, neighbor_dist in graph[idx]:
                if dists[neighbor_idx] > neighbor_dist + dist:
                    dists[neighbor_idx] = neighbor_dist + dist
                    heapq.heappush(q, [neighbor_dist + dist, neighbor_idx])
        return dists

    graph = [[] for _ in range(n + 1)]
    for i, j, dist in fares:
        graph[i].append([j, dist])
        graph[j].append([i, dist])
    # calc all case, min dist of i to j
    dists = [] + [dijkstra(i) for i in range(1, n + 1)]
    answer = float("INF")
    for i in range(1, n + 1):
        answer = min(answer, dists[s][i] + dists[i][a] + dists[i][b])
    return answer
