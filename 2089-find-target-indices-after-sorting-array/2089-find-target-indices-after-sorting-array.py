class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new=[]
        nums.sort()
        for n in range(len(nums)):
            if nums[n]==target:
                new.append(n)
        return new