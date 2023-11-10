class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in opp:
                stack.append(int(i))
            else:
                if len(stack) > 0:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if i == '*':
                        stack.append(num1*num2)
                    elif i == '/':
                        if num1>=0 and num2>=0:
                            stack.append((num2//num1))
                        elif num1<0 and num2<0:
                            stack.append((abs(num2)//abs(num1)))
                        else:
                            stack.append(-1*(abs(num2)//abs(num1)))

                    elif i == '+':
                        stack.append(num1+num2)
                    elif i == '-':
                        stack.append(num2-num1)
        return stack.pop()