def get_rangoli(size):
    letters = [chr(n) for n in range(96 + size, 96, -1)]
    result = []
    padding = 2 * (len(letters) + len(letters) - 1)
    for line in range(size):
        current = ('-'.join(letters[0:line + 1]))
        if line > 0:
            current = current + '-' + current[::-1][2:]
        current = current.center(padding,'-')
        current = current[:-1]
        result.append(current)
    for line in result[::-1][1:]:
        result.append(line)
    return result
                
        

if __name__ == '__main__':
    n = 5
    rangoli = get_rangoli(n)
    print('\n'.join(rangoli))