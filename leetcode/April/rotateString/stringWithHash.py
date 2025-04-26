def rotateString(s: str, goal: str) -> bool:
    # Make a map {letter: set of indexes}
    char_map = {}
    for index, char in enumerate(s):
        if char not in char_map:
            char_map[char] = set()
        char_map[char].add(index)

    for j in range(len(s)):
        



        
    return False
    

def main():
    print(rotateString(s = "gcmbf", goal = "fgcmb"))

main()

