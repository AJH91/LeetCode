class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def preorderTraversal(self,root):
        elements = []
        if root:
            elements.append(root.val)
            elements += self.preorderTraversal(root.left)
            elements += self.preorderTraversal(root.right)
        return elements

def postorderTraversal(self,root):
    elements = []
    if root:
        elements += self.postorderTraversal(root.left)
        elements += self.postorderTraversal(root.right)
        elements.append(root.val)
    return elements







