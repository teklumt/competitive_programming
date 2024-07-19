# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        res = 0        
        def dfs(node):
            nonlocal res
            if not node:
                return []
            if not node.right and not  node.left:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)

            for i in right:
                for j in left:
                    if i  + j <= distance:
                        res += 1
            return [i + 1 for i in left + right]
        dfs(root)
        return res
            


        