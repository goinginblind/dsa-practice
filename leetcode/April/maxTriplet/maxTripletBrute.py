def maximumTripletValue(nums: list[int]) -> int:
# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 
    
    total_starting = (nums[0] - nums[1]) * nums[2]
    minMaxMap = {'max_total': total_starting}
    
    # Handles min len of numbers
    for i in range(2, len(nums)):
        for j in range(1,i):
            for k in range(0,j):
                if (nums[k] - nums[j]) * nums[i] >= minMaxMap['max_total']:
                    minMaxMap['max_total'] = (nums[k] - nums[j]) * nums[i]


    if minMaxMap['max_total'] <= 0:
        return 0
    else:
        return minMaxMap['max_total']
            

def main():
    print(maximumTripletValue([1,2,3]))

main()

