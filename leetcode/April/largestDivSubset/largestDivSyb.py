# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.


def largestDivisibleSubset(nums: list[int]) -> list[int]:
    # Check if len of nums is 1:
        # Return nums if yes
    if len(nums) == 1:
        return nums
    
    # Setup all the variables needed: max_length, current_length, current_sub_start, current_sub_ind (=i?)
    max_length, current_length, current_sub_start = 1, 1, 0
    index_map = {'current_start': 0, 'current_end': 0, 'max_start': 0, 'max_end': 0}
    # Start loop for i in range 1, len nums
    for i in range(1, len(nums)):
        # If previous number is divisible by the previous one:
        if nums[i] % nums[i - 1] == 0:
            # Increse current_subset end index (actually not needed)
            # Increase current subset length by 1
            current_length += 1
            # update max_length
            max_length = max(max_length, current_length)

        # Else:
        else:
            # Start new subset at index i
            current_length = 1
            # New starting index
            current_sub_start = i
    
    return max_length

        






def main():
    A = [1, 2, 8, 9, 27, 81, 162]
    print(largestDivisibleSubset(A))

main()