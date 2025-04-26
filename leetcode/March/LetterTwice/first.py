# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
# Note:
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.
# Input: s = "abccbaacz"; out: 'c'
def repeatedCharacter(s: str) -> str:
    # TODO: hash the string. While doing it, each hash value should be updated, first to hit 2 is gay
    strMap = {}

    for i in s:
        if i not in strMap.keys():
            strMap[i] = 1
        else:
            return i
        
def main():
    print(repeatedCharacter(''))

main()