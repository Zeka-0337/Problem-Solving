from typing import List

def solution(sticker: List[int]) -> int:
    if len(sticker) <= 3:
        return max(sticker)
    now, cant, delay = 0, 0, 0
    now2, cant2, delay2 = 0, 0, 0
         
    for s, s2 in zip(sticker[:-1], sticker[1:]):
        now, cant, delay = max(cant, delay), now+s, max(cant, delay)
        now2, cant2, delay2 = max(cant2, delay2), now2+s2, max(cant2, delay2)

    return max([now, cant, now2, cant2])
