class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSymmetric(self, root):

    if root is None:
        return True
    else:
        return self.pairCheck(root.left, root.right)


def pairCheck(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    if left.val == right.val:
        outerPair = self.pairCheck(left.left, right.right)
        innerPair = self.pairCheck(left.right, right.left)
        return outerPair and innerPair
    else:
        return False








#left > root> right (in-order)
#root > left > right (pre-order)
#left > right > root (post-order)


#       left
#left           right

#       right
#right          left





