class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for i in arr:
            pre.append(pre[-1] ^ i)
        res = []
        for l , r in queries:
            res.append(pre[r + 1] ^ pre[l])
        return res