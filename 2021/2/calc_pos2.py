#!/usr/bin/env python3

hpos=0
depth=0
aim=0
with open("input") as f:
    for line in f:
        cmd, operand = line.split()
        operand = int(operand)
        if cmd == "forward":
            hpos += operand
            depth += aim * operand
        elif cmd == "up":
            aim -= operand
        elif cmd == "down":
            aim += operand
        else:
            raise "Invalid data"
        
print(f"Hpos:{hpos} Depth:{depth} Product:{hpos*depth}")
