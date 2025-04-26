def singleNumber(nums: list[int]) -> int:
    set_nums = set()
    expected = 0
    for num in nums:
        if num not in set_nums:
            set_nums.add(num)
            expected += num * 2
    
    return expected - sum(nums)





def main():
    A = [4,-1,2,-1,2,3,3,-7,-7]
    print(singleNumber(A))

main()