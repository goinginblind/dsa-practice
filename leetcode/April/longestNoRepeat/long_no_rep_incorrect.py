def lengthOfLongestSubstring(s: str) -> int:
    # 0. Create a set of 'seen' chars, create a sequence meter and max sequence len
    seen, current_seq, max_seq = set(), 0, 0

    # 1. Scan the string from beggining
    for char in s:

        # 1.1. Add all characters to a set of seen chars
        if char not in seen:
            seen.add(char)
            current_seq += 1

        # 1.2. If current char is in the set: clear the set, add this one char to it, update max_seq
        # and set current sequence to 1
        else:
            seen.clear()
            seen.add(char)
            max_seq = max(max_seq, current_seq)
            current_seq = 1
    
    # 2. Return
    return max(max_seq, current_seq)
            

def main():
    s = 'dvabcdf'
    print(lengthOfLongestSubstring(s))

main()