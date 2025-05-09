# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
# 
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


def reverseVowels(s: str) -> str:
    left_ptr, right_ptr = 0, len(s) - 1
    string_list = list(s)
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    while left_ptr < right_ptr:
        while left_ptr < right_ptr and string_list[left_ptr] not in vowels:
            left_ptr += 1
        while right_ptr > left_ptr and string_list[right_ptr] not in vowels:
            right_ptr -= 1
        string_list[left_ptr], string_list[right_ptr] = string_list[right_ptr], string_list[left_ptr]
        left_ptr += 1
        right_ptr -= 1

    return ''.join(string_list)



def main():
    string = 'racecar'
    print(reverseVowels(string))


main()