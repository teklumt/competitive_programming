# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createTree(nums):
            if not nums:
                return
            ind = nums.index(max(nums))
            return TreeNode(max(nums),createTree(nums[:ind]),createTree(nums[ind+1:]))
        return createTree(nums)
