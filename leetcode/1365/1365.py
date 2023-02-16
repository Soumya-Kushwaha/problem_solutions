class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        k = sorted(nums)
        return [k.index(f) for f in nums]
