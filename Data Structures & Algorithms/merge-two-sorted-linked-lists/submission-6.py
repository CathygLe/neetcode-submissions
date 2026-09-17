# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1 = list1 
        start2 = list2 
        start = ListNode(0, None)
        head = start 

        while start1 and start2:
            if start1.val < start2.val:
                head.next = start1
                start1 = start1.next 
            else:
                head.next = start2 
                start2 = start2.next 
            
            head = head.next 
        
        if start1:
            head.next = start1
        else:
            head.next = start2 
        
        return start.next

