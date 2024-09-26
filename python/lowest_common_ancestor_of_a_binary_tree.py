# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path_p = []
        self.path_q = []

        def get_path(node, path, target):
            if not node:
                return None
            if node == target:
                path.append(node)
                return node

            left = get_path(node.left, path, target)
            right = get_path(node.right, path, target)

            if left or right:
                path.append(node)
                return node

            return None

        get_path(root, self.path_q, q)
        get_path(root, self.path_p, p)
        
        lowest_node = root

        for i in range(1, min(len(self.path_q), len(self.path_p)) + 1):
            if self.path_q[-i] == self.path_p[-i]:
                lowest_node = self.path_q[-i]

        return lowest_node