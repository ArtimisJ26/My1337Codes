# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            if p == None and q == None:
                return -1
            else:
                return False

        if p.val != q.val:
            return False
        
        leftMatch = self.isSameTree(p.left, q.left)
        rightMatch = self.isSameTree(p.right, q.right)

        if leftMatch == False or rightMatch == False:
            return False
        else:
            return True