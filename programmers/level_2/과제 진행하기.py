from typing import List

def to_min(time: str) -> int:
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(plans: List) -> List[str]:
    plans = [
        [sub, to_min(start), int(last)]
        for sub, start, last in plans]
    # sort by start time
    plans.sort(key=lambda x: x[1])
    answer = []
    stack = []
    for sub, start, last in plans:
        while stack:
            # if paused plan finishes before next plan starts
            if stack[-1][1] + stack[-1][2] <= start:
                fin_sub, fin_start, fin_last = stack.pop()
                answer.append(fin_sub)
                if stack:
                    # update next paused plan's start time
                    stack[-1][1] = fin_start + fin_last
            # else, update the paused plan's last time.
            else:
                stack[-1][2] = stack[-1][1] + stack[-1][2] - start
                break
        stack.append([sub, start, last])
    return answer + [plan[0] for plan in reversed(stack)]
