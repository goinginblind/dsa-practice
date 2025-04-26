# No counter used

def isAnagram(s: str, t: str) -> bool:
    stringMapS, stringMapT = {}, {}
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        stringMapS[i] = 1 + stringMapS.get([i], 0)
        stringMapT[i] = 1 + stringMapT.get([i], 0)

    for j in stringMapS:
        if stringMapS[j] != stringMapT.get(j, 0):
            return False
        
    return True