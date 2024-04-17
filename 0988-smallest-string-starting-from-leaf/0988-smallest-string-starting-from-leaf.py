# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
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
                res[height]=chr(root.val+97)
                # print(res)
                res=res[:height+1]
            else:
                # print(res)
                res.append(chr(root.val+97))
            height+=1
            if root.right is None and root.left is None:
                ans.append("".join(res.copy()[::-1]))
            # print(height)
            dfs(root.left,height)
            dfs(root.right,height)
        dfs(root,0)
        # print(ans)
        
        return min(ans)
            
