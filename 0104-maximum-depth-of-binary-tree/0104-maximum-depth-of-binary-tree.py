# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left_depth, right_depth = 0, 0 
        
        if root:
            if root.left is not None or root.right is not None:
                if root.left:
                    left_depth = 1 + self.maxDepth(root.left)
                if root.right:
                    right_depth = 1 + self.maxDepth(root.right)
            else:
                return 1

            if left_depth > right_depth:
                return left_depth
            else:
                return right_depth
        else:
            return 0
            