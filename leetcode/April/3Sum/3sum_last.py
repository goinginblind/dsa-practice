def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []
    sorted_arr = sorted(nums)
    i = 0
    k = len(nums) - 1
    return_arr = []

    while i < k + 1:
        j = k - 1

        target = (sorted_arr[i] + sorted_arr[k]) * -1
        if target > sorted_arr[k]:
            i += 1
            k = len(nums) - 1
            continue

        while j > i:
            if sorted_arr[j] == target:
                return_arr.append([sorted_arr[i], sorted_arr[j], sorted_arr[k]])
                break
            j -= 1
        
        k -= 1

    return return_arr
            

def main():
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))


main()