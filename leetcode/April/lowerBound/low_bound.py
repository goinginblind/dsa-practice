def findFloor(nums, floor):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2

        # In case we encounter floor
        if nums[mid] == floor and mid != len(nums) - 1:
            while nums[mid] == nums[mid + 1]:
                mid += 1
            return mid
        
        elif nums[mid] == floor and mid == len(nums) - 1:
            return mid
        
        elif nums[mid] > floor:
            high = mid - 1

        elif nums[mid] < floor:
            low = mid + 1

    if nums[mid] < floor:
        return mid
    else:
        return mid - 1


def main():
    arr = [8, 18, 26, 28, 32, 35, 37, 38, 42, 47, 49, 51, 51, 67, 80]
    x = 80
    print(findFloor(arr, x))


main()