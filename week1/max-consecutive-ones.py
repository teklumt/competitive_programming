class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        win=[]
        for i in nums:
            if i==1:
                win.append(i)
            else:
                win=[]
            res=max(res,len(win))
        return res