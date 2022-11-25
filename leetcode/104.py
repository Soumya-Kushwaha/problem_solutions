# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deep(self, root: Optional[TreeNode], deep) -> int:
        return (
            max(self.deep(root.left, deep + 1), self.deep(root.right, deep + 1))
            if root
            else deep
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.deep(root, 0)
