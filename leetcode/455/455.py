class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        r = 0
        heapq.heapify(s)
        heapq.heapify(g)
        while s and g:
            a = heapq.heappop(g)
            while s:
                if a <= heapq.heappop(s):
                    r += 1
                    break

        return r
