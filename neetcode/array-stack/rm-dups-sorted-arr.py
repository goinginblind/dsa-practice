def removeDuplicates(nums: list[int]) -> int:
    k = 1
    for i in range(len(nums) - 1, 0, -1):
        if len(nums) == 1:
            break
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            k+=1
    return k


def main():
    nums=[1,1,2,3,4]
    print(removeDuplicates(nums))
    print(nums)


main()