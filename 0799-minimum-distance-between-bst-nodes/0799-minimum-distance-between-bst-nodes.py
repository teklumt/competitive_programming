# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        def func(root):
            nonlocal res
            if not root:return
            res.append(root.val)
            func(root.left)
            func(root.right)
        func(root)
        ans = inf
        for i in range(len(res)):
            for j in range(len(res)):
                if i != j:
                    ans = min(ans, abs(res[i] - res[j]))
        return ans

