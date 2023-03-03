class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return any(target in f for f in matrix)
