# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, depth):
            nonlocal res
            if not node:
                res = max(res, depth)
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        if root:
            dfs(root, 0)
        
        return res