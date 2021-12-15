#!/usr/bin/env python3

with open("input") as f:
    crabs = list(map(int, f.readline().split(",")))

#crabs = [16,1,2,0,4,2,7,1,2,14]

c_max = max(crabs)
c_min = min(crabs)

print(c_min, c_max)

pos = {}
for p in range(c_min, c_max):
    fuel = 0
    for c in crabs:
        d = abs(p - c)
        fuel += (d+1)*(d/2)
    pos[fuel] = p

min_pos = min(pos)

print("Fuel", min_pos, pos[min_pos])


