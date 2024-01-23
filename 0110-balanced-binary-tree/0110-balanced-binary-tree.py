# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbal = True 
        
        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            if left_depth is None or right_depth is None:
                return None 
            
            if abs(left_depth - right_depth) > 1:
                self.isbal = False
            else:
                return max(left_depth, right_depth) + 1 
            
        depth(root)
        
        return self.isbal