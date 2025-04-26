def majorityElement(nums: list[int]) -> int:
    ...
    nums.sort()
    n = len(nums)
    return nums[n // 2]

def main():
    arr = [2,2,1,1,1,2,2]
    print(majorityElement(arr))


main()