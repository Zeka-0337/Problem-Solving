def possible(r, c, order, park):
    h, w = len(park), len(park[0])
    dic = {
        "N": [-1, 0],
        "S": [1, 0],
        "W": [0, -1],
        "E": [0, 1]}
    dirc, number = order.split(" ")
    for i in range(int(number)):
        r, c = r+dic[dirc][0], c+dic[dirc][1]
        if r < 0 or r == h or c < 0 or\
            c == w or park[r][c] == "X":
            return False
    return [r, c]
    
def solution(park, routes):
    for i, row in enumerate(park):
        if "S" in row:
            r = i
            c = row.index("S")
    for route in routes:
        result = possible(r, c, route, park)
        if result:
            r, c = result
    return [r, c]