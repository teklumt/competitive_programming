class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        right  = s.count(')')
        left = 0
        res = []
        for i in s:
            if i == '(':
                if right:
                    res.append(i)
                    left += 1
                    right -= 1
            elif i == ')':
                if left:
                    res.append(i)
                    left -= 1
                else:
                    right -= 1
            else:
                res.append(i)
        return "".join(res)
