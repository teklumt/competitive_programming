# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        tot = []
        temp = []
        summ = 0
        def dfs(node):
            nonlocal summ
            if not node:
                return 
            temp.append(node.val)
            summ += node.val
            
            dfs(node.left)
            dfs(node.right)
            if summ == targetSum and (node.left is None) and (node.right is None):
                tot.append(temp.copy())
            summ -= temp.pop()
        dfs(root)
        return tot
