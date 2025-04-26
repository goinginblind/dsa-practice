# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.


# Я думал только последовательных, но как оказалось они на любых местах nums могут быть
def largestDivisibleSubset(nums: list[int]) -> list[int]:
    # Check if len of nums is 1:
        # Return nums if yes
    if len(nums) == 1:
        return nums
    
    # Setup all the variables needed: max_length, current_length, current_sub_start, current_sub_ind (=i?)
    current_start, current_end, max_start, max_end = 0, 0, 0, 0

    # Start loop for i in range 1, len nums
    for i in range(1, len(nums)):
        # If previous number is divisible by the previous one:
        if nums[i] % nums[i - 1] == 0 or nums[i - 1] % nums[i] == 0:
            # Update 'current_end' index
            current_end += 1
            # Update max indexes, if the difference between max_end - max_start - current_end - current_start
            if current_end - current_start > max_end - max_start:
                max_start, max_end = current_start, current_end

        # Else:
        else:
            current_start, current_end = i, i
    
    return nums[max_start:max_end + 1]

def main():
    A = [2,3,4,8]  # Должен быть [2, 4, 8]
    print(largestDivisibleSubset(A))

main()