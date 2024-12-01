from utils import read_input

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
similarity = 0
for idx, n in enumerate(left):
    similarity += right.count(n)*n

print(similarity) # solution: 24941624