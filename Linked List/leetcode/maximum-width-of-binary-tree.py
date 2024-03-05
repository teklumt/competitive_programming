# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        store = defaultdict(list)
        maxx = 1

        def traverse(root, level,idx):
            nonlocal store
            if not root: return

            store[level].append(idx)
            traverse(root.left, level + 1 ,idx*2)
            traverse(root.right, level + 1 ,idx*2 + 1)
        traverse(root, 0 ,0)
        # print(store)
        
        for i in store:
            maxx  = max (maxx, store[i][-1] - store[i][0] + 1)
        return maxx
