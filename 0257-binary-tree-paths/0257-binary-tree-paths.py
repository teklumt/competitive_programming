# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return
        res = []
        temp = []
        def func(root):
            if not root:return

            temp.append(str(root.val))
            func(root.left)
            func(root.right)
            if not root.left and not root.right:
                res.append("->".join(temp))
            temp.pop()
        func(root)
        return res

