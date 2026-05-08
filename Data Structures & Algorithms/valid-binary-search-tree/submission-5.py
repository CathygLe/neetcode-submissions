# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, minsf, maxsf):
            if not node:
                return True
            
            if not (minsf < node.val < maxsf):
                return False 
            
            return check(node.left, minsf, node.val) and check(node.right, node.val, maxsf)
        return check(root, float("-inf"), float("inf"))    