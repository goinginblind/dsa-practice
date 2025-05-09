import random
# Notice how this is O(n), not O(n*k)
def findMaxAverage(nums: list[int], k: int) -> float:
    left, right = 0, k - 1
    window = sum(nums[:k])
    result = window / k
    
    while right < len(nums) - 1:
        window -= nums[left]
        left += 1
        right += 1
        window += nums[right]

        result = max(window / k, result)
        
    return round(result, 5)


def main():
    random_list = [random.randint(1, 10) for _ in range(20)]
    k = random.randint(1, 16)
    print(findMaxAverage([1,12,-5,-6,50,3], 6))

main()