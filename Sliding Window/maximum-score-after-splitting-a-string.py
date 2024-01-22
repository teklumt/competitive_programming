class Solution:
    def maxScore(self, s: str) -> int:
        zero_count=[]
        one_count=[]
        for i in s:
            if i=='0':
                if zero_count:
                    zero_count.append(zero_count[-1]+1)
                else:
                    zero_count.append(1)
            else:
                if zero_count:
                    zero_count.append(zero_count[-1])
                else:
                    zero_count.append(0)
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                if one_count:
                    one_count.append(one_count[-1]+1)
                else:
                    one_count.append(1)
            else:
                if one_count:
                    one_count.append(one_count[-1])
                else:
                    one_count.append(0)

        one_count.reverse()

        maxx=-1
        for i in range(len(s)-1):
            maxx=max(maxx,zero_count[i] + one_count[i+1])
        
        return maxx 




        