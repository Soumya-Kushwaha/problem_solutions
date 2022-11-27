class Solution:
    def preorder(self, root: "Node") -> list[int]:
        res = []
        stack = [root]
        while stack:
            if node := stack.pop():
                res.append(node.val)
                stack.extend(reversed(node.children))

        return res
