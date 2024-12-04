def read_input(input_file="input.txt"):
    with open(input_file, "r") as f:
        return [[int(num) for num in line.split()] for line in f]

if __name__ == "__main__":
    print(read_input())