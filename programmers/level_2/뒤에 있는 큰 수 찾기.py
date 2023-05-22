def solution(numbers):
    # Initailize answer list with -1
    answer = [-1 for _ in range(len(numbers))]
    queue = []
    # for all numbers
    for idx, num in enumerate(numbers):
        # So, the queue is always sorted in descending order.
        # So, the last number of the queue is always the biggest number.
        while queue and queue[-1][1] < num:
            # number can only appended when it is the biggest number in the queue
            answer[queue.pop()[0]] = num
        queue.append([idx, num])
    return answer
