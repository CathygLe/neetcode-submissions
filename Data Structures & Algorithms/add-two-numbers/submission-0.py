# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #initialize the beginning
        dummy = ListNode()
        cur = dummy 

        carry = 0
        while l1 or l2 or carry:
            # assign numbers to val 1 and val 2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # result of adding 1 and 2
            res = val1 + val2 + carry
            carry = res // 10
            # result is values in ones place value
            res = res % 10

            cur.next = ListNode(res)

            #update 
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next