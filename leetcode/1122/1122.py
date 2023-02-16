class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else x * 1000)
