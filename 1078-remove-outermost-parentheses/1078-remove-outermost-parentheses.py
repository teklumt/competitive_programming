class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                ind = stack.pop()
                if not stack:
                    temp.add(ind)
                    temp.add(i)
        res = ""
        for i in range(len(s)):
            if i not in temp:
                res += s[i]
        return res

