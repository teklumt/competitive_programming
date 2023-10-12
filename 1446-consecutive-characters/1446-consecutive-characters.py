class Solution:
    def maxPower(self, s: str) -> int:
        res=0
        win=[]
        j=0
        if len(s)==1:
            return 1
        else:
            for i in range (len(s)):
                if len(win)!=0:
                    if s[i]==win[-1]:
                        win.append(s[i])
                        res=max(res,len(win))
                    else:
                        res=max(res,len(win))
                        win=[]
                        j=i
                        win.append(s[i])
                else:
                    win.append(s[i])
            return res
            