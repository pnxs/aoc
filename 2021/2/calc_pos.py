#!/usr/bin/env python3

hpos=0
depth=0
with open("input") as f:
    for line in f:
        cmd, operand = line.split()
        operand = int(operand)
        if cmd == "forward":
            hpos += operand
        elif cmd == "up":
            depth -= operand
        elif cmd == "down":
            depth += operand
        else:
            raise "Invalid data"
        
print(f"Hpos:{hpos} Depth:{depth} Product:{hpos*depth}")
