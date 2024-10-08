"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):            
            for i in node.children:
                dfs(i)
            res.append(node.val)
            
        if root:dfs(root)

        return res
        