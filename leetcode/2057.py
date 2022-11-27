class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        return next((i for i in range(len(nums)) if i % 10 == nums[i]), -1)