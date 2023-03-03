class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(all(f in allowed for f in word) for word in words)
