#!/usr/bin/env python3.9

import pathlib
import re
import itertools

def main():
    program = Data("input.prod").as_string()
    i = 0

    pattern = re.compile("^mem\[(\d+)\] = (\d+)$")
    memory_one = {}
    memory_two = {}

    while i < len(program):
        if program[i].startswith("mask"):
            mask = program[i][-36:]
        else:
            match = re.search(pattern, program[i].strip())
            idx, value = match.groups()
            memory_one = part_one(idx, value, mask, memory_one)
            memory_two = part_two(idx, value, mask, memory_two)
        i += 1

    print("Part 1: ", sum(memory_one.values()))
    print("Part 2: ", sum(memory_two.values()))
    return

def part_one(idx, value, mask, memory):
    result = to_bin(value)
    for i in range(len(mask)):
        if mask[i] in "10":
            result = "".join((result[:i], mask[i], result[i + 1:]))
    memory[idx] = int(result, 2)
    return memory


def part_two(idx, value, mask, memory):
    address = to_bin(idx)

    result = ""
    for m, a in zip(mask, address):
        if m == "1": result += m
        elif m == "0": result += a
        else: result += "X"

    x_idx = [x.start() for x in re.finditer("X", result)]

    floats  = itertools.product("10", repeat=result.count("X"))
    for f in floats:
        for i, x in enumerate(x_idx):
            result = "".join((result[:x], f[i], result[x + 1:]))
        memory[int(result, 2)] = int(value)
    return memory


def to_bin(value):
    return format(int(value), "b").zfill(36)


class Data:
    def __init__(self, file_name):
        self.file_name = file_name

    def as_int(self):
        numbers = [int(d) for d in self._get_data()]
        return numbers

    def as_string(self):
        return self._get_data()

    def _get_data(self):
        directory = pathlib.Path(__file__).parent.absolute()
        input_file = directory.joinpath(self.file_name)
        with open(input_file, "r") as f:
            data = [d.strip() for d in f.readlines()]
        return data


if __name__ == "__main__":
    main()

