def factorial(number):
    result = number
    for i in range(number -1,0,-1):
        result = result * i
    return result

def factorial_super_duper(number):
    return 1 if number == 0 else number * factorial_super_duper(number -1)

def factorial_generator_descending(n):
    result = n
    for i in range(n -1, 1, -1):
        result *= i
        yield result

def create_fibonacci(series_length):
    result = [0,1]
    while len(result) < series_length:
        result.append(result[-1] + result[-2])
    return result

def fibonacci_generator(series_length):
    a, b = 0,1

    for _ in range(0, series_length):
        yield a
        a, b = b, a + b
        


