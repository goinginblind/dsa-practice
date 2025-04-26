# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order 
# of the characters can be different.

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagramHashIndex = {}
    outListIndexer = 0
    outList = []
    for i, n in enumerate(strs):
        anagram_word = ''.join(sorted(n))
        # As of now, we have: i - index, n - the word itself
        if anagram_word not in anagramHashIndex:
            anagramHashIndex[anagram_word] = outListIndexer
            outListIndexer += 1
            outList.append([n])
        else:
            indexForOut = anagramHashIndex[anagram_word]
            outList[indexForOut].insert(0, n)
    return(outList)

        
def main():
    input = ["act","pots","tops","cat","stop","hat"]
    print(groupAnagrams(input))


main()