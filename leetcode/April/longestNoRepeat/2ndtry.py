def lengthOfLongestSubstring(s: str) -> int:
    # 0. Create a set of 'seen' chars and max sequence len. 
    seen, max_seq = {}, 0
    # Create a hashMap 'char: it's last position'
    window_left = 0

    # 1. Scan the string from beggining
    for window_right, char in enumerate(s):

        # 1.1. Add non repeating chars into 'seen'
        if char not in seen:
            seen[char] = window_right

        # 1.2. If char repeats
        elif char in seen:
            # If repeat is inside the window, move left window border to the right 1 pos, 
            # so previous occurance is outside the window
            # Update latest repeat for such character
            if seen[char] >= window_left:
                window_left = seen[char] + 1
                seen[char] = window_right
            # It can be a repeat that's not in the window, then just update position
            else:
                seen[char] = window_right
            
        # 1.3. Update max sequence
        curr_seq = window_right - window_left + 1
        max_seq = max(max_seq, curr_seq)

    return max_seq

            

def main():
    s = 'dvdf'
    print(lengthOfLongestSubstring(s))

main()