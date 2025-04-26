# Input: pattern = "abba", s = "dog cat cat dog"
# 
# Output: true
# 
# Explanation:
# 
# The bijection can be established as:
# 
# 'a' maps to "dog".
# 'b' maps to "cat".
def wordPattern(pattern: str, s: str) -> bool:
    pattern_listed = list(pattern)
    s_listed = s.split(' ')
    
    return len(pattern) == len(s_listed) and len(set(zip(pattern_listed, s_listed))) == len(set(pattern_listed)) == len(set(s_listed))


def main():
    print(wordPattern('abba', 'dog cat dog cat'))


if __name__ == '__main__':
    main()
        