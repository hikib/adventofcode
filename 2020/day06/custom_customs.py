import functools


def main():
    answers = get_data()
    groups = get_groups(answers)

    part_one = 0
    part_two = 0
    intersect = lambda a, b: set(a).intersection(set(b))

    for group in groups:
        part_one += len(set("".join(group)))
        part_two += len(functools.reduce(intersect, group))

    print(f"Sum of different 'yes': {part_one}")
    print(f"Sum of common 'yes': {part_two}")

def get_groups(answers):
    group = []
    for answer in answers:
        if answer != "":
            group.append(answer)
            continue
        yield group
        group.clear()

def get_data():
    with open("input.prod", "r") as f:
        data = [d.strip() for d in f.readlines()]
    return data


if __name__ == "__main__":
    main()

