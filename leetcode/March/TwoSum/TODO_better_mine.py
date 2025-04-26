def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if nums[i] in numMap.keys():
            return
        numMap[nums[i]] = i

