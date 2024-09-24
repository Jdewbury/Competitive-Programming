"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}

        def clone(node):
            if not node:
                return
            elif node.val in self.visited:
                return self.visited[node.val]

            clone_node = Node(node.val)
            self.visited[node.val] = clone_node

            for neigh in node.neighbors:
                clone_node.neighbors.append(clone(neigh))

            return clone_node

        return clone(node)