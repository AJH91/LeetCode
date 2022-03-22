def maxDepth(self, root):
    leftCount = 0
    rightCount = 0
    leftCount += self.maxDepth(root.left)
    rightCount += self.maxDepth(root.right)
    return (leftCount+rightCount)+1



