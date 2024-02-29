# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        store = defaultdict(list)

        def traverse(root,cur):
            if not root: return

            store[tuple(cur)].append(root.val)
            traverse(root.left,[cur[0]+1, cur[1]-1])
            traverse(root.right, [cur[0]+1 , cur[1]+1])

                    
        traverse(root, [0,0])
    
        store2 = defaultdict(list)
        for i  in sorted(store):
            store2[i[1]].extend(sorted(store[i]))
       
        return [ store2[i] for i in sorted(store2)]
        
