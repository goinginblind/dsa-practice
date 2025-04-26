# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.



def missingNumber(nums: list[int]) -> int:
    if len(nums) % 2 == 0:
        expected = len(nums) * len(nums) // 2 + len(nums) // 2
    else:
        expected = len(nums) * (len(nums) // 2 + 1)

    actual = sum(nums)

    return expected - actual
    
    


def main():
    arr = [1]
    print(missingNumber(arr))


main()