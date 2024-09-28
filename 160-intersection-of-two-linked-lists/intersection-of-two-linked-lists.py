# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointA = headA
        pointB = headB
        seen = {}

        while pointA:
            seen[pointA] = pointA.val
            pointA = pointA.next
        
        while pointB:
            if pointB in seen:
                return pointB
            pointB = pointB.next
        
        return None

        