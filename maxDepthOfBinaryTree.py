class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root):

        if root == None:
            return 0

        leftSide = self.maxDepth(root.left)
        rightSide = self.maxDepth(root.right)

        if leftSide > rightSide:
            return leftSide + 1
        else:
            return rightSide + 1



