# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_seq = 0
    current_seq = 0
    for num in nums:
        if num == 1:
            current_seq += 1
            max_seq = max(current_seq, max_seq)
        else:
            current_seq = 0
    
    return max_seq
        

def main():
    arr = [1,1,1,1,0,1,1]
    print(findMaxConsecutiveOnes(arr))


main()