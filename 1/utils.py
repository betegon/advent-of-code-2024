def read_input(input_file="input.txt"):
    output = []
    with open(input_file, "r") as f:
        for line in f:
            output.append(line.split())
    return output
if __name__ == "__main__":
    print(read_input())