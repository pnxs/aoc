#!/usr/bin/env python3
from array import array
from functools import reduce
from ctypes import c_uint16

class ColumnCounter:
    def __init__(self):
        self.cols = []

    def clear(self):
        self.cols = []

    def processSeq(self, seq):
        for e in seq:
            self.process(e)

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

    def get_most_common_char(self):
        bits = array("B")
        for col in self.cols:
            ch = sorted(col, key=col.get, reverse=True)[0]
            if ch == '\n':
                continue
            bits.append(int(ch))
        return bits

def find_rating(f):
    numbers = []
    cc = ColumnCounter()

    for line in f:
        numbers.append(line.strip('\n'))

    y = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
    ]

    bitpos = 0

    while len(numbers) > 1:
        print(len(numbers))
        cc.clear()
        cc.processSeq(numbers)
        mcb = cc.get_most_common_char()
        b = cc.cols[bitpos]
        if b['1'] >= b['0']:
            mcb = '1'
        else:
            mcb = '0'

        numbers = list(filter(lambda a: a[bitpos] == mcb, numbers))
        bitpos += 1

    o2_rate = int(numbers[0], 2)
    print(numbers[0], o2_rate)

    numbers = []
    bitpos = 0
    f.seek(0)
    for line in f:
        numbers.append(line.strip('\n'))

    while len(numbers) > 1:
        print(len(numbers))
        cc.clear()
        cc.processSeq(numbers)
        mcb = cc.get_most_common_char()
        b = cc.cols[bitpos]
        if b['0'] <= b['1']:
            mcb = '0'
        else:
            mcb = '1'

        numbers = list(filter(lambda a: a[bitpos] == mcb, numbers))
        bitpos += 1

    co2_rate = int(numbers[0], 2)
    print(numbers[0], co2_rate)
    print(o2_rate * co2_rate)

with open("input") as f:
    find_rating(f)

    #bits = get_most_common_char(cc.cols)
    #mask = c_uint16((1 << len(bits)) - 1).value
    #n = reduce(lambda m, n: (m << 1) + n, bits, 0)
    #gamma = c_uint16(n & mask).value
    #epsilon = c_uint16(~n & mask).value
    #print(f"Gamma: {gamma:b} Epsilon: {epsilon:b}")

