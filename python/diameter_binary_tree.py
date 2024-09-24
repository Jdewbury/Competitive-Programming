# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0
        
        def get_depth(node):
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            self.max_diam = max(self.max_diam, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        get_depth(root)

        return self.max_diam