class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        for i in s:
            # print(res)
            if res and res[-1][0] == i:
                if res[-1][1] + 1 == k:
                    res.pop()
                else:
                    res[-1][1] += 1
            else:
                res.append([i, 1])   
        ans = ""
        for i, j in res:
            ans += i * j 
        return ans