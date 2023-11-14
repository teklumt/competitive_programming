class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res=0
        stack=[]
        for i in word:
            if stack and stack[-1]>i:
                if len(set(stack))==5:
                    res=max(res,len(stack))
                
                stack=[i] if i=='a' else []
            else:
                stack.append(i)
        if stack and len(set(stack))==5:
            res=max(res,len(stack))
        return res