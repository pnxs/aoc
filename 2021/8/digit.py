#!/usr/bin/env python3

def seg_to_bitfield(seg):
    bv = 0
    for x in seg:
        bv |= 1 << (ord(x) - ord("a"))
    return bv

def assign_numbers(observation):
    ob_bit = []
    for o in observation:
        ob_bit.append(seg_to_bitfield(o))

    no = {}
    # 1, 4, 7, 8
    no[1] = list(filter(lambda i: bin(i).count("1") == 2, ob_bit))[0]
    no[4] = list(filter(lambda i: bin(i).count("1") == 4, ob_bit))[0]
    no[7] = list(filter(lambda i: bin(i).count("1") == 3, ob_bit))[0]
    no[8] = list(filter(lambda i: bin(i).count("1") == 7, ob_bit))[0]
        
    ob_bit = list(filter(lambda i: i != no[1], ob_bit))
    ob_bit = list(filter(lambda i: i != no[4], ob_bit))
    ob_bit = list(filter(lambda i: i != no[7], ob_bit))
    ob_bit = list(filter(lambda i: i != no[8], ob_bit))

    # 2, 3, 5
    x = list(filter(lambda i: bin(i).count("1") == 5, ob_bit))
    for x in list(filter(lambda i: bin(i).count("1") == 5, ob_bit)):
        m1 = bin(x & no[1]).count("1")
        m4 = bin(x & no[4]).count("1")
        if m1==1 and m4==2:
            no[2] = x
        elif m1==2 and m4==3:
            no[3] = x
        elif m1==1 and m4==3:
            no[5] = x
        else:
            print("Obs:", observation)
            print("ob_bit", ob_bit)
            print(no)
            raise Exception("2,3,5 missing")

    # 0, 6, 9
    l = list(filter(lambda i: bin(i).count("1") == 6, ob_bit))
    for x in list(filter(lambda i: bin(i).count("1") == 6, ob_bit)):
        m1 = bin(x & no[1]).count("1")
        m4 = bin(x & no[4]).count("1")
        if m1==2 and m4==3:
            no[0] = x
        elif m1==1 and m4==3:
            no[6] = x
        elif m1==2 and m4==4:
            no[9] = x
        else:
            for ob in ob_bit:
                print(ob, bin(ob), bin(ob).count("1"))
            print("Obs:", observation)
            print("l", l)
            print("m1", m1, "m4", m4)
            print(no)
            raise Exception("0,6,9 missing")

    rev_no = {}
    for n in no:
        rev_no[no[n]] = n

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
        if d == 1:
            cnt +=1
        if d == 4:
            cnt +=1
        if d == 7:
            cnt +=1
        if d == 8:
            cnt +=1

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

