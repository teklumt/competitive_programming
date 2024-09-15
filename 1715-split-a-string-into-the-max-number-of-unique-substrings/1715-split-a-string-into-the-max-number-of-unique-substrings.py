class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        res = 0
        buck = []
        def backtrack(i):
            nonlocal res 
            if i == len(s):
                res = max(res, len(buck.copy()))
                return
            for j in range(i + 1, len(s) + 1):
                cur = s[i: j]
                if cur not in seen:
                    buck.append(cur)
                    seen.add(cur)
                    backtrack(j)
                    seen.remove(buck.pop())
        backtrack(0)
        return res
