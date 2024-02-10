from itertools import permutations

# input_string = input().split()
S = "HACK"
k = 2

for p in permutations(sorted(S), k):
    print(''.join(p))