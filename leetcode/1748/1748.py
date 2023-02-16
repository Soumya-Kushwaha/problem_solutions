class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(v for v,c in collections.Counter(nums).items()if c == 1)
