class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
            stack=[]
            strlist=list(str(n))
            k=len(strlist)

            for i in range(k):
                if stack and stack[-1]>strlist[i]:
                    while i>=1 and len(stack)>=2 and stack[-1]==stack[-2]:
                        i-=1
                        stack.pop()
                    stack[-1]=str(int(stack[-1])-1)
                    if len(stack)==1 and stack[-1]=="0":
                        stack.pop()
                    stack+=["9"]*(k-i)
                    break
                else:
                    stack.append(strlist[i])
            
            return int("".join(stack))
                
            