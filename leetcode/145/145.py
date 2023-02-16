# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = [root]
        while stack:
            if node := stack.pop():
                res.append(node.val)
                stack.extend((node.left, node.right))
        return res[::-1]
