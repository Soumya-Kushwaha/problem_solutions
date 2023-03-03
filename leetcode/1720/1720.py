class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        res = [first]
        res.extend(i ^ res[-1] for i in encoded)
        return res
