class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [name for name, height in sorted(zip(names, heights), key=lambda x:-x[1])]
