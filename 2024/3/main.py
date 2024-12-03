import re

def parse_input():
    with open("3_input.txt", "r") as f:
        return f.read()

def filter_mul(input):
    matches = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))", input)
    return matches

def filter_mul_conditionals(input):
    matches = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))", input)
    return matches

def filter_num_comma_conditionals(input):
    output = []
    is_active = True
    for mul in input:
        if mul == "do()":
            is_active = True
        elif mul == "don't()":
            is_active = False
        else:
            if not is_active:
                continue
            mul = mul.replace("mul(", "")
            mul = mul.replace(")", "")
            n1, n2 = mul.split(",")
            output.append([int(n1), int(n2)])
    return output

def filter_num_comma(input):
    output = []
    for mul in input:
       mul = mul.replace("mul(", "")
       mul = mul.replace(")", "")
       n1, n2 = mul.split(",")
       output.append([int(n1), int(n2)])
    return output

def multiply(pairs):
    product = 0
    for pair in pairs:
        product += pair[0]*pair[1]
    return product

def main():
    input = parse_input()
    filtered = filter_mul(input)
    num_pairs = filter_num_comma(filtered)
    multiplied = multiply(num_pairs)
    print(f"Part 1: {multiplied}")
    # Part 2
    filtered_c = filter_mul_conditionals(input)
    num_pairs_c = filter_num_comma_conditionals(filtered_c)
    multiplied_c = multiply(num_pairs_c)
    print(f"Part 2: {multiplied_c}")

if __name__ == "__main__":
    main()
