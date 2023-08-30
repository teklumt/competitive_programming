class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        summ=0
        for i in nums:
            summ+=i
            result.append(summ)
        return result