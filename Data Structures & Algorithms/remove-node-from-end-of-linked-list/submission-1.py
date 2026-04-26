# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)

        count = 0
        right = None      
        curr = head  
        left = temp

        while count < n and curr:
            count += 1      
            right = curr
            curr = curr.next 
        
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return temp.next

        