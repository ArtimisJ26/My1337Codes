# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        level = 0

        while queue:
            level_length = len(queue)
            res.append([])

            for i in range(level_length):
                curr = queue.popleft()

                res[level].append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
                
            level += 1

        for i, arr in enumerate(res):
            if i%2==1:
                res[i] = arr[::-1]
                
        return res
