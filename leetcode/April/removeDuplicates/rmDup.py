#Input: nums = [0,0,1,1,1,2,2,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

def removeDuplicates(nums: list[int]) -> int:
    slow = 0
    temp_list = [nums[0]]
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            temp_list.append(nums[fast])
            slow = fast
    
    duplicates = ['_'] * (len(nums) - len(temp_list))
    k = len(temp_list)
    nums[:] = temp_list + duplicates
    print(nums)

def main():
    removeDuplicates([0,0,1,1,1,2,2,3,3,4])

main()
        
        
        
            