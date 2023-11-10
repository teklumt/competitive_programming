class Solution:
    def calculate(self, s: str) -> int:
        opp=['+','-','*','/']
        numstack=[]
        oppstack=['+']
        cur=""
        res=0
        for i in s:
            if i!=" ":
                if i in opp:
                    if oppstack[-1]=='*':
                        numstack.append(str(int((int(numstack.pop())*int(cur)))))
                        oppstack.pop()
                    elif oppstack[-1]=='/':
                        numstack.append(str(int((int(numstack.pop())/int(cur)))))
                        oppstack.pop()
                    else:
                        numstack.append(cur)
                    oppstack.append(i)
                    cur=""
                else:
                    cur+=i
        if cur!="":
            if oppstack[-1]=='*':
                        numstack.append(str(int((int(numstack.pop())*int(cur)))))
                        oppstack.pop()
            elif oppstack[-1]=='/':
                        numstack.append(str(int((int(numstack.pop())/int(cur)))))
                        oppstack.pop()
            else:
                numstack.append(cur)
        
        while numstack and oppstack:
            n=oppstack.pop()
            if n=='+':
                res+=int(numstack.pop())
            elif n=='-':
                res-=int(numstack.pop())
            elif n=='*':
                res*=int(numstack.pop())
        return res