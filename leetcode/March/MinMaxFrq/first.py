# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. 
# In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.

def maxFrequency(nums: list[int], k: int) -> int:
    numsMap = {}
    greatest_num = 0
    k_dupe = k
    for i in range(len(nums)):
        if nums[i] > greatest_num:
            greatest_num = nums[i]
        numsMap[nums[i]] = greatest_num



def main():
    print(maxFrequency([1,2,4], 5))

main()


