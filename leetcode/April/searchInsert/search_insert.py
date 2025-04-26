# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be 
# if it were inserted in order. You must write an algorithm with O(log n) 
# runtime complexity.
def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
    if nums[mid] < target:
        return mid + 1
    elif nums[mid] > target:
        return mid


def main():
    arr = [1,3,5,6]
    print(searchInsert(arr, 4))

main()