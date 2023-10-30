class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        hash={}
        res=0
        for i in range(len(colors)):
            hash[i]=neededTime[i]
        win=[]
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                if i==1:
                    win.append(hash[i])
                    win.append(hash[i-1])
                else:
                    win.append(hash[i])
            else:
                if win:
                    res+=sum(win)-max(win)
                win=[hash[i]]
        if len(win)>1:
            res+=sum(win)-max(win)
        return res