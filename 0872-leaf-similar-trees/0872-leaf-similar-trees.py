# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = list(), list()
        
        def leaf_func(root, leaf):
            
            if root.left is None and root.right is None:
                leaf.append(root.val)
                return 
            
            if root.left is not None:
                leaf_func(root.left, leaf)
            if root.right is not None:
                leaf_func(root.right, leaf)
            
        leaf_func(root1, leaf1)
        leaf_func(root2, leaf2)
        
        return leaf1 == leaf2
            