class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        import textwrap

        return [f"{f:{fill}<{k}}" for f in textwrap.wrap(s, k)]
