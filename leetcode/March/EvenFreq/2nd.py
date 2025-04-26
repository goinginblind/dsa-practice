def maxFrequency(nums: list[int]) -> list[int]:
    mp={}
    maxNum = 0
    max = 0
    for i in nums:
        if i % 2 != 0:
            continue

        if not mp:
            maxNum = i
            
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
        
        if mp[i] > max or (mp[i] == max and maxNum > i):
            maxNum = i
            max = mp[i]
    
    if max == 0:
        return -1
    else:
        return maxNum
    

def main():
    arr = [0,1,2,2,4,4,1]
    print(maxFrequency(arr))


main()