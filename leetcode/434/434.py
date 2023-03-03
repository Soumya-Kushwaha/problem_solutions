class Solution:
    def countSegments(self, s: str) -> int:
        return s.count(" ") + 1 if s else 0
