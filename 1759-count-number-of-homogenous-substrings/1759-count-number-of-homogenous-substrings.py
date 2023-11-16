class Solution:
    def countHomogenous(self, s: str) -> int:
        Mod=10**9 + 7
        res=0
        stack=[]
        for i in s:
            if stack:
                if i ==stack[-1]:
                    stack.append(i)
                else:
                    n=len(stack)
                    res+=(n*(n+1))//2
                    stack=[i]
            else:
                stack.append(i)
        n=len(stack)
        res+=(n*(n+1))//2
        return res % Mod