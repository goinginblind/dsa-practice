from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_freq = 0
    max_window_size = 1
    counter = defaultdict(int)
    for right in range(0, len(s)):
        counter[s[right]] += 1
        max_freq = max(max_freq, counter[s[right]])

        if (right - left + 1) - max_freq > k:
            counter[s[left]] -= 1
            left += 1

        max_window_size = max(max_window_size, right - left + 1)

    return max_window_size

def main():
    string = 'AAKACBA'
    x = 2
    print(characterReplacement(string, x))

main()