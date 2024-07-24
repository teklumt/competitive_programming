# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findPath(root,path, value):
            if not root: return
            if root.val == value:
                return path
            path.append('L')
            res = findPath(root.left,path,value)
            if res: return res

            path.pop()
            path.append('R')
            res = findPath(root.right,path,value)
            if res: return res

            path.pop()
            return
        
        startPath  = findPath(root,[], startValue)
        endPath  = findPath(root,[], destValue)
        ptr = 0
        while ptr < min(len(startPath), len(endPath)) and startPath[ptr] == endPath[ptr]: ptr += 1
        
        return 'U' * len(startPath[ptr:]) + "".join(endPath[ptr:]) 
        
