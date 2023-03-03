class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return eval('|'.join(map(str,nums))) * 2 ** (len(nums) - 1)
