#!/usr/bin/env python3
from collections import deque

with open("input") as f:
    fish = list(map(int, f.readline().split(",")))

fm = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for f in fish:
    if f not in fm:
        fm[f] = 0
    fm[f] += 1

fish = deque()
for f in fm:
    fish.append(fm[f])

for d in range(0, 256):
    z = fish.popleft()
    fish.append(z)
    fish[6] += z

print(sum(fish))



