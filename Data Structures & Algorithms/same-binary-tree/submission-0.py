# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are null: identical at this branch
        if not p and not q:
            return True
        
        # One is null or values differ: not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check both subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)