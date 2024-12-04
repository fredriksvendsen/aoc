def parse_input():
    with open("4_input.txt", "r") as f:
        output = []
        for line in f.readlines():
            line_output = []
            for char in line:
                line_output.append(char)
            output.append(line_output)
        return output

def count_xmas(input):
    counter = 0
    h = len(input)
    w = len(input[0])
    for i in range(h):
        for j in range(w):
            if input[i][j] != "X":
                continue
            # Check if normal XMAS
            if j+3 < w and input[i][j+1] == "M" and input[i][j+2] == "A" and input[i][j+3] == "S":
                counter += 1
            # Check if backwards
            if j-3 >= 0 and input[i][j-1] == "M" and input[i][j-2] == "A" and input[i][j-3] == "S":
                counter += 1
            # Check if upwards
            if i-3 >= 0 and input[i-1][j] == "M" and input[i-2][j] == "A" and input[i-3][j] == "S":
                counter += 1
            # Check if downwards
            if i+3 < h and input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
                counter += 1
            # Check if nw
            if i-3 >= 0 and j-3 >= 0 and input[i-1][j-1] == "M" and input[i-2][j-2] == "A" and input[i-3][j-3] == "S":
                counter += 1
            # Check if ne
            if i-3 >= 0 and j+3 < w and input[i-1][j+1] == "M" and input[i-2][j+2] == "A" and input[i-3][j+3] == "S":
                counter += 1
            # Chcek if sw
            if i+3 < h and j-3 >= 0 and input[i+1][j-1] == "M" and input[i+2][j-2] == "A" and input[i+3][j-3] == "S":
                counter += 1
            # Check if se
            if i+3 < h and j+3 < w and input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
                counter += 1
    return counter

def count_x_mas(input):
    counter = 0
    h = len(input)
    w = len(input[0])
    for i in range(1, h-1):
        for j in range(w):
            if input[i][j] != "A":
                continue
            # Check if mas/sam from nw to se
            if i-1 >= 0 and i+1 < h and j-1 >= 0 and j+1 < w:
                nw = input[i-1][j-1]
                se = input[i+1][j+1]
                if (nw == "M" and se == "S") or (nw == "S" and se == "M"):
                    ne = input[i-1][j+1]
                    sw = input[i+1][j-1]
                    if (ne == "M" and sw == "S") or (ne == "S" and sw == "M"):
                        counter += 1
    return counter

def main():
    input = parse_input()
    count = count_xmas(input)
    print(count)
    count_x = count_x_mas(input)
    print(count_x)

if __name__ == "__main__":
    main()
