class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opp=['+', '-', '*','/']
        for i in tokens:
            if i not in opp:
                stack.append(int(i))
            else:
                res=0
                num1=stack.pop()
                num2=stack.pop()
                if i=='+':
                    res+=num1+num2
                elif i=='*':
                    res+=num1*num2
                elif i=='-':
                    res+=num2-num1
                elif i=='/':
                    if num1*num2 >= 0:
                        res+=num2//num1
                    else:
                        res+=-1*(abs(num2)//abs(num1))
                stack.append(res)
        return stack[-1]



