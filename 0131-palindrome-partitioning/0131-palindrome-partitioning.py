class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        buck = []
        def back(ind):
            if ind == len(s):
                res.append(buck.copy())
                return
            
            for  i in range(ind , len(s)):
                val = s[ind : i + 1 ]
                if val == val[::-1]:
                    buck.append(val)
                    back(i + 1)
                    buck.pop()
        back(0)
        return res