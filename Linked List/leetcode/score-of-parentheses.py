class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        tempStack=[]
        res=0
        temp=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(['(',1])
                tempStack.append(temp)
                temp=0
            else:
                stac=stack.pop()
                num=tempStack.pop()
                
                if stack:
                    stack[-1][1]=2
                if stac[1]==1:
                    num+=1
                    if tempStack:
                        tempStack[-1]+=num
                    else:
                         
                        tempStack.append(num)
                else:
                    if tempStack:
                        tempStack[-1]+=num*2
                    else:
                        tempStack.append(num*2)
                temp=0
        return tempStack[-1]

                    
                        

                        
                