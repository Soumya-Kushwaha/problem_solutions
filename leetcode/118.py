class Solution:
    def generate(self, n: int) -> list[list[int]]:
        l = [[1]]
        l.extend(
            [
                1 if not f or f == i else l[-1][f] + l[-1][f - 1]
                for f in range(i + 1)
            ]
            for i in range(1, n)
        )

        return l
