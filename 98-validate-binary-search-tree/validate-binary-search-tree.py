# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node, low, high):
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
              
        return dfs(root, -math.inf, math.inf)