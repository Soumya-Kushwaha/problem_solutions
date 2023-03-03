class Solution:
    def searchRange(self, nums: list[int], t: int) -> list[int]:
        return (
            [nums.index(t), len(nums) - 1 - nums[::-1].index(t)]
            if t in nums
            else [-1, -1]
        )
