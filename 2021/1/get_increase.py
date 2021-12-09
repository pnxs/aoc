#!/usr/bin/env python3

nr_increased=0
old_measurement=None
with open("input") as f:
    for m in f:
        measurement = int(m)

        if old_measurement and measurement > old_measurement:
            nr_increased += 1
        old_measurement = measurement
    
print("Nr of increases:", nr_increased)
