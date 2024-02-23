# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(root,ans):
            if not root:
                ans.append(None)
                return
            ans.append(root.val)
            check(root.left,ans)
            check(root.right,ans)
            return ans
        tree1=check(p,[])
        tree2=check(q,[])
        return tree1==tree2