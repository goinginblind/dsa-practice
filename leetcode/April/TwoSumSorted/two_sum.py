def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        
        elif numbers[left] + numbers[right] < target:
            left += 1

        elif numbers[left] + numbers[right] > target:
            right -= 1
        


def main():
    arr = [2,7,11,15,18,20,30,43]
    target = 18
    print(twoSum(arr, target))


main()