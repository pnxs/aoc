#!/usr/bin/env python3
import re


def draw_line(p1, p2, floor):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        x = x1
        if (y2 < y1):
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            floor[y][x] += 1
    elif y1 == y2:
        y = y1
        if (x2 < x1):
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            floor[y][x] += 1
    else:
        xd = abs(x2 - x1)
        yd = abs(y2 - y1)
        if xd != yd:
            print("Problem", p1, p2)
        if (x2 < x1):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y = y1
        for x in range(x1, x2+1):
            floor[y][x] += 1

            if (y2 > y1):
                y += 1
            else:
                y -= 1




def parse_input():
    coords = []
    max_x = 0
    max_y = 0
    r = re.compile(R"(\d+)\s*,\s*(\d+)\s*->\s*(\d+)\s*,\s*(\d+)")
    with open("input") as f:
        for line in f:
            m = re.match(r, line)
            if m:
                x1, y1, x2, y2 = m.groups()
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
                if x1 > max_x:
                    max_x = x1
                if x2 > max_x:
                    max_x = x2
                if y1 > max_y:
                    max_y = y1
                if y2 > max_y:
                    max_y = y2

                coords.append(((x1,y1), (x2,y2)))

    return coords, max_x, max_y

coords, max_x, max_y = parse_input()
max_y += 1
max_x += 1

floor = [[0]*max_x for _ in range(max_y)]

for p1, p2 in coords:
    draw_line(p1, p2, floor)

dangerous = 0
for i, r in enumerate(floor):
    row = ""
    for v in r:
        if v > 1:
            dangerous += 1
        if v == 0:
            row += " "
        else:
            row += str(v)

    #print(row)
print("Dangerous", dangerous)
