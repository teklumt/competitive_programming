class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def findSubset(nums):
            Subsets, curSubSet = [], []
            BackTrack(0, Subsets, curSubSet, nums)
            return Subsets

        def BackTrack(i, Subsets, curSubSet, nums):
            if i>=len(nums):
                Subsets.append(curSubSet.copy())
                return
            
            curSubSet.append(nums[i])
            BackTrack(i + 1, Subsets, curSubSet, nums)
            curSubSet.pop()

            BackTrack(i + 1, Subsets, curSubSet, nums)
            
        return findSubset(nums)