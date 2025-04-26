from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    multisetS = Counter(list(s))
    multisetT = Counter(list(t))
    if multisetS != multisetT:
        return False
    return True

def main():
    print(isAnagram(s="bbcc", t="bcbc"))

main()