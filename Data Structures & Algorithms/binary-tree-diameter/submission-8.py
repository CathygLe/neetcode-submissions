# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0 

        def height(root1):
            if not root1:
                return 0
            left = height(root1.left)
            right = height(root1.right)

            nonlocal maxDiameter 
            maxDiameter = max(maxDiameter, left + right)

            return max(height(root1.left), height(root1.right)) + 1 
        height(root)

        return maxDiameter
        
    
