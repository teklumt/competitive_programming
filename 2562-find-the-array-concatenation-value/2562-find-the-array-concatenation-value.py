class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        strnum=[]
        for i in nums:
            strnum.append(str(i))
        l=0
        r=len(nums)-1
        res=0
        while l<=r:
            if l<r:
                nn=strnum[l]+strnum[r]
                
                res+=int(nn)
            else:
                res+=int(strnum[l])
            l+=1
            r-=1
        return res
