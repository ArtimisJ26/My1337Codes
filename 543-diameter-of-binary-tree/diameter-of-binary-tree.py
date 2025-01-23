# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        def findDiameter(node, maxim):
            if not node:
                return 0

            left = findDiameter(node.left, maxim)
            right = findDiameter(node.right, maxim)
            
            maxim[0] = max(maxim[0], left + right)

            return max(left,right) + 1
        
        maxim = [0]

        findDiameter(root, maxim)

        return maxim[0]