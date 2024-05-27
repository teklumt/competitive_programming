class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return 0
        check = set(stones)
        memo = defaultdict(set)
        memo[0] = {1}
        memo[1] = {1}
        
       
        for i in stones[1:]:
            for j in memo[i]:
                for k in (j + 1, j - 1, j):
                    if k > 0 and i + k in check:
                        memo[i + k].add(k)
        return memo[stones[-1]]