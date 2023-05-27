from typing import List

def solution(want: List[str], number: List[int], discount: List[str]) -> int:
    queue = discount[:9]
    answer = 0
    for i in range(9, len(discount)):
        queue.append(discount[i])
        for w, n in zip(want, number):
            if queue.count(w) < n:
                break
        else:
            answer += 1
        queue.pop(0)
    return answer


if __name__ == "__main__":
    want = ["banana", "apple", "rice", "pork", "pot"]
    number = [3, 2, 2, 2, 1]
    discount = [
        "chicken",
        "apple",
        "apple",
        "banana",
        "rice",
        "apple",
        "pork",
        "banana",
        "pork",
        "rice",
        "pot",
        "banana",
        "apple",
        "banana"]
    answer = solution(want, number, discount)
    assert answer == 3, "Wrong Answer!"
