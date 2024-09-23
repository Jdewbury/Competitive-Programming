# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root

        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        # recursively iterate through subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return dummy