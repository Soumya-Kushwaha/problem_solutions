class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            res[i] = nums[nums[i]]

        return res
