class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def solve(p: str, left: int, right: int, res: list[str] = []) -> list[str]:
            if left:
                solve(f"{p}(", left - 1, right)
            if right > left:
                solve(f"{p})", left, right - 1)
            if not right:
                res += (p,)
            return res

        return solve("", n, n)
