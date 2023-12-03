class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        res="1"
        i=1
        while i<n:
            num=""
            win=[]
            for j in range(len(res)):
                if win:
                    if res[j]==win[-1]:
                        win.append(res[j])
                    else:
                        num+=str(len(win))
                        num+=win[-1]
                        win=[res[j]]

                else:
                    win.append(res[j])
            if win:
                num+=str(len(win))
                num+=win[-1]
                win=[]
            res=num
            i+=1
        return res