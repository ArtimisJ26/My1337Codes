"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        
        def traverse(node):
            # if visited -> return
            if node in cloned: 
                return cloned[node]

            # add to cloned
            copy = Node(node.val)
            cloned[node] = copy

            # visit neighbors in loop
            for neighbor in node.neighbors:
                copy.neighbors.append(traverse(neighbor))
            return copy    

        return traverse(node) if node else None
 