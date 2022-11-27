class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        check = 0
        while check < len(min(strs, key=len)) and len({f[check] for f in strs}) == 1:
            res += strs[0][check]
            check += 1

        return res
