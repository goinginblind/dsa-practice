# Input: nums = [2,20,4,10,3,4,5]
# 
# Output: 4

# This one DOES NOT PASS LEETCODE CHECK, time limit exceeded
def longestConsecutive(nums: list) -> int:
    # Check if nums len is 0 or 1
    if len(nums) <= 1:
        return len(nums)
    # Set max seq as 1, since it's at least one always, same for current
    max_sequence = 1
    current_sequence = 1
    # Sort the whole array
    nums_sorted = sorted(nums)
    # Loop through it once
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1] + 1:
            current_sequence += 1
        else:
            if max_sequence <= current_sequence:
                max_sequence = current_sequence
            current_sequence = 1