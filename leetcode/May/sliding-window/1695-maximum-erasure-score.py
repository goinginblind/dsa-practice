def maximumUniqueSubarray(nums: list[int]) -> int:
    left = right = 0
    subarray = {nums[left]: left}
    result = window = nums[left]
    
    while right < len(nums) - 1:
        right += 1
        while nums[right] in subarray and left <= subarray[nums[right]]:
            window -= nums[left]
            del subarray[nums[left]]
            left += 1
        window += nums[right]
        subarray[nums[right]] = right
        result = max(window, result)
    
    return result

def main():
    arr = [4, 2, 1, 3, 2]
    print(maximumUniqueSubarray(arr))

main()