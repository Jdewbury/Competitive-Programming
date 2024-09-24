# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = {}
        def get_depth(node, depth):
            if not node:
                return

            get_depth(node.left, depth+1)
            get_depth(node.right, depth+1)

            if depth not in self.levels:
                self.levels[depth] = [node.val]
            else:
                self.levels[depth].append(node.val)

        get_depth(root, 0)
        
        return [self.levels[d] for d in sorted(self.levels.keys())]