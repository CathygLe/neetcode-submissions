"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None 
        

        curr = head
        copy = {}
        
        while curr: 
            if curr not in copy: 
                copy[curr] = Node(curr.val, None)
            curr = curr.next 
        
        curr = head 

        while curr:
            copy[curr].next = copy.get(curr.next)
            copy[curr].random = copy.get(curr.random)

            curr = curr.next 
        return copy[head]





        