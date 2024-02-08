from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    fracs.append(Fraction(*map(int, '1 2'.split())))
    fracs.append(Fraction(*map(int, '3 4'.split())))
    fracs.append(Fraction(*map(int, '10 6'.split())))
    result = product(fracs)
    print(*result)