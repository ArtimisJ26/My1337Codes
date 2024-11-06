# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(mainNode, subNode):
            if not mainNode or not subNode:
                if not mainNode and not subNode:
                    return True
                return False

            if mainNode.val == subNode.val:
                leftChild = dfs(mainNode.left, subNode.left)
                rightChild = dfs(mainNode.right, subNode.right)

                if leftChild and rightChild:
                    return True
            
            return False

        def findRoot(mainNode):
            if not mainNode:
                return False
            
            if mainNode.val == subRoot.val:
                if dfs(mainNode, subRoot):
                    return True
            
            return findRoot(mainNode.left) or findRoot(mainNode.right)

        return findRoot(root)