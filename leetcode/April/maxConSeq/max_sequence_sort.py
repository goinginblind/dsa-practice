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
        elif nums_sorted[i] == nums_sorted[i - 1]:
            continue
        else:
            max_sequence = max(max_sequence, current_sequence)
            current_sequence = 1

    return max(current_sequence, max_sequence)


def main():
    arr = [1,0,1,2]
    print(longestConsecutive(arr))


main()