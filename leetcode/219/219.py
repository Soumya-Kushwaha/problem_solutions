class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i, val in enumerate(nums):
            if val in d and i - d[val] <= k:
                return True
            d[val] = i

        return False
