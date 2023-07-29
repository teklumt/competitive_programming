class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        myhash = {}
        for i in range(len(nums)):
            myhash[nums[i]] = i
        for i in range(len(operations)):
            index = myhash[operations[i][0]]
            nums[index] = operations[i][1]
            del myhash[operations[i][0]]
            myhash[operations[i][1]] = index
        return nums