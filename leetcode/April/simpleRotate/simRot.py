# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


def rotate(nums: list[int], k: int) -> None:
    if len(nums) == 1 or k == 0:
        return nums
    
    if k > len(nums): 
        k = k % len(nums) 

    key = len(nums) - k
    
    formerHalf = nums[0:key]
    latterHalf = nums[key:]
    nums.clear()
    nums.extend(latterHalf + formerHalf)


def main():
    arr = [1,2,3,4,5,6]
    rotate(arr, 8)
    print(arr)


if __name__ == '__main__':
    main()