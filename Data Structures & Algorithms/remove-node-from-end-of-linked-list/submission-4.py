# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 5 
        # right 5 
         
        temp = ListNode(0, head)

        right = temp
        count = 0 
        curr = head
         
        while count < n and curr:
            right = curr
            curr = curr.next
            count += 1 
            

        left = temp 
    
        while right.next:
            left = left.next
            right = right.next
        
        
        left.next = left.next.next 
        
        return temp.next

        




        


        