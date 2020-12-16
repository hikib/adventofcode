#!/usr/bin/env python3

import pathlib
import math

def main():
    notes = Data("input.test").as_string()
    arrival = int(notes[0])
    buses = [int(n) if n != "x" else n for n in notes[1].split(",")]
    solutions = (part_one(arrival, buses), part_two(buses))
    print("Part one: ", solutions[0])
    print("Part two: ", solutions[1])
    return solutions


def part_one(arrival, buses):
    earliest = None

    for i in range(len(buses)):
        if buses[i] != "x":
            time = (( arrival // buses[i] ) + 1) * buses[i]
            if not earliest:
                earliest = (buses[i], time)
                continue
            elif time - arrival < earliest[1]:
                earliest = (buses[i], time - arrival)

    return earliest, earliest[0] * earliest[1]


def part_two(buses):
    # BRUTE FORCE !
    # Tests work
    # TODO: Make it right...
    ids = range(len(buses))
    buses = [(i, b) for i, b in zip(ids, buses) if isinstance(b, int)]
    follows = lambda b, t: ((t//b[1] +1) * b[1] - t) % b[1] == b[0]

    incr = 1
    time = 0
    while not all((follows(b, time) for b in buses)):
        time += incr
        if time % 10000000 == 0:
            print(time)

    return time


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

