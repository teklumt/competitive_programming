# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=Counter()
        def traverse(root):
            if not root:
                return
            count[root.val]+=1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        maxx=max(count.values())
        
        return [x for x in count if count[x]==maxx]

    