import itertools, math
from itertools import combinations

def get_probability(N, letters, K):
    combinations = itertools.combinations(''.join(letters.split()), K)
    num_a = sum('a' in combination for combination in combinations)
    total_combinations = math.comb(N, K)
    result = num_a / total_combinations
    return result

N = 4
letters = 'a a c d'
K = 2

if __name__ == '__main__':
    result = get_probability(N, letters, K)
    print(f'{result:.4f}')


