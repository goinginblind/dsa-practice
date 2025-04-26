def twoSum(nums: list[int], target: int) -> list[int]:
    hash_table = {}
    doubleFlag = False
    # We're loading all of the values from the list into the memory
    for i in nums:
        # If the number encountered for the first time,
        # put it in the hash table formatted like this {number: its difference to target}
        # i.e.: t = 9, number = 3, we have {3: 6}
        if i not in hash_table.keys():
            hash_table[i] = target - i
        # If difference is in keys (so encountered previously), return
        if target - i in hash_table.keys():
            if not doubleFlag and (2 * i == target):
                doubleFlag = True
            elif doubleFlag and (2 * i == target):
                indices = [j for j, x in enumerate(nums) if (x == i or x == target - i)]
                return indices
            else:
                return [nums.index(target - i), nums.index(i)]


def main():
    list_of_nums = [-12, 3, 12, 5, 16]
    print(twoSum(list_of_nums, -7))


main()