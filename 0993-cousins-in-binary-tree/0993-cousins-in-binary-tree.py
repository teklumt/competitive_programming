# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = defaultdict(set)
        queue = deque([[root, 0]])
        temp = defaultdict(set)

        while queue:
            node, level = queue.popleft()
            if not node: continue
            if node.right:
                temp[node.val].add(node.right.val)
            if node.left:
                temp[node.val].add(node.left.val)
           

            res[level].add(node.val)
            queue.append([node.left, level + 1])
            queue.append([node.right, level + 1])
        bol = False
        for currN in res:
            if x in res[currN] and y in res[currN]:
                bol = True
                break
    
        for currN in temp:
            if x in temp[currN] and y in temp[currN]:
             
                bol = False
                break

        
        return bol
        


        