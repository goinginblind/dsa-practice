def longestConsecutive(nums: list) -> int:
    # Check if nums len is 0
    if not nums:
        return 0
    
    # Create a set
    num_set = set(nums)
    max_sequence = 0

    # Loop through it once
    for num in num_set:
        # Check if num is a sequence starter
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # While sequence holds
            while current_num + 1 in num_set:
                current_sequence += 1
                current_num += 1

            max_sequence = max(max_sequence, current_sequence)
        
    return max_sequence


def main():
    arr = [1,0,1,2]
    print(longestConsecutive(arr))


main()