def search(nums: list[int], target: int) -> int:
    if len(nums) == 1 and nums[0] == target:
        return 0
    low = 0
    high = len(nums) - 1

    while high >= low:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid - 1
    return -1


def main():
    arr = [-1]
    print(search(arr, -1))


main()