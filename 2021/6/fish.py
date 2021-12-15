#!/usr/bin/env python3

with open("input") as f:
    fish = list(map(int, f.readline().split(",")))

fm = {}
days = 200

def calc_sum(age, days):
    fish = [age]
    for d in range(0,days):
        #print(d,len(fish), fish)
        #print(d, fish)
        new_fish = []
        for i, f in enumerate(fish):
            if fish[i] == 0:
                fish[i] = 7
                new_fish.append(8)
            fish[i] -= 1
        fish.extend(new_fish)
    return len(fish)

for x in range(0,6):
    print("Precalc ",x)
    fm[x] = calc_sum(x, days)

#fish = [3,4,3,1,2]
fs = 0
for f in fish:
    fs += fm[f]

print("Sum",fs)


