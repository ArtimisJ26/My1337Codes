# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
            
        curr = head
        prevNode = None

        while curr:
            # step 1: save the next of curr node
                nextNode = curr.next
            # step 2: change the next pointer of curr node
                curr.next = prevNode
            # step 3: save the current node
                prevNode = curr
            # step 4: move on
                curr = nextNode

        return prevNode

                