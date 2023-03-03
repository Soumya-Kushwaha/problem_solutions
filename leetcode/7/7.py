class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = int(str(x)[1:][::-1])
            return 0 if num > 2147483648 else -num
        else:
            num = int(str(x)[::-1])
            return 0 if num > 2147483648 else num
