# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traversal(root):
            
            arr=[[]]
            
            def dfs(root):
                
                if root==None:
                    return -1
                
                leftLevel=dfs(root.left)
                rightLevel=dfs(root.right)
                
                currentLevel= max(leftLevel,rightLevel)+1
                
                while len(arr) <= currentLevel:
                    arr.append([])
                
                arr[currentLevel].append(root.val)
                return currentLevel
            
            dfs(root)
            
            return arr
        
        return traversal(root1)[0]==traversal(root2)[0]