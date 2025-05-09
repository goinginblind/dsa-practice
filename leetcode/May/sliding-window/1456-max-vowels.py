# s = "abciiidef", k = 3
def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    max_vowels = current_vowels = sum(1 for char in s[:k] if char in vowels)

    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        
        if s[i-k] in vowels:
            current_vowels -= 1

        max_vowels =max(max_vowels, current_vowels)

        if max_vowels == k:
            return max_vowels

    return max_vowels


def main():
    s = "leetcode"
    k = 3
    print(maxVowels(s, k))


main()


