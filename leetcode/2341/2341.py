class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        d = collections.Counter(nums)
        a = b = 0
        for i in d.values():
            a += i % 2
            b += i // 2

        return b, a
