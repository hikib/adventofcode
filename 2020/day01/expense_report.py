def main():
    with open("input.txt", "r") as f:
        numbers = [int(d) for d in f.readlines()]
    test = [int(d) for d in "1721 979 366 299 675 1456".split()]
    print(get_expenses(test))
    print(get_expenses(numbers))
    print(f"Result part one: {part_one(numbers)}")
    # print(f"Result part two: {part_two(numbers)}")


def get_expenses(numbers):
    for num in numbers:
        if 2020 - num in numbers:
            return num * (2020 - num)



def part_one(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


def part_two(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if sum((i, j, k)) == 2020:
                    return i * j * k

if __name__ == "__main__":
    main()

