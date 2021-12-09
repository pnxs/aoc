#!/usr/bin/env python3

from collections import deque
from itertools import islice

def sliding_window(seq, size=3):
    if len(seq) <= size:
        return seq

    for i in range(len(seq) - size + 1):
        yield seq[i:i+size]

nr_increased=0
old_measurement=None
with open("input") as f:
    seq = []
    for m in f:
        seq.append(int(m))

    for f in sliding_window(seq):
        measurement = sum(f)

        if old_measurement and measurement > old_measurement:
            nr_increased += 1
        old_measurement = measurement

print("Nr of increases:", nr_increased)
