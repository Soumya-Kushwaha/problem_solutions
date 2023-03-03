class Solution:
    def kidsWithCandies(self, candies: list[int], e: int) -> list[bool]:
        m = max(candies)
        return [f + e >= m for f in candies]
