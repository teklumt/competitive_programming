class Solution:
    def decodeString(self, s: str) -> str:
        res=''
        num=0
        numStore=[]
        chrStore=[]
        
        for i in s:
            if i.isdigit():
                num=num*10 + int(i)
            
            elif i=='[':
                
                numStore.append(num)
                chrStore.append(res)
                num=0
                res=''
                
            elif i==']':
                res=chrStore.pop() + res*numStore.pop()
            
            else:
                res+=i
        return res
                