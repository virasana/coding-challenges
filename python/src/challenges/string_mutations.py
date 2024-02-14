def mutate_string(string, position, character):
    result = list(string)
    result[position] = character
    result = ''.join(result)
    return result

if __name__ == '__main__':
    # s = input()
    # i, c = input().split()
    s = 'abracadabra'
    i, c = 5, 'k'
    s_new = mutate_string(s, int(i), c)
    print(s_new)