# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global ans
        global res

        ans=[]
        res=[]
        def dfs(root,height):
            global ans
            global res
            if not root:
                return 
            if len(res)>height:
                res[height]=str(root.val)
              
                res=res[:height+1]
            else:
               
                res.append(str(root.val))
            height+=1
            if root.right is None and root.left is None:
                ans.append("".join(res.copy()))
            print(height)
            dfs(root.left,height)
            dfs(root.right,height)
        dfs(root,0)
        
        return sum(map(int,ans))
            
