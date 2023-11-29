class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        new=[]
        nub=True
        x=0
        for c in strs:
            new.append(len(c))
        m=new.index(min(new))
        while x<len(strs[m]):
            check=strs[0][x]
            for n in strs:
                if check not in n[x]:
                    nub=False
                    break 
            if nub:
                result=result+check
            x=x+1
        return result

