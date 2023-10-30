class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res=1
        win=[]
        left=0
        for i in range(len(nums)):
            win.append(nums[i])
            if len(win)>1:
                flag=True
                n=list(combinations(win,2))
                for j in n:
                    if j[0] & j[1] !=0:
                        flag=False
                        break
                if flag==False:
                    del win[0]
            res=max(res,len(win))

        return res