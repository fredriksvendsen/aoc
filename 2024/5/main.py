import math

def parse_input():
    with open("5_input.txt", "r") as f:
        rules = []
        updates = []
        is_rules = True
        for line in f.readlines():
            if line == "\n":
                is_rules = False
                continue
            line = line.replace("\n", "")
            if is_rules:
                rules.append([int(x) for x in line.split("|")])
            else:
                updates.append([int(x) for x in line.split(",")])
    return rules, updates

def _filter_updates(rules, updates, filter_valid_updates=True):
    valid_updates = []
    for update in updates:
        updates_map = {}
        for idx, val in enumerate(update):
            updates_map[val] = idx
        for n1, n2 in rules:
            n1_map_val = updates_map.get(n1)
            n2_map_val = updates_map.get(n2)
            if n1_map_val is not None and n2_map_val is not None and n1_map_val > n2_map_val:
                break
        else:
            if filter_valid_updates:
                valid_updates.append(update)
            continue
        if not filter_valid_updates:
            valid_updates.append(update)
    return valid_updates

def part_one(rules, updates):
    valid_updates = _filter_updates(rules, updates)
    sum = 0
    for update in valid_updates:
        mid = math.floor(len(update)/2)
        sum += update[mid]
    print(f"Part 1 result: {sum}")

def part_two(rules, updates):
    invalid_updates = _filter_updates(rules, updates, filter_valid_updates=False)
    # cba clean solution rn, quick swap when unordered and go agane
    n_invalid = len(invalid_updates)
    fixed_updates = []
    for idx, update in enumerate(invalid_updates):
        is_fixed = False
        while not is_fixed:
            updates_map = {}
            for idx, val in enumerate(update):
                updates_map[val] = idx
            for n1, n2 in rules:
                v1 = updates_map.get(n1)
                v2 = updates_map.get(n2)
                if v1 is None or v2 is None:
                    continue
                if v1 > v2:
                    update[v1] = n2
                    update[v2] = n1
                    break
            else:
                is_fixed = True
        fixed_updates.append(update)
    two_sum = 0
    for update in fixed_updates:
        mid = math.floor(len(update)/2)
        two_sum += update[mid]
    print(f"Part two: {two_sum}")

def main():
    rules, updates = parse_input()
    part_one(rules, updates)
    part_two(rules, updates)

if __name__ == "__main__":
    main()
