import re


def main():
    my_bag = "shiny gold"
    rules = get_data()
    rule_dict = rules_to_dict(rules)
    count_one = contain_bag(my_bag, rule_dict)
    count_two = count_bags(my_bag, rule_dict)
    print(count_one)
    print(count_two)

def contain_bag(bag, rules, count=0, bags=set()):
    for parent, children in rules.items():
        if bag in children.keys() and parent not in bags:
            bags.add(parent)
            count += 1
            count = contain_bag(parent, rules, count, bags)
    return count

def count_bags(bag, rules, count=0):
    count = sum(rules[bag].values())
    for b, c in rules[bag].items():
        count += count_bags(b, rules, count) * c
    return count

def rules_to_dict(rules):
    rules_dict = dict()
    parent_pattern = re.compile(r"^(?P<parent>\w+\s\w+){1}.*$")
    child_pattern = re.compile(r"(?P<count>\d+)\s(?P<child>\w+\s\w+)")
    for rule in rules:
        parent = re.findall(parent_pattern, rule)[0]
        children = re.findall(child_pattern, rule)
        rules_dict[parent] = { c[1]: int(c[0]) for c in children }
    return rules_dict

def get_data():
    with open("input.prod", "r") as f:
        data = [d.strip() for d in f.readlines()]
    return data


if __name__ == "__main__":
    main()

