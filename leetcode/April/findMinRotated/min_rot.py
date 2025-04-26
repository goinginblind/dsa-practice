def findMin(nums: list[int]) -> int:
    # If array is rotated for len(nums) (not rotated basically)
    if nums[0] < nums[-1]:
        return nums[0]

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[-1]:
            left = mid + 1
        
        elif nums[mid] < nums[-1]:
            right = mid
        
    return nums[right]

        



def main():
    nums = [30, 40, 50, 10, 20]
    print(findMin(nums))


main()