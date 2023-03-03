class Solution:
    def countBits(self, n: int) -> list[int]:
        return [f"{f:b}".count("1") for f in range(n + 1)]
