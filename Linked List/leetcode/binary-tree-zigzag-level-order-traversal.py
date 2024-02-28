# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return
        res=[]
        queue=deque()
        queue.append((root, 0))

        while queue:

            curNode,level = queue.popleft()
            if len(res) == level:
                res.append(deque([curNode.val]))
            else:
                if level%2:
                    res[level].appendleft(curNode.val)
                else:
                    res[level].append(curNode.val)

            if curNode.left is not None:
                queue.append((curNode.left, level + 1))
            if curNode.right is not None:
                queue.append((curNode.right, level + 1))


        return res