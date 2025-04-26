class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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