
def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
    return []  # No solution found

def main():
    num_list = [1, 3, 5, 6, 7, 11, 13, 4, 3, 2, 1, 0 , 5]
    print(twoSum(num_list, 16))

main()