# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
def maxFrequency(nums: list[int]) -> list[int]:
    # Hashing a frequency table key is NUMBER FROM ARRAY, value is its FREQUENCY
    frequencyTable = {}
    # Hashing a maximum frequency table
    maxFreq = {'rate': 0, 'num': -1}
    # Loop thru all the numbers from input array
    for i in range(len(nums)):
        # If not dividable by 2, skip
        if nums[i] % 2 != 0:
            continue
        # If number is encountered for the first time
        if nums[i] not in frequencyTable:
            # Set frequency to 1
            frequencyTable[nums[i]] = 1
            # If first number in the frequency table
            if maxFreq['num'] == -1:
                # Set it as max frequency with a rate of 1
                maxFreq['num'] = nums[i]
                maxFreq['rate'] = 1
        # If not the first number in the whole frequency table
        else:
            # Add one to its freqeuncy
            frequencyTable[nums[i]] += 1
            # If frequency is higher than Maximum Rate
            if frequencyTable[nums[i]] > maxFreq['rate']:
                # Set this number as the new maximum frequency
                maxFreq['num'] = nums[i]
                maxFreq['rate'] = frequencyTable[nums[i]]
        # If number < than maximum Frequency number and its frequency is the same as maximum, keep it as the maximum (ensures the return in
        # case of numbers mathing in frequency is still the highest frequency, but the smallest number)
        if nums[i] < maxFreq['num'] and frequencyTable[nums[i]] == maxFreq['rate']:
            maxFreq['num'] = nums[i]

    return maxFreq['num']


def main():
    array = [0,1,2,2,4,4,1]
    print(maxFrequency(array))
    

main()
