# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2 
        curr = ListNode() 
        start = curr


        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None
        
        while head1 and head2: 

            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next 

            else: 
                curr.next = head2
                head2 = head2.next 
                
            curr = curr.next 

        if not head1 and head2:
            curr.next = head2 
        
        if not head2 and head1:
            curr.next = head1 
        
        return start.next
            
        