def search(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1 

        return -1


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid - 1

    return -1



def main():
    nums = [5,1,3]
    #[7,8,9,10,11,12,13,14,15,1,2,3,4,5,6]
    target = 3
    print(search(nums, target))

main()