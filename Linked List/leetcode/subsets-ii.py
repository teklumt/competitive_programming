class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def findSubsets(nums):
            nums.sort()
            subsets, currSub = [], []
            BackTrack(0, subsets, currSub, nums)
            return subsets
        
        def BackTrack(i, subsets, currSub, nums):
            if i>= len(nums):
                subsets.append(currSub.copy())
                return
            
            currSub.append(nums[i])

            BackTrack(i + 1 ,subsets, currSub, nums)
            currSub.pop()
            while i + 1 <len(nums) and nums[i] == nums[i + 1]:
                i += 1

            BackTrack(i + 1 ,subsets, currSub, nums)
        return findSubsets(nums)