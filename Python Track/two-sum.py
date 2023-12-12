class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash={}
        for i in range(len(nums)):
            myhash[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in myhash:
                if myhash[target-nums[i]] !=i:
                    return [i,myhash[target-nums[i]]]
