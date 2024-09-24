# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node: Optional[TreeNode]) -> int:
            # base case
            if not node:
                return 0
            
            left_depth = get_depth(node.left)
            # if left side is already unbalanced, rest of tree is
            if left_depth == -1:
                return -1
            
            right_depth = get_depth(node.right)
            # if right side is already unbalanced, rest of tree is
            if right_depth == -1:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1

        return get_depth(root) != -1