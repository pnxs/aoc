#!/usr/bin/env python3

def bit1cnt(x):
    return bin(x).count("1")

def seg_to_bitfield(seg):
    bv = 0
    for x in seg:
        bv |= 1 << (ord(x) - ord("a"))
    return bv

def assign_numbers(observation):
    ob_bit = [seg_to_bitfield(o) for o in observation]

    no = {n: list(filter(lambda i: bit1cnt(i) == bc, ob_bit))[0] for n,bc in {1:2, 4:4, 7:3, 8:7}.items()}

    # 2, 3, 5
    for x in list(filter(lambda i: bit1cnt(i) == 5, ob_bit)):
        m1 = bit1cnt(x & no[1])
        m4 = bit1cnt(x & no[4])
        if m1==1 and m4==2: no[2] = x
        elif m1==2 and m4==3: no[3] = x
        elif m1==1 and m4==3: no[5] = x
        else: raise Exception("2,3,5 missing")

    # 0, 6, 9
    for x in list(filter(lambda i: bit1cnt(i) == 6, ob_bit)):
        m1 = bit1cnt(x & no[1])
        m4 = bit1cnt(x & no[4])
        if m1==2 and m4==3: no[0] = x
        elif m1==1 and m4==3: no[6] = x
        elif m1==2 and m4==4: no[9] = x
        else: raise Exception("0,6,9 missing")

    rev_no = {no[n]: n for n in no}
    return rev_no


def process(line):
    observation, digits = line.split("|")
    observation = observation.split()
    
    rev_no = assign_numbers(observation)
    
    digits_n = []
    for d in digits.split():
        digits_n.append(rev_no[seg_to_bitfield(d)])

    cnt = 0
    for d in digits_n:
        if d == 1: cnt +=1
        if d == 4: cnt +=1
        if d == 7: cnt +=1
        if d == 8: cnt +=1

    number = int("".join(map(str, digits_n)))

    return cnt, number
    

cnt = 0
nsum = 0
with open("input") as f:
    for line in f:
        c, number = process(line)
        cnt += 1
        nsum += number

print("Cnt", cnt, "Nsum", nsum)

