def searchRange(nums: list[int], target: int) -> list[int]:
    low = 0
    high = len(nums) - 1

    # While the division in 2 is possible
    while low <= high:
        mid = (low + high) // 2

        # If target found
        if nums[mid] == target:
            # Define lower and higher range
            lower_bound = higher_bound = mid
            
            # While lower bound is in lists bounds and equal to target, lower the bound
            while lower_bound != 0 and nums[lower_bound - 1] == nums[mid]:
                lower_bound -= 1
            
            # While higher bound is in lists bounds and equal to target, increase the bound
            while higher_bound != len(nums) - 1 and nums[higher_bound + 1] == nums[mid]:
                higher_bound += 1

            return [lower_bound, higher_bound]

        # If target is greater then the number we've found
        elif nums[mid] < target:
            low = mid + 1

        # Fi target is lesser than the number we've found
        elif nums[mid] > target:
            high = mid - 1
        
    return [-1, -1]






def main():
    nums, target = [6,6,7,7,8,8,8,8], 5
    print(searchRange(nums, target))


main()

