#!/usr/bin/python3

from utils.file import get_input


def test():
    input = get_input("input.test")
    return two(input.split())


def solve():
    input = get_input("input.prod")
    return two(input.split())


def one(input):
    num = 0
    for i in input:
        nums = get_nums(i, dict())
        first = nums[min(nums.keys())]
        last = nums[max(nums.keys())]
        n = int(first+last)

        num += n

    return num


def two(input):
    num = 0

    for i in input:
        alphs = {"one": "1",
                 "two": "2",
                 "three": "3",
                 "four": "4",
                 "five": "5",
                 "six": "6",
                 "seven": "7",
                 "eight": "8",
                 "nine": "9"}
        nums = get_nums(i, dict())
        alphs = get_alphs(i, dict(), alphs)
        nums.update(alphs)

        first = nums[min(nums.keys())]
        last = nums[max(nums.keys())]
        n = int(first+last)

        num += n

    return num


def get_nums(input, nums, index=0):
    if input[0].isnumeric():
        nums[index] = input[0]

    return nums if len(input) == 1 else get_nums(input[1:], nums, index+1)


def get_alphs(input, nums, alphs):
    a = alphs.popitem()

    if a[0] in input:
        first = input.find(a[0])
        last = input.rfind(a[0])
        nums[first] = a[1]
        if first != last:
            nums[last] = a[1]

    return nums if not alphs else get_alphs(input, nums, alphs)


if __name__ == "__main__":
    solve()
