# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Shift right n times over so there is always a gap of n between left and right
        while n > 0:
            right = right.next
            n -= 1
        
        # Find the last node 
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
            
        