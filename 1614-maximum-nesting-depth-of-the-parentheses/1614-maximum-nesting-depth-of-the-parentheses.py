class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            elif i == ')':
                stack.pop()
            res = max(res, len(stack))
        return res
        