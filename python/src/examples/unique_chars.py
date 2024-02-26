string = "ABBCDDEEFGHIJJJKLL"
k = 3
substrings = [string[i: i+k] for i in range(0, len(string), k)]

for substring in substrings:
    
    seen = set()
    # we use a trick - seen.add() always returns None, whether it is already there or not
    chars = ''.join(ch for ch in substring if ch not in seen and not seen.add(ch))
    print(chars)
    

