# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0 
        
        def find_good(root: TreeNode, max_val=float('-inf')):
            nonlocal answer 
            
            if root.val >= max_val:
                max_val = root.val 
                answer += 1 
                
            if root.left is not None:
                find_good(root.left, max_val=max_val)
            if root.right is not None:
                find_good(root.right, max_val=max_val)
                
        find_good(root)
        
        return answer 