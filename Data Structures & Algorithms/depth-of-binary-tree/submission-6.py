# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []

        stack.append([root,1])
        height = 0

        while stack:
            node, val = stack.pop()

            if node:
                height = max(height, val)

                stack.append([node.left, val +1])
                stack.append([node.right, val + 1])

        return height


            



        