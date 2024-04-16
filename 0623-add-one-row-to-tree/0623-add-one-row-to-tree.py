# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        queue = deque([[root,1]])
        curr = TreeNode(val)
        if depth == 1:
            
            curr.left = root
            return curr

        while queue:
            node ,level = queue.popleft()
            if not node:continue
            if level + 1 == depth:
              
                left = node.left
                right = node.right
               
               
                node.right = TreeNode(val)
                node.left = TreeNode(val)
                node.right.right = right
                node.left.left = left

                queue.append([left , level + 1])
                queue.append([right , level + 1])
            else:
                queue.append([node.left, level+1])
                queue.append([node.right, level+1])

        return root

