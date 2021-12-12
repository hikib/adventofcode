#! /usr/bin/python

with open("input.txt") as f:
    data = list(filter(None, f.read().split("\n")))


def toInt(x):
    if isinstance(x, list): x = x[0]
    return int(x.encode(), 2)


def zeroIsDominant(bit, length):
    return bit.count("0") > length/2


def reduceRatings(ratings, ratingSys, c):
    if len(ratings) == 1:
        return ratings
    zeros = lambda bits, idx: [b for b in bits if b[idx] == "0"]
    ones = lambda bits, idx: [b for b in bits if b[idx] != "0"]
    bits = [i for i in zip(*ratings[:len(ratings)])][c]
    isZero = zeroIsDominant(bits, len(ratings))
    if ratingSys == "csr":
        return zeros(ratings, c) if not isZero else ones(ratings, c)
    return zeros(ratings, c) if isZero else ones(ratings, c)


def part1():
    epsilon = ""
    gamma = ""
    bits = list(zip(*data[:len(data)]))
    for b in bits:
        isZero = zeroIsDominant(b, len(data))
        gamma += "1" if isZero else "0"
        epsilon += "0" if isZero else "1"
    return toInt(gamma) * toInt(epsilon)


def part2():
    c = 0
    ogs = data.copy()
    csr = data.copy()
    while len(ogs) > 1 or len(csr) > 1:
        csr = reduceRatings(csr, "csr", c)
        ogs = reduceRatings(ogs, "ogs", c)
        c += 1
    return toInt(ogs)* toInt(csr)


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())

