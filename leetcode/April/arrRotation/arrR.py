# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
# No rotation is ok too


def check(nums: list[int]) -> bool:
    # If length < 3, can always rotate
    if len(nums) in range(3):
        return True

    currentIndex = 1

    while nums[currentIndex - 1] <= nums[currentIndex]:
        if currentIndex == len(nums) - 1:
            return True
        currentIndex += 1

    if currentIndex < len(nums) - 1:
        currentIndex += 1
    elif currentIndex == len(nums) - 1 and nums[currentIndex] <= nums[0]:
        return True
    elif currentIndex == len(nums) - 1 and nums[currentIndex] > nums[0]:
        return False

    while nums[currentIndex] <= nums[0] and nums[currentIndex] >= nums[currentIndex - 1]:
        if currentIndex == len(nums) - 1:
            return True
        currentIndex += 1
    return False


def main():
    print(check([1,3,2]))


if __name__ == '__main__':
    main()