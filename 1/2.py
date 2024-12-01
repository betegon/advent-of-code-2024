from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(n*right_counts.get(n, 0) for n in left)
print(similarity) # solution: 24941624