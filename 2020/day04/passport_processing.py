import re


def main():
    with open("input.prod", "r") as f:
        data = f.readlines()

    # PART I
    has_all_entries = lambda x: len(x) == 8 or (len(x) == 7 and "cid" not in x)

    passports = yield_passports(data)
    valid_count = 0
    for passport in passports:
        if has_all_entries(passport.keys()):
            # PART II
            if check_entries(passport):
                valid_count += 1
    print(valid_count)


def yield_passports(data):
    passport = {}
    for d in data:
        if d == "\n":
            yield passport
            passport = {}
        entries = d.strip().split()
        for entry in entries:
            field, value = entry.split(":")
            passport[field] = value


def check_entries(entries):
    # Validation rules
    hgt_cm = lambda x: x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193
    hgt_in = lambda x: x[-2:] == "in" and 59 <= int(x[:-2]) <= 76
    byr = lambda x: 1920 <= int(x) <= 2002
    iyr = lambda x: 2010 <= int(x) <= 2020
    eyr = lambda x: 2020 <= int(x) <= 2030
    ecl = lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    hcl = lambda x: re.match("^#[0-9a-f]{6}$", x)
    pid = lambda x: re.match("^[0-9]{9}$", x)

    if all((
        (hgt_cm(entries["hgt"]) or hgt_in(entries["hgt"])),
        byr(entries["byr"]),
        iyr(entries["iyr"]),
        eyr(entries["eyr"]),
        ecl(entries["ecl"]),
        hcl(entries["hcl"]),
        pid(entries["pid"]))):
        return True

    return False


if __name__ == "__main__":
    main()

