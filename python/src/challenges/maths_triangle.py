def triangle(x):
    result = sum([x * 10**i for i in range(0, x)])
    return result

N = 5
print(sum([N * 10**i for i in range(0, N)]))

