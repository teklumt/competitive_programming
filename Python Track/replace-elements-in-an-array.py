class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash={}

        for i in range(len(nums)):
            hash[nums[i]]=i
        
        for operation in operations:

            index = hash[operation[0]]
            del hash[operation[0]]
            hash[operation[1]] = index
            nums[index]=operation[1]
               
        return nums