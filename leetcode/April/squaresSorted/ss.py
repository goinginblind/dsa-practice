def sortedSquares(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return [nums[0] ** 2]
    
    # Set flags for when the comparison needs to stop
    left_done = False
    right_done = False

    # Set a max index and left pointer
    max_index = len(nums) - 1
    left = 0

    # While left is not max and nums[left] is non positive
    while left < max_index and nums[left] < 0:
        left += 1
    
    # Set a right pointer
    if left != max_index:
        right = left + 1
    else:
        right_done = True

    result = []

    while not (left_done and right_done):
        if not left_done and (right_done or nums[left]**2 <= nums[right]**2):
            result.append(nums[left]**2)
            if left > 0:
                left -= 1
            else:
                left_done = True
        
        if not right_done and (left_done or nums[left]**2 > nums[right]**2):
            result.append(nums[right]**2)
            if right < max_index:
                right += 1
            else:
                right_done = True
    return result
    


def main():
    nums = [-5,-3,-2,-1, 0, 1, 9, 11, 12]
    print(sortedSquares(nums))

main()