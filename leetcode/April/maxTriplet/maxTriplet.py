def maximumTripletValue(nums: list[int]) -> int:
# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 
    
    total_starting = (nums[0] - nums[1]) * nums[2]
    minMaxMap = {'a': nums[0], 'index_a': 0,
                'b': nums[1], 'index_b': 1,
                'c': nums[2], 'index_c': 2,
                'max_total': total_starting
                }
    
    # Handles min len of numbers
    if len(nums) == 3: 
        if total_starting < 0:
            return 0
        else:
            return total_starting
    
    for i in range(2, len(nums)):
        if nums[i] >= minMaxMap['c']:
            minMaxMap['c'] = nums[i]
            minMaxMap['index_c'] = i
    
    for j in range(1, len(nums[:minMaxMap['index_c']])):
        if nums[j] <= minMaxMap['b']:
            minMaxMap['b'] = nums[j]
            minMaxMap['index_b'] = j
    
    for q in range(0, len(nums[:minMaxMap['index_b']])):
        if nums[q] >= minMaxMap['a']:
            minMaxMap['a'] = nums[q]
            minMaxMap['index_a'] = q

    if total := (minMaxMap['a'] - minMaxMap['b']) * minMaxMap['c'] < 0:
        return 0
    else:
        return (minMaxMap['a'] - minMaxMap['b']) * minMaxMap['c']
            

def main():
    print(maximumTripletValue([8,6,3,13,2,12,19,5,19,6,10,11,9]))

main()

