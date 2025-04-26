# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Create a map, that has a frequency, key is the frequency, while values are sets of numbers
    updateMap = {}
    mainMap = {1: set()}
    # Loop through all of the nums, each num should:
    for num in nums:
        # If its the first time of such num, add it to the set in frequency 1
        if num not in updateMap:
            updateMap[num] = 1
            mainMap[1].add(num)    
        # Else, add to set of its frequency, removed from the set of previous frequency
        else:
            mainMap[updateMap[num]].remove(num)
            updateMap[num] += 1
            mainMap.setdefault(updateMap[num], set()).add(num)
    # Return the values of the last k entries of the frequency map
    return_list = []
    counter_pop = k
    last_index = -1
    while counter_pop > 0:
        kaka = list(mainMap.items())[last_index]
        while 0 < len(kaka[1]) and counter_pop > 0:
            return_list.append(kaka[1].pop())
            counter_pop -= 1
        last_index -= 1

    return return_list


def main():
    numbers = [4,1,-1,2,-1,2,3]
    x = 3
    print(topKFrequent(numbers, x))

main()