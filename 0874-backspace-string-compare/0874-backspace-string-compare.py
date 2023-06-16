class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        num1 = []
        num2 = []
        n1 = list(s)
        n2 = list(t)
        for n in range(len(n1)):
            if n1[n] != "#":
                num1.append(n1[n])
            else:
                if len(num1)!=0:
                    num1.pop()

        for n in range(len(n2)):
            if n2[n] != "#":
                num2.append(n2[n])
            else:
                if len(num2)!=0:
                    num2.pop()

        return num1 == num2