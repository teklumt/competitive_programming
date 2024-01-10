class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        num=0
        res=[]
        for i in p:
            num+=hash(i)
        
        summ=0
        j=0
        for i in range(len(p)):
            summ+=hash(s[i])
        if num==summ:
            res.append(j)
        
        
        for i in range(len(p),len(s)):
            summ-=hash(s[j])
            summ+=hash(s[i])
            j+=1
            if summ==num:
                res.append(j)
        # if summ==num:
        #     res.append(len(s)-len(p))
        return res



















        n=len(p)
        str1=Counter(p)
        res=[]
        j=0
        bol=True
        temp=Counter(p)
        for i in range(len(s)):
            if i-j+1<n:
                win.append(s[i])
            elif bol:
                temp=Counter(win)
                if temp==str1:
                    res.append(j)
                win.popleft()
                win.append(s[i])
                j+=1
                bol=False
            else:
                nn=True
                for k in str1:
                    if str1[k]!=temp[k]:
                        nn=False
                        break
                if nn:
                    res.append(j)
                temp[s[j]]-=1
                temp[s[i]]+=1
                j+=1
        if temp:
            nn=True
            for k in str1:
                if str1[k]!=temp[k]:
                    nn=False
                    break
            if nn:
                res.append(j)
            temp[s[j]]-=1
            temp[s[i]]+=1
        return res
            





            
        
        # if win:
        #     temp=Counter(win)
        #     if temp==str1:
        #         res.append(j)
        #     win.popleft()
        #     win.append(s[i])
        #     j+=1
        # return res





        #         bol=True
        #         for k in str1:
        #             if str1[k]!=temp[k]:
        #                 bo=False
        #                 break
        #         if bol:
        #             res.append(j)
        #         win.popleft()
        #         win.append(s[i])
        #         j+=1
        # # if win:
        # #     temp=Counter(win)
        # #     bol=True
        # #     for k in str1:
        # #         if str1[k]!=temp[k]:
        # #             bo=False
        # #             break
        # #     if bol:
        # #         res.append(j)
        # #     win.popleft()
        # #     win.append(s[i])
        # return res
                








        n=len(p)
        str1=sorted(list(p))
        str2=deque(list(s[:n]))
        res=[]
        left=1
        if str1==sorted(str2):
            res.append(0)
        for i in range(n,len(s)):
            str2.popleft()
            str2.append(s[i])
            if str1==sorted(str2):
                res.append(left)
            left+=1
        return res
