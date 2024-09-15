"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            for i in node.children:
                queue.append((i , level + 1))
        return res


        