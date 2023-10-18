class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while k and stack and stack[-1]>i:
                stack.pop()
                k-=1
            if len(stack)==1 and stack[-1]==str(0):
                stack.pop()
            stack.append(i)
        while stack and k:
            stack.pop()
            k-=1
        return str(0) if len(stack)==0 else "".join(stack)
    