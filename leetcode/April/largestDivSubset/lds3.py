# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.


def largestDivisibleSubset(nums: list[int]) -> list[int]:
    # Check if nums len is 1:
        # Return nums if yes

    # For i in range of nums:
    ...
    # The first num, we add it to a set numbered [i]
        # If the next num is divisible by first (or the other way around):
            # Add it to the set, continue
        
        # If 

def main():
    A = [2,3,4,8]  # Должен быть [2, 4, 8]
    print(largestDivisibleSubset(A))

main()