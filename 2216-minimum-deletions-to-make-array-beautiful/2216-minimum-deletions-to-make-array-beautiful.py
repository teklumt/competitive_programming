class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[]
        count=0
        for i in nums:
            if stack and len(stack)%2!=0 and i==stack[-1]:
                count+=1
            else:
                stack.append(i)
        
        return count if len(stack)%2==0 else count+1