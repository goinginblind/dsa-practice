# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# MCMXCIV = 1994

def romanToInt(s: str) -> int:
    charMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    lastChar = ''
    finalSum = 0

    for char in s:
        if char in charMap:
            if (char == 'V' or char == 'X') and lastChar == 'I':
                finalSum += charMap[char] - 2
            elif (char == 'L' or char == 'C') and lastChar == 'X':
                finalSum += charMap[char] - 20
            elif (char == 'D' or char == 'M') and lastChar == 'C':
                finalSum += charMap[char] - 200
            else:
                finalSum += charMap[char]
            lastChar = char
    return finalSum

def main():
    print(romanToInt('III'))

main()