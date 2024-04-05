# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = root.val
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node: continue

            if node.val != res:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True