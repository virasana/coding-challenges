def merge_the_tools(string, k):
    if not string or k == 0:
        return []
    
    string_length = len(string)
    substring_length = string_length // k
    substrings = [string[i: i + substring_length] for i in range(0, string_length, substring_length)]

    result = []
    for string in substrings:
        seen = set()
        # this line is worth inspecting closely for learning purposes
        result.append(''.join(ch for ch in string if ch not in seen and not seen.add(ch)))
    return result

if __name__ == '__main__':
    string = "AABCAAADA"
    k = 3
    output = merge_the_tools(string, k)
    print(output)