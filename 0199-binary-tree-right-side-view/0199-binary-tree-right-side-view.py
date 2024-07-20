# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([[root, 0]])
        res = []
        
        while queue:
            root , level = queue.popleft()
            if not root: continue

            if len(res) <= level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            queue.append([root.left, level + 1])  
            queue.append([root.right, level + 1])
        # print(res)
        return [level[-1] for level in res]  