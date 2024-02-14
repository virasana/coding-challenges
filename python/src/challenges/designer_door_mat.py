def get_design(margin, N, M, expected):
    design = []
    num_lines = (N -1) // 2
    char = '.|.'
    body = {}
    for i in range(1, num_lines + 1):
        middle = (2 * i -1) * char
        body[i] = center(middle, M)
        assert(body[i] == expected[i -1])
        body[N + 1 - i] = center(middle, M)
        assert(body[N + 1 - i] == expected[N - i])
    body[num_lines + 1] = (center('WELCOME', M))

    return '\n'.join(body[key] for key in sorted(body.keys()))

def center(string, M):
    return '    ' + string.center(M, '-')

if __name__ == '__main__':
    expected = """\
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------\
"""

    N = 7
    M = N * 3
    margin = '    '

    actual = get_design(margin, N, M, expected.split('\n'))
    print(actual)
    print()
    print(expected)
    print()

    actual = actual.split('\n')
    expected = expected.split('\n')

    for i in range(0, len(expected)):
        print(f'{i}: {actual[i] == expected[i]}')

    print(actual == expected)

