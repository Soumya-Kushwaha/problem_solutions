class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = res = nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            res = max(current, res)
        return res
