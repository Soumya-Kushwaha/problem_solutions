class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(f ** 2 for f in nums)
