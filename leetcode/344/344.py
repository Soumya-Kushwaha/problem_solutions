class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
