# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        maxx = 0

        def traversal(root):
            nonlocal maxx

            if not root:
                return (0, inf, -inf)
            
            curSumLeft, leftMin, leftMax = traversal(root.left) 
            curSumRight, rightMin, rightMax = traversal(root.right) 

            minn = min( leftMin, rightMin, root.val) 
            maxIn = max ( leftMax, rightMax, root.val) 

            if leftMax < root.val < rightMin:

                maxx = max(maxx, curSumLeft + curSumRight + root.val)

                return (curSumLeft + curSumRight + root.val , minn, maxIn)
            else:
                return (-inf, minn, maxIn)

        traversal(root)
        return maxx
        