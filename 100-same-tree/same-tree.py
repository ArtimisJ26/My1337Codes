# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return False if self.compare(p,q) == False else True
    
    def compare(self, nodep, nodeq):
        if nodep == None or nodeq == None:
            if nodep == None and nodeq == None:
                return -1
            else:
                return False

        if nodep.val != nodeq.val:
            return False
        
        leftMatch = self.compare(nodep.left, nodeq.left)
        rightMatch = self.compare(nodep.right, nodeq.right)

        if leftMatch == False or rightMatch == False:
            return False

