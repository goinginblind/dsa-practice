# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
import math
def productExceptSelf(nums: list[int]) -> list[int]:
    # Hash the numbers: keys are indices, values are the numbers
    productHash = {'prod': 1}
    numbersHash = {}
    resultList = []
    oneZeroFlag = False
    zeroIndex = None
    for i, n in enumerate(nums):
        if n == 0 and not oneZeroFlag:
            oneZeroFlag = True
            numbersHash[i] = n
            zeroIndex = i
            continue
        if n == 0 and oneZeroFlag:
            # So a second zero, so all the products are 0s:
            return [0] * len(nums)

        productHash['prod'] =  n * productHash['prod']
        numbersHash[i] = n
    
    for j in numbersHash:
        if oneZeroFlag and j != zeroIndex:
            resultList.append(0)
        elif oneZeroFlag and j == zeroIndex:
            resultList.append(productHash['prod'])
        else:
            resultList.append(productHash['prod'] // numbersHash[j])

    return resultList
    
        
def main():
    print(productExceptSelf([1,2,4,6]))
    
main()

