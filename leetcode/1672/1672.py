class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(f) for f in accounts)
