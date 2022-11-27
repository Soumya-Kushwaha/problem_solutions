# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = [root]
        while stack:
            if node := stack.pop():
                res.append(node.val)
                stack.extend((node.right, node.left))
        return res
