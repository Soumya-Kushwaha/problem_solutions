class Solution:
    import functools

    @functools.cache
    def fib(self, n: int) -> int:
        return n if n in {0, 1} else self.fib(n - 1) + self.fib(n - 2)
