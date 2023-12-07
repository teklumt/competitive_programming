class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=[]
        if 0 not in nums:
               return 0
        for n in nums:
            if n+1 not in nums:
                result.append(n+1)
                
        return min(result)