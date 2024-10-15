# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        curr = root
        res = []
        stack = [curr]
        to_delete = set(to_delete)

        def dfs(curr):
            if not curr:
                return None
            if curr.val in to_delete:
                if curr.left or curr.right:
                    if curr.left:
                        new_node = dfs(curr.left)
                        if new_node:
                            res.append(new_node)
                    if curr.right:
                        new_node = dfs(curr.right)
                        if new_node:
                            res.append(new_node)
                to_delete.remove(curr.val)
                return None

            curr.left = dfs(curr.left)
            curr.right = dfs(curr.right)

            return curr
        
        new_node = dfs(curr)
        if new_node:
            res.append(new_node)
        return res