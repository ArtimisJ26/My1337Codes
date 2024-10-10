# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            # go left
            dfs(node.left, path + "->" + str(node.val))
            # go right
            dfs(node.right, path + "->" + str(node.val))
            if not (node.left or node.right):
                path += "->" + str(node.val)
                res.append(path[2:])
        
        dfs(root, "")
        return res