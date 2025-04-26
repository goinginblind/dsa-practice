# Input: 
# nums = [3,4,5,6], target = 7
# 
# Output: [0,1]


def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}
    for i, n in enumerate(nums):
        if target - n in prevMap:
            return prevMap[target - n], i
        prevMap[n] = i    

def main():
    print(twoSum([3,3,4,5,6], 6))

main()