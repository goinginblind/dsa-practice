def threeSum(nums: list[int]) -> list[list[int]]:
    # Sort the array
    nums.sort()
    return_list = []

    for index, target in enumerate(nums):
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        left = index + 1
        right = len(nums) - 1   
        
        while left < right:
            total = target + nums[left] + nums[right]

            if total == 0:
                return_list.append([target, nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return return_list

    


def main():
    arr = [-1,0,1,2,-1,-4] #[3, -1, -7, 2, 4, -2, 0, 1, -3, 5]
    print(sorted(arr))
    print(threeSum(arr))
    # [-7, -3, -2, -1, 0, 1, 2, 3, 4, 5]


main()