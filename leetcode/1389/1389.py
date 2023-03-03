class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        l = []
        for a, b in zip(nums, index):
            l.insert(b, a)
        return l
