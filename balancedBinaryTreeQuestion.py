class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def height(root):

    if root is None:
        return False
    return max(height(root.left), height(root.right)) + 1

def isBalanced(self, root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <= 1) and self.isBalanced(
            root.left) is True and self.isBalanced(root.right) is True:
        return True

    return False
