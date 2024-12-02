
def get_input_lists():
    with open("input.txt", "r") as f:
        l1 = []
        l2 = []
        for line in f.readlines():
            n1, n2 = line.split("   ")
            l1.append(int(n1))
            l2.append(int(n2))
        return l1, l2

def main():
    l1, l2 = get_input_lists()
    l1 = sorted(l1)
    l2 = sorted(l2)
    distance = 0
    for n1, n2 in zip(l1, l2):
        distance += abs(n2 - n1)
    print(f"Part 1 result: {distance}")
    sim_dict = {}
    for n in l2:
        sim_dict[n] = sim_dict.get(n, 0) + 1
    sim_score = 0
    for n in l1:
        sim_score += n * sim_dict.get(n, 0)
    print(f"Result part 2: {sim_score}")

if __name__ == "__main__":
    main()
