import time

def minion_game_slow(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            print(substring)
            if substring[0] in vowels:
                kevin += 1
            else:
                stuart += 1
        
    score = get_score(stuart, kevin)
    print(score)
    return score


def minion_game_fast(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    score = ""

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    
    score = get_score(stuart, kevin)
    print(score)
    return score

def get_score(stuart, kevin):
    if kevin == stuart:
        score = "Draw"
    else:
        score = f'{"Kevin:" if kevin > stuart else "Stuart:"} {str(max(kevin, stuart))}'
    return score

if __name__ == "__main__":
    input = "BANANA" * 50
    time_start = time.time()    
    minion_game_slow(input)
    time_end = time.time()
    slow = time_end - time_start
    print(f'minion_game_slow took {slow}')

    time_start = time.time()    
    minion_game_fast(input)
    time_end = time.time()
    fast = time_end - time_start
    print(f'minion_game_fast took {fast}')

    if fast < slow:
        print(f'minion_game_{"fast" if fast < slow else "slow"} is quicker by ', f'{max(fast, slow) / min(fast, slow) * 100:.2f}', "percent")
    

