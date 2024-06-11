class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        myhash={}
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                myhash[nums[i]]=i
        for i in range(1,nums[-1]):
            if i not in myhash:
                return i
        return len(myhash)+1
