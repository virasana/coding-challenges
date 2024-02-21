from functools import reduce

  
append_fib = lambda x, _: x + [x[-1] + x[-2]]

# using functools.reduce
def get_fib_1(n):
    if n < 0:
        raise IndexError
    fib = [0,1]
    if n < 2:
        return fib[:n]
    return reduce(append_fib, range(n-2), fib)

#using simple implementation
def get_fib(n):
    if n < 0:
        raise IndexError
    fib = [0,1]
    if n < 2:
        return fib[:n]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i -2])
    return fib

if __name__ == '__main__':
    print(get_fib_1(5))
