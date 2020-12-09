#!/usr/bin/env python3

import pathlib


def main():
    data = get_data()
    numbers = [int(d) for d in data]

    # PART I
    i = 1
    preamble = 25
    valid = True
    while valid:
        valid, invalid_num = is_sum(numbers,preamble, i)
        i += 1
    print("First number without sum: ", invalid_num)

    # PART II
    nums = numbers[:numbers.index(invalid_num)]
    valid = False
    i = 2
    while not valid:
        valid, sum_list = get_sum_list(nums, invalid_num, i)
        i += 1
    max_min = sum((min(sum_list), max(sum_list)))
    print("Encryption weakness: ", max_min)


def is_sum(numbers, preamble, i=0):
    num = numbers[preamble + i]
    previous = numbers[i:preamble + i]
    for p in previous:
        check = num - p
        if num - p in previous:
            return True, num
    return False, num


def get_sum_list(numbers, invalid_num, i):
    n = 1
    while n <= len(numbers):
        chunk = numbers[i: i+n+1]
        n += 1
        if sum(chunk) - invalid_num == 0:
            return True, chunk
    return False, numbers


def get_data():
    file_name = "input.prod"
    directory = pathlib.Path(__file__).parent.absolute()
    input_file = directory.joinpath(file_name)
    with open(input_file, "r") as f:
        data = [d.strip() for d in f.readlines()]
    return data


if __name__ == "__main__":
    main()

