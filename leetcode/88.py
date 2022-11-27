class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
