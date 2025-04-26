# Input:
#  1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output:
#  1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

def moveZeros(nums: list[int]) -> list[int]:
    current_index, zero_count = 0, 0
    while current_index < len(nums) - 1 - zero_count:
        if nums[current_index] == 0:
            del nums[current_index]
            nums.append(0)
            zero_count += 1
            current_index -= 1
            if current_index < 0:
                current_index = 0
            continue
        current_index += 1
    return nums 
            



def main():
    arr = [1, 2, 0, 4, 2, 9, 0, 2]
    print(moveZeros(arr))

main()