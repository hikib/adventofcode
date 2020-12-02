import re


def main():
    # test = [i for i in "1-3 a: abcde,1-3 b: cdefg,2-9 c: ccccccccc".split(',')]
    # valid_by_counts = [t for t in test if validate_count(t)]
    # valid_by_positions = [t for t in test if validate_position(t)]
    with open("input.txt", "r") as f:
        data = [d for d in f.readlines()]
    pattern = re.compile(r"^(?P<num_A>\d+)-(?P<num_B>\d+)\s(?P<letter>\w):\s(?P<password>\w+)$")
    valid_by_counts = [i for i in data if validate_count(pattern, i)]
    valid_by_positions = [i for i in data if validate_position(pattern, i)]
    print(f"Valid passwords by count: {len(valid_by_counts)}")
    print(f"Valid passwords by positions: {len(valid_by_positions)}")


def validate_position(pattern, line):
    matches = re.search(pattern, line)
    validate = lambda x: matches.group("letter") == matches.group("password")[int(x)-1]
    count_valids = len([i for i in (matches.group("num_A"), matches.group("num_B")) if validate(i)])
    return count_valids == 1


def validate_count(pattern, line):
    matches = re.search(pattern, line)
    count = matches.group("password").count(matches.group("letter"))
    validate = lambda x: int(matches.group("num_A")) <= x <= int(matches.group("num_B"))
    return validate(count)



if __name__ == "__main__":
    main()

