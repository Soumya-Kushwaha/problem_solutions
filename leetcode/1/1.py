class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for ind, i in enumerate(nums):
            rem = target - i
            if i in d:
                return [ind, d[i]]
            d[rem] = ind
