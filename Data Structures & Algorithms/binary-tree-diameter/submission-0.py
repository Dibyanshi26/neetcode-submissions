# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            nonlocal longest
            if not node:
                return 0

            # Get the max depth/height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Diameter passing through this node
            diameter = left_height + right_height
            longest = max(longest, diameter)

            # Return height of this subtree to the parent
            return 1 + max(left_height, right_height)

        dfs(root)
        return longest