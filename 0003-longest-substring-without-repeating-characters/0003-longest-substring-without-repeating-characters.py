class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=[]
        if len(s)==1:
            return 1
        if s=="":
            return 0
        for n in range(len(s)-1):
            check=""
            check+=s[n]
            for m in range(n+1,len(s)):
                if s[m] not in check:
                    check+=s[m]
                else:
                    break
            result.append(check)
        maxx=0
        for m in range(len(result)):
            if len(result[m])>maxx:
                maxx=len(result[m])
        return maxx
