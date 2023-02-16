class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        l = len(nums)
        return sum(nums[i] == nums[j] for i in range(l) for j in range(i + 1, l))
