def solution(wallpaper):
    answer = []
    lur, luc, rdr, rdc = len(wallpaper), len(wallpaper[0]), 0, 0
    for r, row in enumerate(wallpaper):
        if '#' in row:
            lur, rdr = min(lur, r), max(rdr, r+1)
            lr, rc = row.index('#'), row.rindex('#')
            luc, rdc = min(luc, lr), max(rdc, rc+1)
    return [lur, luc, rdr, rdc]