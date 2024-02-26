# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global res
        res=True
        def check(p,q):
            global res
            if not p and not q:
                return
            if p is None or q is None:

                res=res and False
                return
            if q.val!=p.val:
                res=res and False

            check(p.left,q.left)
            check(p.right,q.right)
     
        check(p,q)
        return res