# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, minBound, maxBound):
            if not node:
                return True
            
            if not (minBound < node.val and maxBound > node.val):
                return False
            
            return (check(node.left, minBound, node.val ) and 
                   check(node.right, node.val, maxBound ))

        return check(root, float("-inf"), float("inf"))
            
            
            


            


        