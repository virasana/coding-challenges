from collections import namedtuple

def get_average_mark(input):
    N, columns, data = int(input[0]), input[1], input[2:]

    if data is None or N == 0 or len(data) == 0:
        raise(ValueError('get_average_mark requires at least one row of data'))
    
    Row = namedtuple('Row', columns.split())
    return sum(int((Row(*row.split())).MARKS) for row in data)/N 
    
input = """\
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6\
""".split('\n')
# N, columns, data = input[0], input[1], input[2:]
# Row = namedtuple('Row', columns.split())
# results = [float((Row(*datum.split()).MARKS)) for datum in data]
# print(results)
# average = sum(float((Row(*datum.split()).MARKS)) for datum in data) / int(N)

print(get_average_mark(input))
