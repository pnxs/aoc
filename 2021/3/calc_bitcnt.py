#!/usr/bin/env python3

from array import array
from functools import reduce
from ctypes import c_uint16


class ColumnCounter:
    def __init__(self):
        self.cols = []

    def process(self, line):
        ll = len(line)
        lc = len(self.cols)

        if ll > lc:
            for n in range(ll - lc):
                self.cols.append({})

        for i, v in enumerate(line):
            col = self.cols[i]
            if v not in col:
                col[v] = 0
            col[v] += 1


def get_most_common_char(seq):
    bits = array("B")
    for col in cc.cols:
        ch = sorted(col, key=col.get, reverse=True)[0]
        if ch == '\n':
            continue
        bits.append(int(ch))
    return bits


with open("input") as f:
    cc = ColumnCounter()
    for line in f:
        cc.process(line)

    bits = get_most_common_char(cc.cols)
    mask = c_uint16((1 << len(bits)) - 1).value
    n = reduce(lambda m, n: (m << 1) + n, bits, 0)
    gamma = c_uint16(n & mask).value
    epsilon = c_uint16(~n & mask).value
    print(f"Mask {mask:b}")

    print(f"Gamma: {gamma:b} Epsilon: {epsilon:b}")
    print(f"Gamma: {gamma} Epsilon: {epsilon}")
    power_consumption = gamma * epsilon
    print(f"Power consumption: {power_consumption}")

