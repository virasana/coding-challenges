def find_runner_up(arr):
    seen = set()
    unique_values = [x for x in arr if x not in seen and not seen.add(x)]
    sorted_array = sorted(unique_values)
    result = sorted_array[len(sorted_array) - 2]
    return result

if __name__ == '__main__':
    input = '2 3 6 6 5'
    arr = map(int, input.split())
    print(find_runner_up(arr))
