def hour_to_min(time: str) -> int:
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def solution(n, t, m, timetable):
    time = hour_to_min("09:00")
    buses = [time + i * t for i in range(n)]
    timetable = [hour_to_min(t) for t in timetable]
    timetable.sort()
    answer = time
    for bus in buses:
        for _ in range(m):
            if not (timetable and timetable[0] <= bus):
                answer = bus
                break
            answer = timetable.pop(0) - 1
    h, m = divmod(answer, 60)
    return f"{h:02d}:{m:02d}"
