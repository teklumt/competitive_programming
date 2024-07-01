class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = []
        for i in arr:
            if i % 2:
                res.append(i)
            else:
                res = []
            if len(res) == 3: return True
        return 