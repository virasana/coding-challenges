def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring[0] in vowels:
                kevin += 1
            else:
                stuart += 1
        
    if kevin == stuart:
        print("Draw")
    else:
        print("Kevin" if kevin > stuart else "Stuart", max(kevin, stuart))


if __name__ == "__main__":
    minion_game("BANANA")

