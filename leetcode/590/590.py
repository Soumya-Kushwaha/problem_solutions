"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> list[int]:
        res = []
        stack = [root]
        while stack:
            if node := stack.pop():
                res.append(node.val)
                stack.extend(node.children)

        return res[::-1]
