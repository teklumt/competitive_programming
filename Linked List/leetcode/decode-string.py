class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=[]
        temp=0
        for i in s:
            if i.isdigit():
                temp=temp*10 + int(i)
            elif i.isalpha() or i=='[':
                if temp:
                    num.append(temp)
                    temp=0
                stack.append(i)
            else:
                
                res=''
                while stack[-1]!='[':
                    res=stack.pop() + res
                stack.pop()
                nn=1
                if num:
                    nn=num.pop()
                stack.append(nn*res)
                res=''
        res=''
        while stack:
            res=stack.pop()+res
        return res




