class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
