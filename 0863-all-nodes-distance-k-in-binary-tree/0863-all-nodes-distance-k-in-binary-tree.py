# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        res = defaultdict(list)
        def traversal (root):
            if not root:return
            if root.left:
                res[root.val].append(root.left.val)
                res[root.left.val].append(root.val)
            if root.right:
                res[root.val].append(root.right.val)
                res[root.right.val].append(root.val)
            
            traversal(root.left)
            traversal(root.right)
        traversal(root)

       
        final = []
        seen = set()
  
            
        stack = [(target.val, 0)] 
               
        while stack:
            node, currSumm = stack.pop()
        
            if currSumm == k:
                final.append(node)
                continue
            for  j in res[node]:
                if j not in seen:
                    stack.append((j , currSumm + 1))
                    seen.add(node)
   
        return final if k != 0 else [target.val]
        