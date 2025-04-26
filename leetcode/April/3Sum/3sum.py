def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []
    
    i = 0
    j = 1
    k = len(nums) - 1
    return_arr = []
    even = True

    while k - i > 1:
        if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]]:
            return_arr.append()
        
        if k - j == 1:
            if even:
                k -= 1
                j = i + 1
                even = False
            else:
                i += 1
                j = i + 1
                even = True
            continue
        
        j += 1

    return return_arr


def main():
    nums = [3, -1, -2, 2, 3, 6, 7, 0, -7, 2, 4, -2, 0, 1, -3, 5]
    print(threeSum(nums))


main()