from utils import read_input

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
left.sort()
right.sort()
distance = sum([abs(x - y) for x, y in zip(left, right)])
print(distance) # solution: 2086478 