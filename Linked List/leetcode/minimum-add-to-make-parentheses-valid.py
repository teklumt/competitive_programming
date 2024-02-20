class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=Counter()
        res=0
        for i in s:
            if i ==')':
                if count['(']>0:
                    count['(']-=1
                else:
                    # count[')']+=1
                    res+=1
            else:
                count['(']+=1
        return res+count['(']