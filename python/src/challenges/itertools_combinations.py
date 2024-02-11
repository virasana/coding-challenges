from itertools import combinations

S, k = ["HACK", "2"]

for i in range(1, int(k) + 1):
    for c in [''.join(c) for c in combinations(sorted(S), i)]:
        print(c)
