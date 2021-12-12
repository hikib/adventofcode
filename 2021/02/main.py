#! /usr/bin/python

with open("input.txt") as f:
    data = f.read().split("\n")

def part1():
    pos = {"x": 0, "y": 0}
    for step in data:
        if not step: continue
        i = step.split()
        direction, val = i[0], int(i[1])
        if direction.startswith("f"):
            pos["x"] += val
        elif direction.startswith("d"):
            pos["y"] += val
        else:
            pos["y"] -= val
    return pos["x"] * pos["y"]

def part2():
    pos = {"x": 0, "y": 0, "aim": 0}
    for step in data:
        if not step: continue
        i = step.split()
        direction, val = i[0], int(i[1])
        if direction.startswith("f"):
            pos["x"] += val
            pos["y"] += pos["aim"] * val
        elif direction.startswith("d"):
            pos["aim"] += val
        else:
            pos["aim"] -= val
    return pos["x"] * pos["y"]

if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())

