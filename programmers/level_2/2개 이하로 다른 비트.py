def next_big(num):
    str_num = str(bin(num))
    if '0' in str_num[2:]:
        # 가장 작은 자리수의 0을 1로 바꾼다.
        idx = len(str_num) - str_num.rindex('0') - 1
        # 가능하다면, 바꿀자리의 바로 뒷자리 1을 0으로 바꾸어 최대한 작아지게 만든다.
        if idx:
            idx -= 1
        return num + 2 ** idx
    # 제일 큰 자리수의 1을 0으로 바꾸고, 맨 앞에 1을 추가한다.
    return num + 2 ** (len(str_num) - 3)


def solution(numbers):
    return [next_big(num) for num in numbers]


if __name__ == '__main__':
    result = solution([2, 7])
    assert result == [3, 11], "wrong answer"
