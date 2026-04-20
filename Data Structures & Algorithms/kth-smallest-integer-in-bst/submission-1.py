# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []

        count = 0
        cur = root

        # while we have smt in our stack or root exists
        while stack or cur:

            # find the left most val (aka smallest)
            while cur:
                stack.append(cur)
                cur = cur.left 

            # no more left elements, so take the last one added
            cur = stack.pop()
            count += 1

            # If equals, return
            if count == k:
                return cur.val
            
            # else move to the next right element
            cur = cur.right

            

            
        