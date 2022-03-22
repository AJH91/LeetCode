# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSameTree(p, q) -> bool:
                if p.val == q.val:
                    return True

                if p is None or q is None:
                    return False

                if p.val < q.val:
                    if p.left:
                        return p.left.isSameTree(q.val)
                    else:
                        return False

                if p.val > q.val:
                    if p.right:
                        return p.right.isSameTree(q.val)
                    else:
                        return False
tree1 = TreeNode([1,2])
tree2 = TreeNode([1,2])
print(isSameTree(tree1,tree2))

tree1 = TreeNode([2,2])
tree2 = TreeNode([1,2])
print(isSameTree(tree1,tree2))

tree1 = TreeNode([2,2])
tree2 = TreeNode([1,None,2])
print(isSameTree(tree1,tree2))

