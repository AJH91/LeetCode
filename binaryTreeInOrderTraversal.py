# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        elements = []
        S = Solution()

        if not root:
            return []

        if root.left:
            elements += S.inorderTraversal(root.left)
        elements.append(root.val)
        if root.right:
            elements += S.inorderTraversal(root.right)
        return elements