def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []
    return_set = set()
    i = 0
    k = 2
    while i < k:
        j = i + 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                return_set.add(tuple(sorted([nums[i], nums[j], nums[k]])))
            j += 1
        
        if k < len(nums) - 1:
            k += 1
        elif k == len(nums) - 1:
            i += 1

    return_list = []
    for item in return_set:
        return_list.append(list(item))

    return return_list
    


            

def main():
    nums = [-1,0,1,0]
    print(threeSum(nums))


main()