class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        # hashmap={}
        stack=[]
        for i in range(2*len(nums)):
            i=i%len(nums)
            while stack and stack[-1][-1]<nums[i]:
                index,val=stack.pop()
                res[index]=nums[i]
            stack.append([i,nums[i]])
        return res
