# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None 
        
        def get_ancestor(node):
            if not node:
                return False 
            temp = False
            if node.val == p.val or node.val == q.val:
                temp = True 
                
            left = get_ancestor(node.left)
            right = get_ancestor(node.right)
            
            if (left and right) or (temp and (left or right)):
                self.result = node
                
            return temp or left or right
        
        get_ancestor(root)
        
        return self.result