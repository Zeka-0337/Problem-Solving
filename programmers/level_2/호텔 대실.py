from typing import List
import heapq 

def to_min(time: str) -> int:
    h, m = time.split(":")
    m = float(m) 
    h = float(h) * 60
    return h + m

# 맞왜틀?
def solution(book_time: List) -> int:
    book_time = [[to_min(s), to_min(e)+10] for s, e in book_time]
    book_time.sort(key=lambda x: x[1])
    answer = 1
    queue = []
    while book_time:
        if not queue:
            queue.append(book_time.pop(0))
        _, e = queue.pop(0)
        while book_time and book_time[0][0] < e:
            queue.append(book_time.pop(0))
        answer = max(answer, len(queue)+1)
    return answer


def solution(book_time: List) -> int:
    book_time = [[to_min(s), to_min(e)+10] for s, e in book_time]
    book_time.sort()
    queue = []
    answer = 1
    for s, e in book_time:
        if not queue:
            queue.append(e)
            continue
        if queue[0] > s:
            answer += 1
        else:
            heapq.heappop(queue)
        heapq.heappush(queue, e)
    return answer
