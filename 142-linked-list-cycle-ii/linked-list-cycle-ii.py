# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head
        fast = slow.next
        seen = {}
        
        while fast:
            if fast in seen:
                return fast
            seen[slow] = slow.val
            fast = fast.next
            slow = slow.next
        
        return None            