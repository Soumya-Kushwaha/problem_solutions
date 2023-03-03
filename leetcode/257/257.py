class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = [
            f"{str(root.val)}->{path}" for path in self.binaryTreePaths(root.left)
        ]

        result += [
            f"{str(root.val)}->{path}" for path in self.binaryTreePaths(root.right)
        ]

        return result or [str(root.val)]
