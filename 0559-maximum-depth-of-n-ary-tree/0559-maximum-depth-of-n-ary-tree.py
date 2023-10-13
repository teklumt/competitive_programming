"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        mystack=[]
        if root:
            mystack.append((root,1))
        depth=0
        while mystack:
            (node,level)=mystack.pop()
            depth=max(depth,level)
            for i in node.children:
                mystack.append((i,level+1))
        return depth