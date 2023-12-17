class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num=[]
        res=[]
        for i in  grid:
            num+=i
        store=Counter(num)
        for  i in store:
            if store[i]>1:
                res.append(i)
                break
        num.sort()
        for i in range(1,len(num)*len(num)):
            if i not in store:
                res.append(i)
                break
            
        if len(res)!=2:
            res.append(num[-1]+1)
        return res