class Solution:
    def closing(self, current_open: str, check_val: str) -> bool:
        if current_open == "(" and check_val == ")":
            return True
        if current_open == "[" and check_val == "]":
            return True
        return current_open == "{" and check_val == "}"

    def isValid(self, s: str) -> bool:
        opened = ""
        for i in s:
            if i in "([{":
                opened += i
            elif opened and self.closing(opened[-1], i):
                opened = opened[:-1]

            else:
                return False
        return opened == ""
