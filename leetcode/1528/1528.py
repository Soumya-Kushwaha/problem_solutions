class Solution:
    def restoreString(self, s: str, d: list[int]) -> str:
        (*a,) = s
        for i in range(len(s)):
            a[d[i]] = s[i]

        return "".join(a)
